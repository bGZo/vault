---
comments: true
draft: true
aliases:
  - 在 Steam Deck 上开启用户级别的 SMB
created: 2025-09-16T21:21:32
modified: 2025-12-08T22:17:15
tags: []
title: 在 Steam Deck 上开启用户级别的 SMB
---

# 在 Steam Deck 上开启用户级别的 SMB

重要性不言而喻，远程打个补丁，从 SD 上下载点文件都非常有用，导出一些游戏也比较实用。

传统上，SMB 必须使用 Sudo 开启，但是 SteamOS 这种不可变系统有个毛病就是，每次更新完系统，之前所有的东西全部重装，包括你的 SMB，而跳过系统更新对于 SD 来说更是不可能，这点简直是跟 MC 学的，笑死。

所以一个合理的方案就是一用户级别的权限开启 SMB，这需要走一些弯路。

## 前置要求：HomeBrew

相比于 ArchLinux 自带的 Pacman 管理器，HB 完全安装在本地用户目录，不会被 SD 的系统更新整挂掉，所以比较方便，我们需要借助 HB 安装 SMB，安装时间比较久，运行：

```shell
brew install samba
# 检查是否安装成功
smbd -v
# 检查下安装路径
where smbd
```

## 保存配置文件

```shell
cat /home/deck/env/linux/samba/deck.conf
#
# Sample configuration file for the Samba suite for Debian GNU/Linux.
#
#
# This is the main Samba configuration file. You should read the
# smb.conf(5) manual page in order to understand the options listed
# here. Samba has a huge number of configurable options most of which 
# are not shown in this example
#
# Some options that are often worth tuning have been included as
# commented-out examples in this file.
#  - When such options are commented with ";", the proposed setting
#    differs from the default Samba behaviour
#  - When commented with "#", the proposed setting is the default
#    behaviour of Samba but the option is considered important
#    enough to be mentioned here
#
# NOTE: Whenever you modify this file you should run the command
# "testparm" to check that you have not made any basic syntactic 
# errors. 

#======================= Global Settings =======================

[global]
   # 将运行所需目录放到用户目录
   pid directory = /home/deck/.local/var/samba/run
   lock directory = /home/deck/.local/var/samba/lock
   state directory = /home/deck/.local/var/samba/state
   cache directory = /home/deck/.local/var/samba/cache
   private dir = /home/deck/.local/var/samba/private

   # 日志放到用户目录
   log file = /home/deck/.local/var/log/samba/log.%m
   logging = file
   max log size = 1000

   server role = standalone server
   map to guest = bad user

   # 关闭打印相关，避免依赖系统路径和权限
   load printers = no
   printing = bsd
   printcap name = /dev/null
   disable spoolss = yes

   # 端口
   smb ports = 1445


[deck]
    path = /home/deck
    browseable = yes
    writable = yes
    read only = no
    guest ok = no
    valid users = deck
    create mask = 0660
    directory mask = 0770

[sd]
    path = /run/media/deck/deck/
    browseable = yes
    writable = yes
    read only = no
    guest ok = no
    valid users = deck
    create mask = 0660
    directory mask = 0770
```

> [!NOTE]
> 配置文件里有个坑，就是端口不能是一般的 SMB 端口，如 445，所以我在上面配置中改成了 1445，可能是权限保留问题，总之，如果是 445 端口，总是连接超时。

## 开启自启动

就像前面说的，开启自启动的文件最好还是放在用户目录，目录在 `/home/deck/.config/systemd/user`，编辑文件：

```shell
[Unit]
Description=User-level SMB Service for Deck
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
```

保存，重载并启动配置文件：

```shell
systemctl --user daemon-reload
systemctl --user enable --now deck-smb.service
```

接下来应该就可以放心使用了，一劳永逸。Mac 连接服务器：

```shell
smb://192.168.31.29:1445/deck
```

## 配置中踩的一些坑

第一次启动报错启动太快，无法开启用户级别的 SMB：

```shell
~/.config/systemd/user > systemctl --user status smb.service                                                                       
× smb.service - User-level SMB Service for Deck
     Loaded: loaded (/home/deck/.config/systemd/user/smb.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Mon 2025-09-15 00:21:48 +08; 19s ago
   Duration: 72ms
 Invocation: 6b48f8fc4ef041bba66f33868b3b21bd
   Main PID: 33601 (code=exited, status=1/FAILURE)

Sep 15 00:21:48 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 5.
Sep 15 00:21:48 steamdeck systemd[1655]: smb.service: Start request repeated too quickly.
Sep 15 00:21:48 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 15 00:21:48 steamdeck systemd[1655]: Failed to start User-level SMB Service for Deck.
Sep 15 00:21:55 steamdeck systemd[1655]: smb.service: Start request repeated too quickly.
Sep 15 00:21:55 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 15 00:21:55 steamdeck systemd[1655]: Failed to start User-level SMB Service for Deck.
```

当时在前台运行没有问题，一旦用 systemctl 就报错，查看日志发现：

```shell
journalctl --user -u smb.service -e --no-pager
Sep 16 00:05:27 steamdeck systemd[1655]: Started User-level SMB Service for Deck.
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Main process exited, code=exited, status=1/FAILURE
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 1.
Sep 16 00:05:27 steamdeck systemd[1655]: Started User-level SMB Service for Deck.
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Main process exited, code=exited, status=1/FAILURE
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 2.
Sep 16 00:05:27 steamdeck systemd[1655]: Started User-level SMB Service for Deck.
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Main process exited, code=exited, status=1/FAILURE
Sep 16 00:05:27 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 3.
Sep 16 00:05:28 steamdeck systemd[1655]: Started User-level SMB Service for Deck.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Main process exited, code=exited, status=1/FAILURE
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 4.
Sep 16 00:05:28 steamdeck systemd[1655]: Started User-level SMB Service for Deck.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Main process exited, code=exited, status=1/FAILURE
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Scheduled restart job, restart counter is at 5.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Start request repeated too quickly.
Sep 16 00:05:28 steamdeck systemd[1655]: smb.service: Failed with result 'exit-code'.
Sep 16 00:05:28 steamdeck systemd[1655]: Failed to start User-level SMB Service for Deck.
```

连续重启了 5 次然后报错，怀疑是用户权限目录不足，所以创建用户目录，加上手动指定输出日志目录

```shell
# 把 Samba 的运行/锁/状态/缓存/私有/日志目录放到用户目录,上面配置已体现
pid directory = /home/deck/.local/var/samba/run
lock directory = /home/deck/.local/var/samba/lock
state directory = /home/deck/.local/var/samba/state
cache directory = /home/deck/.local/var/samba/cache
private dir = /home/deck/.local/var/samba/private
log file = /home/deck/.local/var/log/samba/log.%m
log level = 2
server role = standalone server
security = user
```

然后发现好像不是这个的问题，排查可能是 SMBD 绑定端口（445）的问题，赋权：

```shell
# 一次性给 smbd 设置能力（需要 sudo）：
# sudo setcap 'cap_net_bind_service=+ep' /home/linuxbrew/.linuxbrew/sbin/smbd
# Invalid file '/home/linuxbrew/.linuxbrew/sbin/smbd' for capability operation
# 目标不是“普通文件”。Homebrew 前缀下的 smbd 通常是个符号链接，setcap 不会对符号链接生效，必须对真实二进制文件本体设置能力

realbin="$(readlink -f /home/linuxbrew/.linuxbrew/opt/samba/sbin/smbd)"
echo "$realbin"
file "$realbin"            # 确认是 ELF 可执行
sudo setcap 'cap_net_bind_service=+ep' "$realbin"
getcap "$realbin"          # 验证已生效
```

最后发现还是不行，没办法了，直接前台调试看看：

```shell
/home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
# `-i`：前台运行（不 daemonize）
# `-d 3`：日志等级为 3（可调高到 5 甚至 10，越高越详细）
# `-s ...`：指定你的配置文件
```

然后发现了报错

```shell
/home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
smbd version 4.22.4 started.
Copyright Andrew Tridgell and the Samba Team 1992-2025
uid=1000 gid=1000 euid=1000 egid=1000
directory_create_or_exist: mkdir failed on directory /home/deck/.local/var/samba/private/msg.sock: No such file or directory
```

Samba 4.x 需要 private dir 下有 msg.sock 目录用于进程间通信。之前可能只在 systemd 单元里只创建了 /home/deck/.local/var/samba/private，但没有递归创建 msg.sock 子目录。

```shell
mkdir -p /home/deck/.local/var/samba/private/msg.sock
```

再次前台启动：

```shell
/home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
smbd version 4.22.4 started.
Copyright Andrew Tridgell and the Samba Team 1992-2025
uid=1000 gid=1000 euid=1000 egid=1000
invalid permissions on directory '/home/deck/.local/var/samba/private/msg.sock': has 0755 should be 0700
```

发现权限不对，这是 Samba 的**安全检查**，要求 `msg.sock` 目录权限必须是 `0700`（只有所有者可读写执行），而你现在是 `0755`（其他用户也可读/执行），修正权限

```shell
chmod 700 /home/deck/.local/var/samba/private/msg.sock
```

然后再次启动，虽然成功启动了 `waiting for connections`，但似乎仍然有报错：

```shell
/home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
smbd version 4.22.4 started.
Copyright Andrew Tridgell and the Samba Team 1992-2025
uid=1000 gid=1000 euid=1000 egid=1000
Registered MSG_REQ_DMALLOC_MARK and LOG_CHANGED
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
Processing section "[deck]"
adding IPC service
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
loaded services
set_profile_level: INFO: Profiling support unavailable in this build.
daemon 'smbd' : Starting process ...
tdb(/home/deck/.local/var/samba/state/registry.tdb): tdb_open_ex: could not open file /home/deck/.local/var/samba/state/registry.tdb: No such file or directory
Could not open tdb: No such file or directory
Failed to fetch domain sid for WORKGROUP
tdb(/home/deck/.local/var/samba/state/account_policy.tdb): tdb_open_ex: could not open file /home/deck/.local/var/samba/state/account_policy.tdb: No such file or directory
Could not open tdb: No such file or directory
account_policy_get: tdb_fetch_uint32_t failed for type 1 (min password length), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 2 (password history), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 3 (user must logon to change password), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 4 (maximum password age), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 5 (minimum password age), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 6 (lockout duration), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 7 (reset count minutes), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 8 (bad lockout attempt), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 9 (disconnect time), returning 0
account_policy_get: tdb_fetch_uint32_t failed for type 10 (refuse machine password change), returning 0
tdbsam_open: Converting version 0.0 database to version 4.0.
tdbsam_convert_backup: updated /home/deck/.local/var/samba/private/passdb.tdb file.
tdb(/home/deck/.local/var/samba/state/winbindd_idmap.tdb): tdb_open_ex: could not open file /home/deck/.local/var/samba/state/winbindd_idmap.tdb: No such file or directory
TDBSAM converted successfully.
waiting for connections
```

启动之后，我的 Mac 连接服务器 `smb://192.168.31.29` 仍然报错找不到，非常奇怪。排查了端口，服务等等，最终发现是端口的问题，换一个端口就能连上。

```shell
# 1. 检查 smbd 是否监听 445 端口（Mac 只用 445，不用 139）
ss -ltnp | grep 445
netstat -anp | grep 445
# 应该看到 0.0.0.0:445 或 192.168.31.29:445 有 smbd 进程。

LISTEN 0      50           0.0.0.0:445        0.0.0.0:*
LISTEN 0      50              [::]:445           [::]:*

# 2. 检查防火墙（如 firewalld、iptables）是否放行 445 端口：
sudo iptables -L -n | grep 445
sudo ufw status


# 3. smbd 没有绑定 445 端口（权限问题）,确定执行过
sudo setcap 'cap_net_bind_service=+ep' /home/linuxbrew/.linuxbrew/opt/samba/sbin/smbd

# 4. 配置问题，你的配置没问题，[deck] 共享已开放，valid users = deck，Mac 端要用 deck 用户和密码连接，确认你已设置 Samba 密码：
sudo /home/linuxbrew/.linuxbrew/bin/smbpasswd -L -c /home/deck/env/linux/samba/deck.conf -a deck
```

一顿操作下来什么都没成功，然后 Mac 连接的时候还是迅速报错：

```shell
smbutil view //deck@192.168.31.29/deck
smbutil: server connection failed: Operation timed out
```

观察 Deck 的前台命令行，无任何连接输出

```shell
~/env > /home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
smbd version 4.22.4 started.
Copyright Andrew Tridgell and the Samba Team 1992-2025
uid=1000 gid=1000 euid=1000 egid=1000
Registered MSG_REQ_DMALLOC_MARK and LOG_CHANGED
lp_load_ex: refreshing parameters
Initialising global parameters
Processing section "[global]"
Processing section "[deck]"
adding IPC service
added interface wlan0 ip=192.168.31.29 bcast=192.168.31.255 netmask=255.255.255.0
loaded services
set_profile_level: INFO: Profiling support unavailable in this build.
daemon 'smbd' : Starting process ...
Failed to fetch domain sid for WORKGROUP
waiting for connections
```

表现是可以 Ping 通 Steam Deck ，但是 NC 连不上

```shell
~ > ping 192.168.31.29                                          
PING 192.168.31.29 (192.168.31.29): 56 data bytes
64 bytes from 192.168.31.29: icmp_seq=0 ttl=64 time=11.890 ms
64 bytes from 192.168.31.29: icmp_seq=1 ttl=64 time=4.102 ms
q64 bytes from 192.168.31.29: icmp_seq=2 ttl=64 time=39.757 ms
64 bytes from 192.168.31.29: icmp_seq=3 ttl=64 time=4.115 ms
^C
--- 192.168.31.29 ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.102/14.966/39.757/14.661 ms

~ > nc -vz 192.168.31.29 445                                           
nc: connectx to 192.168.31.29 port 445 (tcp) failed: Connection refused
```

说明网络互通，Mac 能到达 Deck。而 Deck 上 445 端口虽然 smbd 启动时监听，但实际上**没有真正开放**，或者监听的 smbd 进程已退出/崩溃，或者被别的服务占用后立刻关闭。

怀疑是谁占了 445 端口，查了一下

```shell
~/env > ps aux | grep smbd
deck       81179  0.0  0.1  84572 26232 pts/5    S+   20:53   0:00 /home/linuxbrew/.linuxbrew/sbin/smbd -i -d 3 -s /home/deck/env/linux/samba/deck.conf
deck       82238  0.0  0.0   6596  4472 pts/7    S+   20:59   0:00 grep --color=auto smbd

~/env > ss -ltnp | grep 445
LISTEN 0      50           0.0.0.0:445        0.0.0.0:*
LISTEN 0      50              [::]:445           [::]:*                                              
~/env > sudo lsof -i :445
COMMAND   PID USER FD   TYPE  DEVICE SIZE/OFF NODE NAME
smbd    81179 deck 30u  IPv6 4205857      0t0  TCP *:microsoft-ds (LISTEN)
smbd    81179 deck 32u  IPv4 4205859      0t0  TCP *:microsoft-ds (LISTEN)
```

发现谁都没占 445。实在没招了，问了下 chatGPT

> 这种情况**99% 是 Linux 内核拒绝了 445 端口的非 root 绑定**，即使你看到 `ss -ltnp` 显示监听，实际上内核会直接拒绝外部连接。
> - **普通用户运行的 smbd，虽然 setcap 后能监听 445，但部分 Linux 发行版（包括 SteamOS/Arch 衍生）默认限制非 root 进程监听 445/139，或 setcap 没有生效。**
> - 这会导致：本地能看到监听，**但所有外部连接都被内核直接拒绝**，smbd 根本收不到连接，表现为“Connection refused”。

没招了，之前的步骤全部用 ROOT 操作一遍，然后启动这个服务，我发现仍然无法连接。具体的命令就不罗列了，太折腾了，最后试了一下 1445 端口，成功了。

简直了。

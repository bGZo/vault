---
aliases:
  - How to manage app in debian
  - Manage-app-in-debian
created: 2025-07-16T20:45:43
modified: 2025-07-16T20:46:16
title: How to manage app in debian
---

# How to manage app in [[debian]]

> Ubuntu 和 Debian 通吃是因为 Debian 系的 APT 包管理器。

## \#1 Install

From mirror source:

```shell
sudo apt install -y xxx
```

From `deb` package:

```shell
sudo dpkg -i xxx.deb
```

Use another tool after run `sudo apt install gdebi`

```shell
sudo gdebi xxx.deb
```

From source code (after `tar zxf xxx.tgz`):

> 有些软件没有被收录进软件镜像源，或者说开发者需要去使用他们最新的版本，这时候就要自己去他们的官网或者是代码托管平台下载最新的 Linux 源码，自己来 build. 这种方式安装需要解决很多的依赖，安装前多 Google

```shell
sudo make
sudo make install
```

You could install `build-essential` before )

If need to install dependency with prompt:

```shell
sudo apt install -f xxx
```

Or run the script supported by application : )

[通过apt离线下载deb包以及其依赖包_OS与驱动_鲲鹏_华为云论坛 (huaweicloud.com)](https://bbs.huaweicloud.com/forum/thread-62703-1-1.html)

[我如何去忽略某些依赖关系？ (qastack.cn)](https://qastack.cn/server/250224/how-do-i-get-apt-get-to-ignore-some-dependencies)

## \#2 Reinstall

```shell
sudo apt reinstall xxx
```

```shell
sudo apt reinstall -d xxx
```

## \#3 Uninstall

```shell
sudo apt purge xxx
```

```shell
dpkg --get-selections | grep XXX
```

```shell
sudo apt purge XXX  #一个带core的package, 如果没有带core的package, 则是情况而定.
```

## \#4 Clean old version software

Most easy way is following, which only work for have updated recently packages:

```shell
sudo apt autoclean
sudo apt autoremove
```

For log:

```shell
sudo echo > /var/log/syslog
sudo echo > /var/log/kern.log
```

For SNAP

```shell
#!/bin/shell
# Removes old revisions of snaps
# CLOSE ALL SNAPS BEFORE RUNNING THIS
set -eu
snap list --all | awk '/disabled/{print $1, $3}' |
while read snapname revision; do
    snap remove "$snapname" --revision="$revision"
done
```

A more hacker way is:

```shell
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
```

> [!tip]
> 这条命令是用于清理 Debian 或 Ubuntu 系统中残留的已经被标记为 "rc"（已删除但配置文件仍然存在）状态的软件包。让我逐步解释这个命令的各个部分：
#chatGPT

`dpkg -l`：这部分命令列出系统中安装的所有软件包。

`|`：这是管道符号，用于将第一个命令的输出传递给下一个命令。

`grep ^rc`：这部分命令使用 `grep` 工具来过滤出以 "rc" 开头的行，这些行代表了已删除但配置文件仍然存在的软件包。

`awk '{print $2}'`：这部分命令使用 `awk` 工具提取每一行中的第二列，也就是软件包的名称。

`|`：再次使用管道符号，将 `awk` 命令的输出传递给下一个命令。

`sudo xargs dpkg -P`：最后，这部分命令使用 `xargs` 来将软件包名称传递给 `dpkg -P` 命令，以卸载这些软件包。`dpkg -P` 命令会删除已标记为 "rc" 状态的软件包及其配置文件。

> [!Warning]
> 使用 `dpkg -P` 命令可能会导致数据丢失，因此在运行此命令之前应谨慎考虑，并确保您了解正在删除的软件包及其影响。

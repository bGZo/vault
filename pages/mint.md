---
created: 2025-01-12T02:16:35
modified: 2025-03-30T17:27:29
tags-link:
  - "[[debian]]"
---

## [[minisforum-um880pro|minisforum880pro]]

```shell
~ > cat /proc/version
Linux version 6.8.0-38-generic (buildd@lcy02-amd64-049) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.2.0-23ubuntu4) 13.2.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #38-Ubuntu SMP PREEMPT_DYNAMIC Fri Jun  7 15:25:01 UTC 2024
~ > uname -a
Linux bgzo-EliteMini-Series 6.8.0-38-generic #38-Ubuntu SMP PREEMPT_DYNAMIC Fri Jun  7 15:25:01 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

Okey, this is kind of the third time I choose to use linux,[^the_third_time] and this time, I would choose Mint 22 on mini pc. So what's the difference?

The former ubuntu is install on the laptop, which means that you could meet those problems:

1. connect wifi and `archinstall` from cli.
2. screen lighting change.
3. bluetooth connection & high quality voice.
4. touch pad gestures.
5. gpu drives.
6. non-english languages supported [^chinese_shown]
7. gaming `wine` error.
8. shortcut setting.
9. battery management.
10. without main client & support with commercial companies.

After solving above problems, you would feel **LINUX IS SO GOOD**. Fortunately, in mini pc, this kind of problems would be more tolerable. So I still not recommend using linux on your laptop, if you have nothing to do, or if you are students having a lot of time. That would give you a good experience.

## Installation

> [!NOTE]
Replace software source installed when installing.
Those applications might be used, so recommended install it.

```bash
$ sudo apt install vim
```

## dotfiles

https://github.com/bgzo/dotfiles

## replace: apt source mirror [help_mirror]

default source file is located in `/etc/apt/sources.list.d/official-package-repositories.list`, you could put ubuntu mirror and mint mirror on it.

The sources.list on Mint 22 would be like following:

```shell
deb https://mirrors.tuna.tsinghua.edu.cn/linuxmint/ wilma main upstream import backport
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse

# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换
deb http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse
```

## SSH support

```bash
$ sudo apt install openssh-server
$ sudo systemctl status ssh         # Then service should be running
$ sudo vim /etc/ssh/sshd_config
```

mainly keep those configs be activated

```bash
Port 22
PasswordAuthentication yes
ListenAddress 0.0.0.0
```

then restart service:

```bash
$ sudo systemctl restart ssh
```

it should be okey

```bash
$ ssh user@192.168.31.20
```

## Proxy

via [[proxy]]

[^the_third_time]: the first time is using ubuntu 20 in 2020. The second time is using archlinux in 2023.
[^chinese_shown]: chinese charset shown on system and cli & fctix input.
[help_mirror]: https://mirrors.tuna.tsinghua.edu.cn/help/linuxmint/, https://mirrors.ustc.edu.cn/help/linuxmint.html will error with

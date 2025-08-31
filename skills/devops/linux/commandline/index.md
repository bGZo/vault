---
aliases:
  - 命令行
  - cli
  - Commandline
  - Linux command-line
comments: false
created: 2024-07-28T00:00:00
modified: 2025-08-30T18:22:56
title: Linux command-line
type: tool
---

# Linux command-line

> [!NOTE]
>
> It's evergreen(常青) knowledge that will not be out of date any time soon.
>
> — [The Linux Command Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/) | [zh-has](https://chinese.freecodecamp.org/news/the-linux-commands-handbook/)

## 默认颜色

| color    | decribe                                                 |
| -------- | ------------------------------------------------------- |
| **白色**   | 普通文件                                                    |
| **蓝色**   | 目录                                                      |
| **绿色**   | 可执行文件                                                   |
| **红色**   | 压缩文件                                                    |
| **浅蓝色**  | 链接文件                                                    |
| **红色闪烁** | 链接的文件有问题                                                |
| **黄色**   | 设备文件                                                    |
| **灰色**   | 其他文件                                                    |
| **绿色**   | 是有问题的，代表权限中有其它组权限拥有写入权限，系统默认这是一个高风险目录。将权限改到 775 以下就可以解决 |

## Angle brackets

`>` -> 输出重定向

`>>` -> 追加

## [[skills/devops/linux/index|Linux]] Category

Refer to https://www.runoob.com/linux/linux-command-manual.html

### 文件管理

#### Cat

#### Chattr

#### Chgrp

#### Chmod

#### Chown

#### Cksum

#### Cmp

#### Diff

#### Diffstat

#### File

#### Find

#### Git

#### Gitview

#### Indent

#### Cut

#### Ln

#### Less

#### Locate

#### Lsattr

#### Mattrib

#### Mc

#### Mdel

#### Mdir

#### Mktemp

#### More

#### Mmove

#### Mread

#### Mren

#### Mtools

#### Mtoolstest

#### Mv

#### Od

#### Paste

#### Patch

#### Rcp

#### Rm

#### Slocate

#### Split

#### Tee

#### Tmpwatch

#### Touch

#### Umask

#### Which

#### Cp

#### Whereis

#### Mcopy

#### Mshowfat

#### Rhmask

#### Scp

#### Awk

#### Read

#### Updatedb

### 文档编辑

#### Col

#### Colrm

#### Comm

#### Csplit

#### Ed

#### Egrep

#### Ex

#### Fgrep

#### Fmt

#### Fold

#### Grep

#### Ispell

#### Jed

#### Joe

#### Join

#### Look

#### Mtype

#### Pico

#### Rgrep

#### Sed

#### Sort

#### Spell

#### Tr

#### Expr

#### Uniq

#### Wc

#### Let

### 文件传输

#### Lprm

#### Lpr

#### Lpq

#### Lpd

#### Bye

#### Ftp

#### Uuto

#### Uupick

#### Uucp

#### Uucico

#### Tftp

#### Ncftp

#### Ftpshut

#### Ftpwho

#### Ftpcount

### 磁盘管理

#### Cd

#### Df

- 获取磁盘的使用情况信息
- `-h` 会将值以更为可读的方式显示

#### Dirs

#### Du

```shell
du
# 单独计算每个文件的大小
du -m
du -g
# 以兆字节（MB）或千兆字节（GB）为单位显示文件大小
du -h
# 显示更为可读的，适应大小的数值
du -a
# 输出文件夹中每一个文件的大小
```

按大小对目录进行排序, 获取前 10 个结果

```shell
du -h <directory> | sort -nr | head
```

#### Edquota

#### Eject

#### Mcd

#### Mdeltree

#### Mdu

#### Mkdir

#### Mlabel

#### Mmd

#### Mrd

#### Mzip

#### Pwd (print work directory)

- 打印当前目录 显示出当前工作目录的绝对路径

#### Quota

#### Mount

#### Mmount

#### Rmdir

#### Rmt

#### Stat

#### Tree

#### Umount

#### Ls

#### Quotacheck

#### Quotaoff

#### Lndir

#### Repquota

#### Quotaon

### 磁盘维护

#### Badblocks

#### Cfdisk

#### Dd

#### e2fsck

#### ext2ed

#### Fsck

#### fsck.minix

#### Fsconf

#### Fdformat

#### Hdparm

#### Mformat

#### Mkbootdisk

#### Mkdosfs

#### mke2fs

#### mkfs.ext2

#### mkfs.msdos

#### Mkinitrd

#### Mkisofs

#### Mkswap

#### Mpartition

#### Swapon

#### Symlinks

#### Sync

#### Mbadblocks

#### mkfs.minix

#### fsck.ext2

#### Fdisk

#### Losetup

#### Mkfs

#### Sfdisk

#### Swapoff

### 网络通讯

#### Apachectl

#### Arpwatch

#### Dip

#### Getty

#### Mingetty

#### Uux

#### Telnet

#### Uulog

#### Uustat

#### Ppp-off

#### Netconfig

#### [[nc]]

#### Httpd

#### Ifconfig

#### Minicom

#### Mesg

#### Dnsconf

#### Wall

#### Netstat

#### Ping

#### Pppstats

#### Samba

#### Setserial

#### Talk

#### Traceroute

#### Tty

#### Newaliases

#### Uuname

#### Netconf

#### Write

#### Statserial

#### Efax

#### Pppsetup

#### Tcpdump

#### Ytalk

#### Cu

#### Smbd

#### Testparm

#### Smbclient

#### Shapecfg

### 系统管理

#### Adduser

#### Chfn

#### Useradd

#### Date

#### Exit

#### Finger

#### Fwhios

#### Sleep

#### Suspend

#### Groupdel

#### Groupmod

#### Halt

#### Kill

#### Last

#### Lastb

#### Login

#### Logname

#### Logout

#### Ps (Process Status)

- 进程状态，类似于 windows 的任务管理器

#### Nice

#### Procinfo

#### Top

#### Pstree

#### Reboot

#### Rlogin

#### Rsh

#### Sliplogin

#### Screen

#### Shutdown

#### Rwho

#### Sudo

#### Gitps

#### Swatch

#### Tload

#### Logrotate

#### Uname

#### Chsh

#### Userconf

#### Userdel

#### Usermod

#### Vlock

#### Who

#### Whoami

#### Whois

#### Newgrp

#### Renice

#### Su

#### Skill

#### W

#### Id

#### Groupadd

#### Free

### 系统设置

#### Reset

#### Clear

#### Alias

#### Dircolors

#### Aumix

#### Bind

#### Chroot

#### Clock

#### Crontab

#### Declare

#### Depmod

#### Dmesg

#### Enable

#### Eval

#### Export

#### Pwunconv

#### Grpconv

#### Rpm

#### Insmod

#### Kbdconfig

#### Lilo

#### Liloconfig

#### Lsmod

#### Minfo

#### Set

#### Modprobe

#### Ntsysv

#### Mouseconfig

#### Passwd

#### Pwconv

#### Rdate

#### Resize

#### Rmmod

#### Grpunconv

#### Modinfo

#### Time

#### Setup

#### Sndconfig

#### Setenv

#### Setconsole

#### Timeconfig

#### Ulimit

#### Unset

#### Chkconfig

#### Apmd

#### Hwclock

#### Mkkickstart

#### Fbset

#### Unalias

#### SVGATextMode

#### Gpasswd

### 备份压缩

#### Ar

#### Bunzip2

#### Bzip2

#### bzip2recover

#### Gunzip

#### Unarj

#### Compress

#### Cpio

#### Dump

#### Uuencode

#### Gzexe

#### Gzip

#### Lha

#### Restore

#### Tar

#### Uudecode

#### Unzip

#### Zip

#### Zipinfo

### 设备管理

#### Setleds

#### Loadkeys

#### Rdev

#### Dumpkeys

#### MAKEDEV

#### Poweroff

### 其他

#### Bc

#### Tail

#### Head

#### Xargs

#### Ip

#### Nohup

#### Killall

#### Pkill

## Linux 常用命令全拼

Refer to: https://www.runoob.com/w3cnote/linux-command-full-fight.html

### Df

disk free 其功能是显示磁盘可用空间数目信息及空间结点信息。换句话说，就是报告在任何安装的设备或目录中，还剩多少自由的空间。

### Du

Disk usage

### Rpm

即 RedHat Package Management，是 RedHat 的发明之一

### Rmdir

Remove Directory（删除目录）

### Rm

Remove（删除目录或文件）

### Cat

concatenate 连锁

- cat file1file2>>file3 把文件 1 和文件 2 的内容联合起来放到 file3 中

### Insmod

install module,载入模块

- ln -s : link -soft 创建一个软链接，相当于创建一个快捷方式

### Mkdir

Make Directory(创建目录)

### Touch

touch

### Man

Manual

### Su

Swith user(切换用户)

### Cd

Change directory

### Ls

List files

### Mkdir

Make directory

### Rmdir

Remove directory

### Mkfs

Make file system

### Fsck

File system check

### Uname

Unix name

### Lsmod

List modules

### Mv

Move file

### Rm

Remove file

### Cp

Copy file

### Ln

Link files

### Fg

Foreground

### Bg

Background

### Chown

Change owner

### Chgrp

Change group

### Chmod

Change mode

### Umount

Unmount

### Dd

本来应根据其功能描述 "Convert an copy" 命名为 "cc"，但 "cc" 已经被用以代表 "CComplier"，所以命名为 "dd"

### Tar

Tape archive （磁带档案）

### Ldd

List dynamic dependencies

### Insmod

Install module

### Rmmod

Remove module

### Lsmod

List module

- 文件结尾的 "rc"（如.bashrc、.xinitrc 等）：Resource configuration
- Knnxxx /Snnxxx（位于 rcx.d 目录下）：K（Kill）；S(Service)；nn（执行顺序号）；xxx（服务标识）
- .a（扩展名 a）：Archive，static library
- .so（扩展名 so）：Shared object，dynamically linked library
- .o（扩展名 o）：Object file，complied result of C/C++ source file

### RPM

Red hat package manager

### Dpkg

Debian package manager

### Apt

Advanced package tool（Debian 或基于 Debian 的发行版中提供）

### Bin

Binaries (二进制文件)

### /dev

Devices (设备)

### /etc

Etcetera (等等)

### /lib

LIBrary

### /proc

Processes

### /sbin

Superuser Binaries (超级用户的二进制文件)

### /tmp

Temporary (临时)

### /usr

Unix Shared Resources

### /var

Variable (变量)

### FIFO

First In, First Out

### GRUB

GRand Unified Bootloader

- IFS= Internal Field Seperators

### LILO

LInux LOader

### MySQL

My 是最初作者女儿的名字，

### SQL

Structured QueryLanguage

### PHP

Personal Home Page Tools = PHP HypertextPreprocessor

### PS

Prompt String

### Perl

“Pratical Extraction and Report Language”(实际的抽取和报告语言) =”Pathologically Eclectic Rubbish Lister”

- Python 得名于电视剧 Monty Python’s Flying Circus

### Tcl

Tool Command Language

### Tk

ToolKit

### VT

Video Terminal

### YaST

Yet Another Setup Tool

### Apache

“a patchy” server

### Apt

Advanced Packaging Tool

### Ar

archiver

### As

assembler

### Awk

“Aho Weiberger and Kernighan”三个作者的姓的第一个字母

### Bash

Bourne Again SHell

### Bc

Basic (Better) Calculator

### Bg

BackGround

### Biff

作者 HeidiStettner 在 U.C.Berkely 养的一条狗,喜欢对邮递员汪汪叫。

### Cal

Calendar (日历)

### Cat

Catenate (链接)

### Cd

Change Directory

### Chgrp

Change Group

### Chmod

Change Mode

### Chown

Change Owner

### Chsh

Change Shell

### Cmp

compare

### Cobra

Common Object Request BrokerArchitecture

### Comm

common

### Cp

Copy

### Cpio

CoPy In and Out

### Cpp

C Pre Processor

### Cron

Chronos 希腊文时间

### Cups

Common Unix Printing System

### Cvs

Current Version System

### Daemon

Disk And Execution MONitor

### Dc

Desk Calculator

### Dd

Disk Dump (磁盘转储)

### Df

Disk Free

### Diff

Difference

### Dmesg

diagnostic message

### Du

Disk Usage

### Ed

editor

### Egrep

Extended GREP

### Elf

Extensible Linking Format

### Elm

ELectronic Mail

### Emacs

Editor MACroS

### Eval

EVALuate

### Ex

EXtended

### Exec

EXECute (执行)

### Fd

file descriptors

### Fg

ForeGround

### Fgrep

Fixed GREP

### Fmt

format

### Fsck

File System ChecK

### Fstab

FileSystem TABle

### Fvwm

F*** Virtual Window Manager

### Gawk

GNU AWK

### Gpg

GNU Privacy Guard

### Groff

GNU troff

### Hal

Hardware Abstraction Layer

### Joe

Joe’s Own Editor

### Ksh

Korn SHell

### Lame

Lame Ain’t an MP3 Encoder

### Lex

LEXical analyser

### Lisp

LISt Processing = Lots of IrritatingSuperfluous Parentheses

### Ln

Link

### Lpr

Line PRint

### Ls

list

### Lsof

LiSt Open Files

### M4

Macro processor Version 4

### Man

MANual pages

### Mawk

Mike Brennan’s AWK

### Mc

Midnight Commander

### Mkfs

MaKe FileSystem

### Mknod

Make Node

### Motd

Message of The Day

### Mozilla

MOsaic GodZILLa

### Mtab

Mount TABle

### Mv

Move

### Nano

Nano’s ANOther editor

### Nawk

New AWK

### Nl

Number of Lines

### Nm

names

### Nohup

No HangUP

### Nroff

New ROFF

### Od

Octal Dump

### Passwd

Passwd

### Pg

pager

### Pico

PIne’s message COmposition editor

### Pine

“Program for Internet News &Email” = “Pine is not Elm”

### Ping

拟声 又 = Packet Internet Grouper

### Pirntcap

PRINTer CAPability

### Popd

POP Directory

### Pr

pre

### Printf

Print Formatted

### Pty

pseudo tty

### Pushd

PUSH Directory

### Rc

runcom = run command, rc 还是 plan9 的 shell

### Rev

REVerse

### Rm

ReMove

### Rn

Read News

### Roff

RunOFF

### Rpm

RPM Package Manager = RedHat PackageManager

- rsh, rlogin, rvim 中的

### R

Remote

### Rxvt

ouR XVT

### Seamoneky

我

### Sed

Stream Editor

### Seq

SEQuence

### Shar

Shell ARchive

### Slrn

S-Lang rn

### Ssh

Secure Shell

### Ssl

Secure Sockets Layer

### Stty

Set TTY

### Su

Substitute User

### Svn

SubVersion

### Tar

Tape ARchive

### Tcsh

TENEX C shell

### Tee

T (T 形水管接口)

### Telnet

TEminaL over Network

### Termcap

terminal capability

### Terminfo

terminal information

### Tex

τέχνη的缩写，希腊文 art

### Tr

traslate

### Troff

Typesetter new ROFF

### Tsort

Topological SORT

### Tty

TeleTypewriter

### Twm

Tom’s Window Manager

### Tz

TimeZone

### Udev

Userspace DEV

### Ulimit

User’s LIMIT

### Umask

User’s MASK

### Uniq

UNIQue

### I

VIsual = Very Inconvenient

### Vim

Vi IMproved

### Wall

write all

### Wc

Word Count

### Wine

WINE Is Not an Emulator

### Xargs

eXtended ARGuments

### Xdm

X Display Manager

### Xlfd

X Logical Font Description

### Xmms

X Multimedia System

### Xrdb

X Resources DataBase

### Xwd

X Window Dump

### Yacc

yet another compiler compiler

### Fish

the Friendly Interactive SHell

### Su

Switch User

### MIME

Multipurpose Internet Mail Extensions

### ECMA

European Computer ManufacturersAssociation

## 中文计划

[man-pages-zh/manpages-zh: Chinese Manual Pages](https://github.com/man-pages-zh/manpages-zh) 中文计划

```bash
sudo apt install manpages-zh
man -M /usr/share/man/zh_CN (xxx)
```

## References

- [The Linux Commands Handbook (bjpcjp.github.io)](https://bjpcjp.github.io/pdfs/devops/linux-commands-handbook.pdf)
    - `dirname` <-> `basename`
- [linux命令在线中文手册](http://linux.51yip.com/)
- [Linux 命令搜索引擎](https://wangchujiang.com/linux-command/) | [jaywcjlove/linux-command](https://github.com/jaywcjlove/linux-command)
- [Linux man pages online (man7.org)](https://man7.org/linux/man-pages/index.html)
- > 在您的系统设置为中文环境时， 如果有对应的中文手册页，则该手册页将显示中文版本。如系统并非中文环境，请临时调整您的环境变量以使用中文内容

# 命令行

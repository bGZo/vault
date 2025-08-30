---
created: 2024-08-14T12:00:00
modified: 2025-04-04T10:37:08
comments: false
title: Command line
---

> [!NOTE]
>
> It's evergreen(常青) knowledge that will not be out of date any time soon.
>
> — [The Linux Command Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/) | [zh-has](https://chinese.freecodecamp.org/news/the-linux-commands-handbook/)

## [[skills/devops/linux/index|Linux]] Category

Refer to https://www.runoob.com/linux/linux-command-manual.html

### 文件管理
#### cat
#### chattr
#### chgrp
#### chmod
#### chown
#### cksum
#### cmp
#### diff
#### diffstat
#### file
#### find
#### git
#### gitview
#### indent
#### cut
#### ln
#### less
#### locate
#### lsattr
#### mattrib
#### mc
#### mdel
#### mdir
#### mktemp
#### more
#### mmove
#### mread
#### mren
#### mtools
#### mtoolstest
#### mv
#### od
#### paste
#### patch
#### rcp
#### rm
#### slocate
#### split
#### tee
#### tmpwatch
#### touch
#### umask
#### which
#### cp
#### whereis
#### mcopy
#### mshowfat
#### rhmask
#### scp
#### awk
#### read
#### updatedb
### 文档编辑
#### col
#### colrm
#### comm
#### csplit
#### ed
#### egrep
#### ex
#### fgrep
#### fmt
#### fold
#### grep
#### ispell
#### jed
#### joe
#### join
#### look
#### mtype
#### pico
#### rgrep
#### sed
#### sort
#### spell
#### tr
#### expr
#### uniq
#### wc
#### let
### 文件传输
#### lprm
#### lpr
#### lpq
#### lpd
#### bye
#### ftp
#### uuto
#### uupick
#### uucp
#### uucico
#### tftp
#### ncftp
#### ftpshut
#### ftpwho
#### ftpcount
### 磁盘管理
#### cd
#### df
- 获取磁盘的使用情况信息
- `-h` 会将值以更为可读的方式显示

#### dirs
#### du

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

#### edquota
#### eject
#### mcd
#### mdeltree
#### mdu
#### mkdir
#### mlabel
#### mmd
#### mrd
#### mzip
#### pwd (print work directory)

- 打印当前目录 显示出当前工作目录的绝对路径

#### quota
#### mount
#### mmount
#### rmdir
#### rmt
#### stat
#### tree
#### umount
#### ls
#### quotacheck
#### quotaoff
#### lndir
#### repquota
#### quotaon
### 磁盘维护
#### badblocks
#### cfdisk
#### dd
#### e2fsck
#### ext2ed
#### fsck
#### fsck.minix
#### fsconf
#### fdformat
#### hdparm
#### mformat
#### mkbootdisk
#### mkdosfs
#### mke2fs
#### mkfs.ext2
#### mkfs.msdos
#### mkinitrd
#### mkisofs
#### mkswap
#### mpartition
#### swapon
#### symlinks
#### sync
#### mbadblocks
#### mkfs.minix
#### fsck.ext2
#### fdisk
#### losetup
#### mkfs
#### sfdisk
#### swapoff
### 网络通讯
#### apachectl
#### arpwatch
#### dip
#### getty
#### mingetty
#### uux
#### telnet
#### uulog
#### uustat
#### ppp-off
#### netconfig
#### [[nc]]
#### httpd
#### ifconfig
#### minicom
#### mesg
#### dnsconf
#### wall
#### netstat
#### ping
#### pppstats
#### samba
#### setserial
#### talk
#### traceroute
#### tty
#### newaliases
#### uuname
#### netconf
#### write
#### statserial
#### efax
#### pppsetup
#### tcpdump
#### ytalk
#### cu
#### smbd
#### testparm
#### smbclient
#### shapecfg
### 系统管理
#### adduser
#### chfn
#### useradd
#### date
#### exit
#### finger
#### fwhios
#### sleep
#### suspend
#### groupdel
#### groupmod
#### halt
#### kill
#### last
#### lastb
#### login
#### logname
#### logout
#### ps (Process Status)

- 进程状态，类似于 windows 的任务管理器

#### nice
#### procinfo
#### top
#### pstree
#### reboot
#### rlogin
#### rsh
#### sliplogin
#### screen
#### shutdown
#### rwho
#### sudo
#### gitps
#### swatch
#### tload
#### logrotate
#### uname
#### chsh
#### userconf
#### userdel
#### usermod
#### vlock
#### who
#### whoami
#### whois
#### newgrp
#### renice
#### su
#### skill
#### w
#### id
#### groupadd
#### free
### 系统设置
#### reset
#### clear
#### alias
#### dircolors
#### aumix
#### bind
#### chroot
#### clock
#### crontab
#### declare
#### depmod
#### dmesg
#### enable
#### eval
#### export
#### pwunconv
#### grpconv
#### rpm
#### insmod
#### kbdconfig
#### lilo
#### liloconfig
#### lsmod
#### minfo
#### set
#### modprobe
#### ntsysv
#### mouseconfig
#### passwd
#### pwconv
#### rdate
#### resize
#### rmmod
#### grpunconv
#### modinfo
#### time
#### setup
#### sndconfig
#### setenv
#### setconsole
#### timeconfig
#### ulimit
#### unset
#### chkconfig
#### apmd
#### hwclock
#### mkkickstart
#### fbset
#### unalias
#### SVGATextMode
#### gpasswd
### 备份压缩
#### ar
#### bunzip2
#### bzip2
#### bzip2recover
#### gunzip
#### unarj
#### compress
#### cpio
#### dump
#### uuencode
#### gzexe
#### gzip
#### lha
#### restore
#### tar
#### uudecode
#### unzip
#### zip
#### zipinfo
### 设备管理
#### setleds
#### loadkeys
#### rdev
#### dumpkeys
#### MAKEDEV
#### poweroff
### 其他
#### bc
#### tail
#### head
#### xargs
#### ip
#### nohup
#### killall
#### pkill

## Linux 常用命令全拼

Refer to: https://www.runoob.com/w3cnote/linux-command-full-fight.html

### df

disk free 其功能是显示磁盘可用空间数目信息及空间结点信息。换句话说，就是报告在任何安装的设备或目录中，还剩多少自由的空间。

### du

Disk usage

### rpm

即 RedHat Package Management，是 RedHat 的发明之一

### rmdir

Remove Directory（删除目录）

### rm

Remove（删除目录或文件）

### cat

concatenate 连锁

- cat file1file2>>file3 把文件 1 和文件 2 的内容联合起来放到 file3 中

### insmod

install module,载入模块

- ln -s : link -soft 创建一个软链接，相当于创建一个快捷方式

### mkdir

Make Directory(创建目录)

### touch

touch

### man

Manual

### su

Swith user(切换用户)

### cd

Change directory

### ls

List files

### mkdir

Make directory

### rmdir

Remove directory

### mkfs

Make file system

### fsck

File system check

### uname

Unix name

### lsmod

List modules

### mv

Move file

### rm

Remove file

### cp

Copy file

### ln

Link files

### fg

Foreground

### bg

Background

### chown

Change owner

### chgrp

Change group

### chmod

Change mode

### umount

Unmount

### dd

本来应根据其功能描述 "Convert an copy" 命名为 "cc"，但 "cc" 已经被用以代表 "CComplier"，所以命名为 "dd"

### tar

Tape archive （磁带档案）

### ldd

List dynamic dependencies

### insmod

Install module

### rmmod

Remove module

### lsmod

List module

- 文件结尾的 "rc"（如.bashrc、.xinitrc 等）：Resource configuration
- Knnxxx /Snnxxx（位于 rcx.d 目录下）：K（Kill）；S(Service)；nn（执行顺序号）；xxx（服务标识）
- .a（扩展名 a）：Archive，static library
- .so（扩展名 so）：Shared object，dynamically linked library
- .o（扩展名 o）：Object file，complied result of C/C++ source file

### RPM

Red hat package manager

### dpkg

Debian package manager

### apt

Advanced package tool（Debian 或基于 Debian 的发行版中提供）

### bin

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

### apache

“a patchy” server

### apt

Advanced Packaging Tool

### ar

archiver

### as

assembler

### awk

“Aho Weiberger and Kernighan”三个作者的姓的第一个字母

### bash

Bourne Again SHell

### bc

Basic (Better) Calculator

### bg

BackGround

### biff

作者 HeidiStettner 在 U.C.Berkely 养的一条狗,喜欢对邮递员汪汪叫。

### cal

Calendar (日历)

### cat

Catenate (链接)

### cd

Change Directory

### chgrp

Change Group

### chmod

Change Mode

### chown

Change Owner

### chsh

Change Shell

### cmp

compare

### cobra

Common Object Request BrokerArchitecture

### comm

common

### cp

Copy

### cpio

CoPy In and Out

### cpp

C Pre Processor

### cron

Chronos 希腊文时间

### cups

Common Unix Printing System

### cvs

Current Version System

### daemon

Disk And Execution MONitor

### dc

Desk Calculator

### dd

Disk Dump (磁盘转储)

### df

Disk Free

### diff

Difference

### dmesg

diagnostic message

### du

Disk Usage

### ed

editor

### egrep

Extended GREP

### elf

Extensible Linking Format

### elm

ELectronic Mail

### emacs

Editor MACroS

### eval

EVALuate

### ex

EXtended

### exec

EXECute (执行)

### fd

file descriptors

### fg

ForeGround

### fgrep

Fixed GREP

### fmt

format

### fsck

File System ChecK

### fstab

FileSystem TABle

### fvwm

F*** Virtual Window Manager

### gawk

GNU AWK

### gpg

GNU Privacy Guard

### groff

GNU troff

### hal

Hardware Abstraction Layer

### joe

Joe’s Own Editor

### ksh

Korn SHell

### lame

Lame Ain’t an MP3 Encoder

### lex

LEXical analyser

### lisp

LISt Processing = Lots of IrritatingSuperfluous Parentheses

### ln

Link

### lpr

Line PRint

### ls

list

### lsof

LiSt Open Files

### m4

Macro processor Version 4

### man

MANual pages

### mawk

Mike Brennan’s AWK

### mc

Midnight Commander

### mkfs

MaKe FileSystem

### mknod

Make Node

### motd

Message of The Day

### mozilla

MOsaic GodZILLa

### mtab

Mount TABle

### mv

Move

### nano

Nano’s ANOther editor

### nawk

New AWK

### nl

Number of Lines

### nm

names

### nohup

No HangUP

### nroff

New ROFF

### od

Octal Dump

### passwd

Passwd

### pg

pager

### pico

PIne’s message COmposition editor

### pine

“Program for Internet News &Email” = “Pine is not Elm”

### ping

拟声 又 = Packet Internet Grouper

### pirntcap

PRINTer CAPability

### popd

POP Directory

### pr

pre

### printf

Print Formatted

### pty

pseudo tty

### pushd

PUSH Directory

### rc

runcom = run command, rc 还是 plan9 的 shell

### rev

REVerse

### rm

ReMove

### rn

Read News

### roff

RunOFF

### rpm

RPM Package Manager = RedHat PackageManager

- rsh, rlogin, rvim 中的

### r

Remote

### rxvt

ouR XVT

### seamoneky

我

### sed

Stream Editor

### seq

SEQuence

### shar

Shell ARchive

### slrn

S-Lang rn

### ssh

Secure Shell

### ssl

Secure Sockets Layer

### stty

Set TTY

### su

Substitute User

### svn

SubVersion

### tar

Tape ARchive

### tcsh

TENEX C shell

### tee

T (T 形水管接口)

### telnet

TEminaL over Network

### termcap

terminal capability

### terminfo

terminal information

### tex

τέχνη的缩写，希腊文 art

### tr

traslate

### troff

Typesetter new ROFF

### tsort

Topological SORT

### tty

TeleTypewriter

### twm

Tom’s Window Manager

### tz

TimeZone

### udev

Userspace DEV

### ulimit

User’s LIMIT

### umask

User’s MASK

### uniq

UNIQue

### i

VIsual = Very Inconvenient

### vim

Vi IMproved

### wall

write all

### wc

Word Count

### wine

WINE Is Not an Emulator

### xargs

eXtended ARGuments

### xdm

X Display Manager

### xlfd

X Logical Font Description

### xmms

X Multimedia System

### xrdb

X Resources DataBase

### xwd

X Window Dump

### yacc

yet another compiler compiler

### Fish

the Friendly Interactive SHell

### su

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

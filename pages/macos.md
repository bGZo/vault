---
draft: true
aliases:
  - darwin
  - MacOS
created: 2024-06-09T12:00:00
modified: 2025-09-27T21:01:47
tags:
  - operating-system
title: MacOS
wikipedia: https://en.wikipedia.org/wiki/Darwin_(operating_system)
---
# MacOS

## Architecture

![[image_1717909749760_0.png]]

## Version

| Version | RelName  | Darwin | Date     |
| ------- | -------- | ------ | -------- |
| 11      | BigSur   | 20     | 20201112 |
| 12      | Monterey | 21     | 20211025 |
| 13      | Ventura  | 22     | 20221024 |
| 14      | Sonoma   | 23     | 20230926 |
| 15      | Sequoia  |        | 202409   |
| 26      | Tahoe    |        | 202509   |

## Fuck app store

## 审查

比如 Mac 端从 Store 中下载的 Telegram 不支持 18+ Show content；via: https://github.com/telegramdesktop/tdesktop/issues/16346

## HiDPI (High Dots Per Inch)

> 在较小尺寸下却拥有较高分辨率的显示器。Apple 将其称作“[视网膜屏幕](https://en.wikipedia.org/wiki/Retina_Display "wikipedia:Retina Display")”，这项技术主要存在于高端笔记本电脑和显示器中
> https://wiki.archlinuxcn.org/wiki/HiDPI

强开低缩放下的 HiDPI via: [[waydabber-BetterDisplay|BetterDisplay]]

## File System

Mac 和 Linux 同属 Unix，而 Unix 设计的哲学就是：「Everything is file」

与 LInux 不用的是，Mac 的应用是沙箱机制，类似 Linux 下的 FlatHub 和 Snap，所有的应用放在 `/Appliction` 下面，拖进来就是安装，放到废纸篓就是删除。与之相对的，用户目录放在 `~/Library`。

```shell
tree -d -L 1
.
├── Applications # 全局应用程序
├── bin # 最基本的命令，比如 ls, cat 等
├── cores # 核心转储文件，系统发生异常时使用，平时为空
├── dev # 设备文件，比如终端，磁盘等
├── etc -> private/etc 
├── home -> /System/Volumes/Data/home
├── Library # 全局共享的资源文件，比如字体、配置等
├── opt # 遵循Unix规范，一般是自己编译的软件
├── private # 系统私有数据存储目录，其中三个目录通过链接挂在/
├── sbin # 系统管理命令，大多数 IO、网络命令
├── System # 系统只读目录
├── tmp -> private/tmp
├── Users # 用户目录
├── usr # Unix 系统资源，包含非核心的系统工具
├── var -> private/var
└── Volumes # 外接硬盘挂在位置
```

## References

- https://web.archive.org/web/20241217020831/https://www.v2ex.com/t/1097598
- https://www.quora.com/On-Linux-everything-is-a-file-is-this-the-same-on-a-Mac-OS-because-it-is-based-on-Unix

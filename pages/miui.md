---
draft: true
aliases:
  - 澎湃OS
  - MIUI
created: 2024-12-08T21:26:22
modified: 2025-08-31T11:08:59
title: MIUI
---
# MIUI

## 魔改 ROM

### Wifi Direct

把系统自带的给砍了，只有自家的小米快传支持，其他家基本也这样做，换来了一大堆形态各异的快传 APK....

via: https://web.archive.org/web/20220313035433/https://c.mi.com/thread-2205843-1-0.html

## ROOT #deprecated

MIUI Root 的两个条件：**[MI FLash](https://lanzous.com/id0jgad) 解 BL 锁**, + 开发版及以上/系统支持 (虚拟) 机, OV 厂的手机可以退而求其次用虚拟机. IPhone 用户越狱可以用 **[[Checkra1n](https://checkra.in/)]**

MIUI 有两种刷机方式

- 线刷 / fastboot 刷机 / `.gz`
	- 分区镜像
- 卡刷 / recovery 刷机 / `.zip`
	- ota 格式的包

![Image](https://pbs.twimg.com/media/Fl2mdvQacAAkwNH?format=png&name=large)

两种刷机方式不兼容, 各有各的包, 如今线刷包越来越少, 官方卡版本, 不循序进行降级操作, 卡刷包同样无法降级, 只能在开机的时候才可以刷入. 如果将卡刷包刷入线刷后会报错:`“couldn't find script”`. via: https://www.mobile01.com/topicdetail.php?f=634&t=5994087. 官方也有对应的教程. 如 [通用线刷教程](http://www.miui.com/shuaji-393.html), [小米手机刷机教程(高通机型)](https://www.xiaomi.cn/post/5326872)

ROM 仓库：

- [MIUI官方ROM仓库](https://roms.miuier.com/weekly/)
- [台湾镜像]( https://mirom.ezbox.idv.tw/)

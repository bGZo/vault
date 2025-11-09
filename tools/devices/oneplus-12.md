---
draft: true
aliases:
  - 一加12
  - Oneplus-12
created: 2025-04-04T23:33:28
modified: 2025-11-08T21:11:09
tags-link:
  - "[[android]]"
title: Oneplus-12
---
# Oneplus-12

## 入手原因

### iOS + Android 双持

Android 上面有非常多的软件生态，iOS App Store 的上架策略很严，所以很多这方面的软件就消失了。比如

- [[kiwibrowser-src.next|kiwi browser]]: 手机浏览器
    - Okey, It's died on Apr 8, 2025
- [[mihonapp-mihon|mihon]]: 漫画阅读器
- [[PicGo-flutter-picgo|flutter-picgo]]: 图床上传器
- [[Mygod-VPNHotspot|VPNHotspot]]: VPN 热点分享
- [[Predidit-Kazumi|Kazumi]]: 追番聚合
- [[rosuH-EasyWatermark|EasyWatermark]]: 水印

### 家人守护

我很难再找到一款可以替代「家人守护」的软件

### 拍照

有喜有悲，一开始拿到手，有 120X 的变焦拍摄还是很惊艳的，但其实这只是算法，并且 12 在后续的 OTA 上做了等级阉割，他的拍照水平是不如自家的旗舰 FindX 系列的。实际的潜望长焦也就那样，远远不如 Pixel 的 30 倍变焦 [^algo-photo]：

[^algo-photo]: I hate this. 比较介意的点，是算法介入，一旦有了 AI 识别修复，那么拍照记录的意义又在哪呢？就像是万恶的美颜算法，都是假的。via: https://www.bilibili.com/video/BV1cbA3eeEzb

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1TdameXEF5&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1TdameXEF5' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1TdameXEF5</a></center>

## 担忧

### 屏幕品控

一加 12 的屏幕品次真是仅次于小米 11 烧 CPU 的大问题： https://www.coolapk.com/feed/63671089?shareKey=ZDRiZThlNzdlOTJiNjdlZTMwOTY~&shareUid=2988517&shareFrom=com.coolapk.app_15.2

### 碎屏险只保两年

![300](https://raw.githack.com/bGZo/assets/dev/2025/1000000280_origin_Screenshot_2025-04-09-14-34-54-96.jpg)

## Magisk ROOT

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV19Bf5YJEDD&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV19Bf5YJEDD' target='_blank' class='external-link'>https://www.bilibili.com/video/BV19Bf5YJEDD</a></center>

首先解锁：

```shell
adb reboot bootloader
fastboot flashing unlock
```

去大侠阿木， https://yun.daxiaamu.com/OnePlus_Roms/ ， 下载全量包，因为源站不再提供直链下载，你会得到一个百度网盘的链接。

下载对应版本的全量包，然后随便找个提取器，提取器提取 `boot.img`， 如 https://github.com/ssut/payload-dumper-go

拿到对应的 `boot.img`，去 `Magisk` 修复引导文件，然后进入 `bootloader` 重新刷入引导，你就成功拿到了用户级别的 ROOT。

```shell
# 检测是否存在已连接的设备  
fastboot devices
# 刷入  
fastboot flash boot [magisk_patched-xxx.img 文件路径]  
# 终端输出 Finished 表示成功  
# 重启  
fastboot reboot
```

> [!NOTE]
> 在刷机的过程中，我这边多次出现了进 fastboot 后不识别设备，输入命令然后就进入了等待模式，显示 `<Waiting for Device>`，我的解决办法就是多试一试，

或者你可以去 https://magiskcn.com/pixel-boot.html 拿到别人打好的包

## 应用安装

### ADB 无线调试

开发者模式打开无线调试

```shell
adb connect 192.168.46.1:5555
```

重新连接

```shell
adb kill-server
```

## 折腾模块

### 隐藏 ROOT

- Shamiko，与 Magisk 自带的工作原理相反，前者考注入隐藏，后者考不住入隐藏；

### 恢复 Play Integrity

下载这个 App 检查下自己的环境：`Play Integrity API Checker`，主要检测三个指标：

- MEETS_DEVICE_INTEGRITY：系统没被改动/解锁（或成功伪装）
- MEETS_BASIC_INTEGRITY：没被当成模拟器 / 恶意环境
- MEETS_STRONG_INTEGRITY： 设备 + 系统 + 密钥链全部原生纯净（**root / 自制 ROM 永远=NO**）

### 是否要切换为 KernelSu

## 叛逃氧 OS：反诈

之前没有感觉，直到真打过电话来才有感觉，不能一直这样下去，得想办法跑掉。但仍然有如下阻力：

1. 无法 OTA，每次升级之后都会丢信号；
2. 氧 OS 没有回锁可能无法用支付宝？ https://www.bilibili.com/video/BV1UmPseQEuU

## References

- 一加未来可能全面降级： https://www.coolapk.com/feed/63756148?shareKey=NjY2YmNkZmY1NWI4NjdlZDQxNzI~&shareUid=2988517&shareFrom=com.coolapk.app_15.2
- https://oplus.icu/

---
draft: true
aliases:
  - Pixel 8 Pro
  - Pixel7 Pro
created: 2025-11-07T05:43:48
modified: 2025-11-08T21:11:57
title: Pixel 8 Pro
---
# Pixel 8 Pro

如果国产真的好，我是一辈子都不会碰 Pixel 的，如果国产真的好，那么 Pixel 三星这种手机厂商就会被国产卷死，实际上呢？各玩各的，你爱用不用。

要不是上周突然的一通反诈电话，我还会抱着 [[oneplus-12|一加12]] 继续用吧，用处不多不少，但都很关键，比如：

1. 通话录音
2. 大容量硬盘
3. 家人守护

如果是 24+1T 的顶配，使用场景会变得更宽，比如：

1. 彻底同步 OneDrive 网盘；
2. 24G 内存跑 LLM；

这一些都很美，但是就是有我开头说的那个问题，我不知道他会泄漏我的什么数据，所以我完全无法尽善尽美的在这台手机上工作。这一记电话让我在这台手机上的任何行为都倍感压力。所以我不得不换机。替他的替代还有什么呢？

1. 继续用一加，然后刷氧 OS
2. 三星
3. Pixel

我选择了最后，因为三星有 SIM 卡送中 [^sumsung-on-china] 的问题，但 Pixel 又都是单 SIM 卡的手机，所以至少我会卖一台 Pixel，然后可能会把一加刷成氧 OS，必要的时候 DSU 到 Color OS 用下家人守护，暂时就这些。

[^sumsung-on-china]: https://www.v2ex.com/t/1121351

## 后续

买到的这个设备，版本是 `BP3A.251005.004.B1`，是一个 Beta 系统，看选择界面也无法跳过，只能强制更新，对于想 ROOT 的我来说，是一场噩梦。

刷机嘛，对吧，对于 Pixel 非常简单：

```shell
# 识别设备
$ adb devices
List of devices attached
38181FDJG008CJ	device

#重启进入 Bootloader
$ adb reboot bootloader

# 解锁 BL
$ fastboot flashing unlock
OKAY [  0.017s]
Finished. Total time: 0.017s

# 查看当前设备，找包
$ fastboot getvar product
product: husky
Finished. Total time: 0.000s

# 检查当前的引导版本，发现无法刷到 Android 15
$ fastboot getvar version-bootloader
version-bootloader: ripcurrent-16.3-13642541
Finished. Total time: 0.000s

# 回锁
$ fastboot flashing lock
OKAY [  0.222s]
Finished. Total time: 0.222s
```

最后失败了，非常流畅，原因就是这则公告：

> Pixel 8（8、8 Pro、8a）设备的 2025 年 5 月更新包含一项启动加载程序更新，该更新会增加启动加载程序的防回滚版本。这样可以防止设备回滚到之前存在漏洞的引导加载程序版本。在这些设备上刷写 2025 年 5 月更新后，您将无法刷写和启动旧版 Android 15 build。
> https://developers.google.com/android/images?hl=zh-cn#special_instructions_for_updating_pixel_devices_to_the_may_2025_monthly_release

当前的 Pixel 8 Pro Android 16 的 ROM 包版本号全是测试版（前缀 `BP`），什么意思呢？虽然正式版的 Android 16 GSI [^GSI] 已经发布了 [^android-16-release]，但是对于 Pixel 8 Pro 的适配版本还在测试中，可能会在接下来 1～2 个月发布。我寄即使我退出 Google 的 Beta 测试，我仍然无法收到 OTA 的升级包，非常操蛋。

[^GSI]: https://developer.android.com/topic/generic-system-image/releases?hl=zh-cn
[^android-16-release]: https://en.wikipedia.org/wiki/Android_16

能做什么呢？

1. 主机用 Beta 的系统，每个月活着半个月重新刷一次 ROOT；
2. 卖掉；

因为我不太喜欢折腾，对于 Pixel OS 本身也不太习惯，最后还是选择了卖掉。不过卖的倒是很快，总体使用了半天下来，有点感受记录一下：

1. Beta 系统会强制更新，看 Reddit 还有数不尽的 BUG 和抱怨；
2. Google 相机的拍照是真好，突然觉得 OPPO 的影像就是算法垃圾；
3. 系统动画并不如 OPPO，这点确实得承认，流畅归流畅，动画总有掉帧；
4. 跟国产类似，Pixel 的广告无法容忍，负一屏的探索关掉几乎就没用了；
5. 小横条、桌面搜索框无法隐藏，这两个 UI 几乎是老化机器的通病；
6. 地区限制，跟三星类型，很多功能都是锁区的，比如 Google VPN；
7. 5G 方案，Pixel IMS 被封过一次，即使有解决方案，也算是 Google 对在华设备的一次打击，我怀疑未来的可用性，毕竟我不想买次升级系统都刷写一遍电话；
8. 录音通话，跟 5G 类似，需要特殊手段才能开启，并且不一定稳定，加上还需要考虑如何让自己的微信语音也走录音，也是一个很大的问题；
9. 马达有点硬，不如一加 12 舒服；

## 参考方案

1. https://sspai.com/post/78200
2. https://github.com/EstebanForge/Pixel-VoLTE-VoWIFI-5G-Enabler
3. 我很怕 Pixel 可能最后和 氧 OS 一样，每次更新都得刷一遍基带，via: https://www.bilibili.com/video/BV1UmPseQEuU

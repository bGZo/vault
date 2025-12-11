---
comments: true
draft: false
aliases:
  - How to install and use chatgpt on rooted android
  - What problem you could meet when using chatgpt on a rooted android
created: 2025-06-12T23:41:37
modified: 2025-12-11T22:18:58
tags: []
title: How to install and use chatgpt on rooted android
type: how-to
---

# How to install and use chatgpt on rooted android

总的来说，在 ROOT 的手机上使用 chatGPT，你可能会遇到的几个问题：

1. Devices's date and time are set properly
	1. ![](https://raw.githack.com/bGZo/assets/dev/2025/1749868182517.png)
2. PlayIntegrity: Preauth PlayIntegrity verification failed
	1. ![](https://raw.githack.com/bGZo/assets/dev/2025/1749826001219.jpg)
3. Unusual Activity Coming from your system
	1. ![](https://raw.githack.com/bGZo/assets/dev/2025/1749826400677.png)

第一个可能是手机的 Play 版本比较低，我在尝试更新过后可以正常使用。

第二个和第三个其实是一个问题，就是 Play Integerity 不完成，Google 验证过不去导致的。所以问题变成了如何修补 Play Integerity。先来下载这个 App 检查下自己的环境：`Play Integrity API Checker`，看看这几个指标：

- MEETS_DEVICE_INTEGRITY：系统没被改动/解锁（或成功伪装）
- MEETS_BASIC_INTEGRITY：没被当成模拟器 / 恶意环境
- MEETS_STRONG_INTEGRITY： 设备 + 系统 + 密钥链全部原生纯净（**root / 自制 ROM 永远=NO**）

显然一个 ROOT 过后的手机不可能满足上面三个条件，因此需要第三方模块来隐藏，分别是：

1. Integrity Box v16, https://github.com/MeowDump/Integrity-Box
2. Play Integrity Fork v14, https://github.com/osm0sis/PlayIntegrityFork
3. Tricky Store, https://github.com/5ec1cff/TrickyStore

三个项目依次安装，然后在模块内运行，重启手机，上面三个就能全绿了。

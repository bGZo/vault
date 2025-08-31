---
aliases:
  - 安卓
  - Android
created: 2020-05-01T00:00:00
modified: 2025-08-31T11:14:57
tags: []
title: Android
---

# Android

由 google 主导的移动设备开源系统, 根据 Android 开源项目 (AOSP), 手机厂商可以创建定制的 Android 操作系统版本, 将设备和配件移植到 Android 平台

我曾非常喜欢酷安的一个功能，【应用集】，相信我，这也是我为什么会养成下载他的习惯的原因之一，在中国，永远有一条铁律，美好的事情不将长久，一切美好都被审查终结了。

## App Collections

国内软件大多走双标的路线. 开拓海外市场的 app 出了两个版本 (国内版/国际版). 国际版上架 Goolge Play , 接受 Google 审核的版本, 所以上架 Google Play 的 app 软件包总是容量偏小, 而且基本没有需要获取用户隐私的流氓行为. 国内版就不然了.

- Command line: [[termux-termux-app]]
	- **0.90 及以上** 版本需要 **Android7.0 及以上版本的系统**. 此安装包由 **F-Droid 编译并签名**, 且**保证与此源代码 tarball 保持一致**.
- **APKPure**
- Coolapk
- Clash
- Onedrive
- Outlook
- Bitwarden
- Zarchiver Pro
- [[kiwibrowser-src.next]]
- Root:
	- [vtools](https://github.com/helloklf/vtools)
	- Sence.
- Weread
	- 下载书的目录: `/data/data/com.tencent.weread/databases/210837723/book/database`
- Wechat `/storage/emulated/0/Android/data/com.tencent.mm/MicroMsg/Download`
- QQ: `/storage/emulated/0/Android/data/com.tencent.mobileqq/Tencent/QQfile_recv`
- [SD Maid](https://sdmaid.darken.eu/)
- [虚拟大师](https://www.vmos.com/)
	- 冲动消费
		- 最近入了 Coolapk 上的 [VMos Pro](https://www.vmos.com), 感觉这个 APP 很有可能在国内被 Ban, 仓促购买是我大意了, 总而言之, 开始把 QQ, Wechat, Alipay 搬运到虚拟机 (Xposed) 里了, 于是就有了换 8G 内存手机以来第一次希望为内存扩容的欲望, 还是如 安迪 - 比尔定律 那样, 多余的内存总会被未来的什么东西吃掉. 未雨绸缪永远是个好习惯. 加上之前也有用太极 阴的经历, 难免有一些想法.
	- Bugs
		- 以部落冲突为代表的游戏闪退/不可用
		- 淘宝无法浏览商品
		- 官方银行不可用
- PC 虚拟屏幕
	- [SuperDisplay](https://superdisplay.app/)
	- [spacedesk | Multi Monitor App | Virtual Display Screen | Software Video Wall](https://www.spacedesk.net/)

## More playable

魔改必须要 Root, 灰色地带的 Root 可以薅一些隐藏的羊毛

- [[root|Root]]
- [[xposed|XPosed]]
- [[xposed-taichi|Taichi]]

## Install APK

- [应用的安装路径和过程](https://cn.apkjam.com/blog/app-installation.html)
- Android 应用涉及到的路径有：
	- `/system/app` 系统自带的应用程序，无法删除。root 后可以删除，
	- 注意
	- 可能造成系统崩溃
	- `/data/app` 用户程序安装的目录，有删除权限。安装应用时会把 apk 文件复制到此目录
	- `/data/data` 存放应用程序的数据
	- `/data/dalvik-cache` 将 apk 中的 .dex 文件安装到该目录下（.dex 文件是 dalvik 虚拟机的可执行文件)
- 复制 apk 安装包到 `/data/app` 目录下，解压并扫描安装包
- 把 .dex 文件（Dalvik 字节码）保存到 `/data/dalvik-cache` 目录，并在 `/data/data` 目录下创建对应的应用数据目录

## BlueStack

> virtualbox+androidx86+intel libhoudini+host 渲染加速
>
> **virtualbox 解决 emulator 载体问题**,**android x86**使得 guest 是 x86 架构, 在系统层面确保 gust host 架构相同, 免除指令模拟,**intel libhoudini** 是 intel 提供的免费但不开源 arm to x86 指令翻译工具, 这个工具使得只提供了 arm so 的 app 在 emulator 成为可行且性能不错 (由于不开源, 不知道翻译是发生在哪个阶段, 但我猜是运行时动态翻译, 文档显示翻译后性能接近直接跑 x86 指令, 实测的确如此！) **host 渲染加速**基本原理是, 在 guesthost 间建立一条高速数据传输通道, 将 guest 端渲染命令打包传给 host 端, host 端解包再执行命令, 最后把结果返回, 注意, 这里很多时候是要求同步的, 这也是为什么强调通道必须高速. 另外, 别说我为何知道这些细节, 因为我正在做这玩意！(?????说了我也不太了解,++)

- 为什么卡? via: https://www.zhihu.com/question/33423859/answer/57133469
	- Intel X86/64 上无法运行 ARM, 所以采用模拟, 模拟带来的时间损耗是数量级的. 利用 QEMU 转 x86 解释执行, 效率远低于 hyper-v 的 x86 硬件虚拟化.
	- > 这不同于 virtualbox 里跑 linux, guest 指令几乎不用模拟直接在 host cpu 上执行 (?????)
	- 渲染软实现, 没有 Host 端硬件加速.
	- 对比 iOS: 模拟了一个运行 iOS 环境的虚拟机, 所有 iOS 代码 compiled 之后都可以 mac-native 的速度运行. 而 QE 模拟了包括 storage system, screen 在内的几乎所有的硬件.
	- Method
	- 保存 emulator 的 snapshot, 具体在 AVD manager 中勾选 "Store a snapshot for faster startup"；
	- 使用硬件加速, 比如你在使用的电脑是基于 x86 架构的, 而你需要模拟的 android 设备也是 x86 架构的, 那么使用硬件加速可以很大的提升 emulator 的速度, 此时你需要安装 Intel’s Hardware Accelerated Execution Manager (HAXM)；

## Android 进程分类 (6)

- 前台进程 (foreground)
	- 目前正在屏幕上显示的进程和一些系统进程。举例来说，Dialer Storage，Google Search 等系统进程就是前台进程；再举例来说，当你运行一个程序，如浏览器，当浏览器界面在前台显示时，浏览器属于前台进程（foreground），但一旦你按 Home 回到主界面，浏览器就变成了后台程序（background）。我们最不希望终止的进程就是前台进程。
- 可见进程 (visible)
	- 可见进程是一些不在前台，但用户依然可见的进程，举例来说： widget、输入法等，都属于 visible。这部分进程虽然不在前台，但与我们的使用也密切相关，我们也不希望它们被终止（你肯定不希望时钟、天气，新闻等 widget 被终止，那它们将无法同步，你也不希望输入法被终止，否则你每次输入时都需要重新启动输入法）。
- 次要服务 (secondary server)
	- 目前正在运行的一些服务（主要服务，如拨号等，是不可能被进程管理终止的，故这里只谈次要服务），举例来说：谷歌企业套件，Gmail 内部存储，联系人内部存储等。这部分服务虽然属于次要服务，但很一些系统功能依然息息相关，我们时常需要用到它们，所以也太希望他们被终止。
- 后台进程 (hidden)
	- 虽然作者用了 hidden 这个词，但实际即是后台进程（background），就是我们通常意义上理解的启动后被切换到后台的进程，如浏览器，阅读器等。当程序显示在屏幕上时，他所运行的进程即为前台进程（foreground），一旦我们按 Home 返回主界面（注意是按 Home，不是按 Back），程序就驻留在后台，成为后台进程（background）。后台进程的管理策略有多种：有较为积极的方式，一旦程序到达后台立即终止，这种方式会提高程序的运行速度，但无法加速程序的再次启动；也有较消极的方式，尽可能多的保留后台程序，虽然可能会影响到单个程序的运行速度，但在再次启动已启动的程序时，速度会有所提升。这里就需要用户根据自己的使用习惯找到一个平衡点。
- 内容供应节点 (content provider)
	- 没有程序实体，仅提供内容供别的程序去用的，比如日历供应节点，邮件供应节点等。在终止进程时，这类程序应该有较高的优先权。
- 空进程 (empty)
	- 没有任何东西在内运行的进程，有些程序在程序退出后，依然会在进程中驻留一个空进程，这个进程里没有任何数据在运行，作用往往是提高该程序下次的启动速度或者记录程序的一些历史信息。这部分进程无疑是应该最先终止的。
- MinFreeManager
	- 设置这六类进程的管理策略
- [Android 内存管理原理](https://cn.apkjam.com/lmk.html)

# [[navigation|Navigation]]

- [Download APK Fast, Free and Safe on Android](https://apkpure.com/)
- [APKMirror - Free APK Downloads - Free and safe Android APK downloads](https://www.apkmirror.com/)
- [下载Android应用程序-下载，恢复，在Uptodown分享](https://cn.uptodown.com/)
- [豌豆荚手机精灵](https://www.wandoujia.com/)

## References

- `.nomedia`: [[~_nomedia-文件的作用]]
- [是谁让安卓变卡了 - 简书](https://www.jianshu.com/p/f6d731683ca7)
- [LearningNotes|Enjoy Learning.](https://github.com/francistao/LearningNotes)
- [AndroidInterview-Q-A|The top Internet companies android interview questions and answers](https://github.com/JackyAndroid/AndroidInterview-Q-A)
- [android|Smartisan open source code for full build.(repo manifest xml)](https://github.com/SmartisanTech/android)
- [Markwon|Android markdown library (no WebView)](https://github.com/noties/Markwon)
- [WeiXinMPSDK](https://github.com/JeffreySu/WeiXinMPSDK)
- [Notes](https://github.com/coder-pig/Android-Storage-Box)

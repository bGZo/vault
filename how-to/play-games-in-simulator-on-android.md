---
comments: true
draft: true
aliases:
  - 如何在安卓模拟器上玩游戏
  - How to play game in anndroid
created: 2025-07-16T20:04:24
modified: 2025-12-17T07:16:51
tags: []
title: 如何在安卓模拟器上玩游戏
---

# 如何在安卓模拟器上玩游戏

上学校的时候没有自己的电脑，充其量就配一台手机，所以唯一能承载娱乐的就是一台安卓机，如今游戏手机市场不在像十年前那样繁荣，我记得游戏强制版号还没出来的时候，TapTap 还没有分国际服和国服，上面还是会有一大堆直装游戏。我以为自己捡到了宝，印象非常深刻，比如：

- 異次元通訊
- 银河牛仔
- ....

具体还有什么我已经记不清了，只是后来一切都变了，taptap.io，也就是国际服分出去之后，虽然还能支持支付宝收款，但屏蔽国区，已经没有再办法正常用了。后面我就把账号注销了，尽管我已经在上面花钱买了很多游戏，比如：

- 去月球
- 我在 7 年之后等你
- 帕斯卡契约
- MushDash
- ....

还买了什么也不记得了，甚至因为什么删号的，我也忘记了。总之，能在安卓手机上玩到更多的游戏，总不见的是一件坏事。

我是没想到自己在成为社畜之后仍然有这个需求，因为公司市场要加班，就总是需要一些东西打发时间，等待时间打卡下班。所以这个需求只增不减，好惨😭

如果你财力雄厚，可以直接用国内出的云电脑服务，当然这不是这片文章的重点，就不展开了。

根据你的喜好，能玩的游戏种类还是比较多的，比如：

- Galgame 模拟器
- Switch 模拟器
- Windows / PC 模拟器
- PSP 模拟器
- GBA 模拟器

## Galgame

这类游戏我接触的比较多，因为性能要求不高，有这方面需求的人也早在十多年前就开始折腾了，解决方案很多，还有非常多安卓直装包，甚至还有把自家付费程序打包进软件的厂商。绿绒混杂，请自行臻辩。

总体上来说，根据制作游戏的引擎不通，需要用的模拟器也不尽然，如：

- KrKr2
	- https://github.com/zeas2/Kirikiroid2
	- https://github.com/2468785842/krkr2
- JoiPlay
	- https://joiplay.cyou
- [Tyranor模拟器正式发布|个人日记 - 绯月ScarletMoon](https://bbs.kfmax.com/read.php?tid=912800&sf=233)
	- https://wwa.lanzoui.com/i3138upab7i
- [Studio O.G.A.](https://onscripter.osdn.jp/)
	- [onsshare/onscripter: onscripter clootection](https://github.com/onsshare/onscripter)
- [xupefei/Locale-Emulator: Yet Another System Region and Language Simulator](https://github.com/xupefei/Locale-Emulator)

为了弄懂这些东西，你可能需要懂一些这些游戏背后的制作引擎，如：

- KiriKiri -> `Krkr2`
- NScripter -> `OneScripts Plus`

更多请参考： https://en.wikipedia.org/wiki/List_of_visual_novel_engines

---

## Switch 模拟器

2023、2024 年本身就要发布 Switch 2 的，但是考虑到模拟器横行，任天堂跳票了，在 2024 年大规范起诉模拟器，大部分模拟器被牵连关闭，比如

- Yuzu / https://yuzu-emulator.com
	- 包含其他分支，如 Suyu、Nuzu
- Ryujinx / 龙神 https://github.com/GreemDev/Ryujinx
- Sudachi / https://github.com/emuplace/sudachi.emuplace.app / https://sudachi-emulator.com

当然，还要大量的模拟器出现，2025 年仍然有效的有：

- https://github.com/eden-emulator
- https://github.com/winterwisperer/sudachi / https://sudachiemulator.org
- https://git.citron-emu.org/citron/emulator / https://citron-emu.org / https://github.com/Zephyron-Dev/Citron-CI/tree/main

当然这些全是 Yuzu 的 Fork 版，就是改包换名而已。如果你要玩，下面是一些有用的链接 [^switch-link-ref]：

- `prod.keys` 下载
	- https://raw.githubusercontent.com/ZeeWanderer/s/refs/heads/master/prod.keys
	- https://prodkeys.net/version15/
- 固件下载：
	- https://github.com/THZoria/NX_Firmware
	- https://prodkeys.net/yuzu-f
- 驱动下载：
	- [[K11MCH1-AdrenoToolsDrivers|AdrenoToolsDrivers]] https://github.com/K11MCH1/AdrenoToolsDrivers
	- https://suyuemulator.dev/switch-gpu-drivers-download
- 游戏下载：
	- https://www.gamer520.com

<iframe src="https://www.youtube.com/embed/Php0Idwajtc" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=Php0Idwajtc' target='_blank' class='external-link'>https://www.youtube.com/watch?v=Php0Idwajtc</a></center>

[^switch-link-ref]: https://www.reddit.com/r/EmulationOnAndroid/comments/17d0fmfario_bros_wonder_run_30_fps_stable_on_yuzu/t, https://docs.mesa3d.org/drivers/freedreno.html, https://gitee.com/dreamboyn81/dreaming-space

## PC 模拟器

这个视频说的很清楚了：

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1QSJfzQEEg&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1QSJfzQEEg' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1QSJfzQEEg</a></center>

总之有几个问题，概括起来就是全部模拟器都不像 SD 那样集成度高，如果想要模仿 SD，就要走一遍 SD 的路：

1. 内容分发，手机没有原生的 Steam，所以你只能从电脑倒入到手机；
2. 驱动下载，基本没有哪个商家愿意花时间去做驱动，你只能用五花八门的开源驱动，并且表现都不一样；
3. 社区支持，大多数玩家的折腾都是在社媒上零零散散地分布着，很多经验和资源无法重复利用，存在大量的浪费；

- [[olegos2-mobox|mobox]]
- [[brunodev85-winlator|Winlator]]

## 待解决的问题

- [ ] Switch 模拟器锁帧

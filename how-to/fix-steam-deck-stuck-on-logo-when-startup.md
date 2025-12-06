---
comments: true
draft: false
aliases:
  - 如何修复 Steam Deck OLED 开机卡 Logo
  - How to fix steam deck stuck on logo when startup
created: 2025-11-30T14:01:38
modified: 2025-11-30T14:14:25
tags: []
title: 如何修复 Steam Deck OLED 开机卡 Logo
---

# 如何修复 [[steam-deck|Steam Deck OLED]] 开机卡 Logo

先写下自己怎么搞坏的吧，我自己准备了一块 Windows 的启动盘，然后进 Windows，进去更新了 Windows，打好了驱动，但是发现蓝牙无论如何都无法识别。Reddit 当然有一些方法，但 OLED 和 LED 的版本还不一样，还没有办法通用，所以暂时无解。

折腾完，我看着挺完美，就直接放过去了，下个星期准备玩的时候才发现连 Steam 主系统都进不去了，非常震惊，是没想到装个 Windows 然后会把我的主系统都搞坏掉。

能怎么办呢，我收集了网上的资料，大致看了下：

1. 重置 CMOS；
2. 做一个 Linux 恢复镜像，然后从 U 盘进入恢复系统；
3. 回滚系统；

最后我用第三种方法恢复了，第一种方法最坑，可能只适用 LCD 的机型，反正我试过之后，连 BIOS 都进不去了。

<iframe src="https://www.youtube.com/embed/Lqf8MT3xn8g" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=Lqf8MT3xn8g' target='_blank' class='external-link'>https://www.youtube.com/watch?v=Lqf8MT3xn8g</a></center>

第二种方法也很蠢，比较折腾，而且不知道我的数据能不能被完美的保留下来，我还存着非常多截图在用户目录呢，不能就这么丢了。

然后尝试第三种方法成功了，具体步骤如下：

1. quick access + 电源键
2. 选择下面的 B 版本系统，执行回滚

然后坐和等待，全程大概 20 分钟，系统就恢复好了；

<iframe src="https://www.youtube.com/embed/FBIYKla2z_Y" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=FBIYKla2z_Y' target='_blank' class='external-link'>https://www.youtube.com/watch?v=FBIYKla2z_Y</a></center>

如果上述步骤无法解决你的问题，你可能只能通过方法 2 了，具体步骤可能需要查看官网的指南，如下： https://help.steampowered.com/zh-cn/faqs/view/1B71-EDF2-EB6D-2BB3

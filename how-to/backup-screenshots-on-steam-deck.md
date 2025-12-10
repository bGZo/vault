---
comments: true
draft: true
aliases:
  - 如何在 Steam Deck 上备份截图
created: 2025-12-08T22:18:09
modified: 2025-12-08T23:31:04
tags: []
title: 如何在 Steam Deck 上备份截图
---

# 如何在 Steam Deck 上备份截图

Steam 本地当然提供了截图的管理功能，还有画廊，还有 Steam 云上传，全程无缝，但是有个问题，我有上千张截图，你让我一个一个上传？简直在开玩笑，好吧。

借助之前的折腾： [[enable-user-smb-on-steam-deck|在 Steam Deck 上开启用户级别的 SMB]]，我们有了一个随便怎么折腾都不会挂掉的 SMB 服务，可以随时用 Mac 等设备连上 Steam，管理 Steam 的文件。

这样的背景下，我们的管理截图的需求就变成了如何快速定位截图的位置，我们可以用软连接达到这一点，因为用户目录一般都是在缓存里存着，所以最好创建一个用户目录级别的软连接：

```shell
ln -s /home/deck/.local/share/Steam/userdata /home/deck/userdata
```

因为我有三个 steam 账户，所以对我而言，需要创建三个截图目录，具体命令如下：

```shell
ln -s /home/deck/.local/share/Steam/userdata/12467603290/760/remote /home/deck/Pictures/bgzous
ln -s /home/deck/.local/share/Steam/userdata/131140098148/760/remote /home/deck/Pictures/bgzocn
ln -s /home/deck/.local/share/Steam/userdata/141420650290/760/remote /home/deck/Pictures/bgzotr
```

这样，下次直接访问 `Pictures` 就可以直达自己账户下游戏的目录，如果需要备份，直接拖出来就是，或者使用 `rclone`，都很好。

我是直接拖到 Onedrive 备份的，这里就不赘述了，感兴趣的人自行研究。

顺便贴一下，本地录制的目录在

`~/.local/share/Steam/userdata/<你的Steam ID>/gamerecordings/`， 但都是 steam 内部格式，需要在桌面端图库界面进行导出之后才能在 Videos 目录下找到。


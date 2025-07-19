---
aliases:
  - 存储
created: 2024-01-28T00:00:00
modified: 2025-07-19T12:50:03
tags:
  - 3C
  - tool
title: 存储
---

# 存储

## Why

## How

## What

### 存储介质

#### [[ssd|SSD]]

- [[~深入浅出ssd]]

#### HDD

- S.M.A.R.T. Self-Monitoring Analysis and Reporting Technology 自我监测、分析及报告技术
	- 一种自动的硬盘状态检测与预警系统和规范。通过在硬盘硬件内的检测指令对硬盘的硬件如磁头、盘片、马达、电路的运行情况进行监控、记录并与厂商所设定的预设安全值进行比较，若监控情况将要或已超出预设安全值的安全范围，就可以通过主机的监控硬件或软件自动向用户作出警告并进行轻微的自动修复，以提前保障硬盘数据的安全
- ![[2022-04-04_21.39.01_zh.wikipedia.org_5dad25d158b8_1649079902319_0.png]]
via: https://zh.wikipedia.org/zh-cn/S.M.A.R.T.

#### TF SD Card

- TF / SD 卡虽然可拓展性好，但是寿命相较于 NVME 很短，并且买二手的话，受限于没有 SMART 分区，也不知道具体的剩余寿命。
- Bus Speed
- ![[sdex08_1706440111803_0.png]]
  via: https://www.bodnara.co.kr/bbs/article.html?num=147425, https://unwire.hk/2018/06/27/sd-express/dc/cam-parts, https://www.sdcard.org/developers/sd-standard-overview/bus-speed-default-speed-high-speed-uhs-sd-express
- EVO Plus: 三星独有格式.
- Refereneces
	- [[~为什么现在的手机大多已不支持SD存储卡扩展呢]]
	- [[~安卓旗艦為何不採用nvme呢]]

### 检测工具

```shell
# Windows
scoop install diskgenius crystaldiskinfo crystaldiskmark
```

- [电脑怎么检测硬盘坏道的方法 - 知乎](https://zhuanlan.zhihu.com/p/137066637) => DiskGenius
	- ATTO Disk Benchmark
	- AS SSD Benchmark
	- HD Tune Pro
	- `05` + `c5` + `c6`

## Refs

  - [求推荐稳点的硬盘，两块希捷酷鱼 4T 同时挂了 - V2EX](https://www.v2ex.com/t/830555)
  - [手把手，嘴对嘴，讲解硬盘SMART信息 - 知乎](https://zhuanlan.zhihu.com/p/165947075)
  - [CrystalDiskInfo不能识别固态硬盘 - 电脑讨论 - Chiphell -](https://www.chiphell.com/thread-1949105-1-1.html)
  - [机械硬盘的“寻道错误率”该怎么理解？ - V2EX](https://www.v2ex.com/t/618015)

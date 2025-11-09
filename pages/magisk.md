---
draft: true
aliases:
  - Magisk
created: 2025-08-30T23:51:30
modified: 2025-08-31T00:01:31
title: Magisk
wikipedia: https://en.wikipedia.org/wiki/Magisk_(software)
---
# Magisk

> 随着 SuperSu (XDA 非常著名的开发者 ChainFire 维护的一款作品) 走向商业化 (很久没有更新), 安卓 5.0 之后, 谷歌封堵了大量的漏洞, 一些以商业化模式运作的各种所谓的一键 ROOT 工具全都玩完!, 这些东西相对来说还非常危险, 因为基本任何商业化或者第三方机构给出的超级用户管理工具, 都等于是把你的手机变成别人的了, 甚至他们还可以比流氓还流氓!. 而 SuperSU 不一样, 它一直是保持着非商业化运作, 并且更新非常积极, 但遗憾的是在 2017 年 10 月, 开发者 ChainFire 发布声明不再参与维护 SU, 好像是把 SuperSU 卖给了中国的一家商业化运作的公司, 自此更新节奏非常缓慢, 目前 SuperSU 已经不能实现安卓 O(8.0) 以上更高版本的 ROOT 了, 而取代这一切的, 是 Magisk. Magisk 是一位中国台湾的学生 @topjohnwu 开发的 Android 框架, 它不但可以获取 Root 权限, 而且支持 Magisk 模块. 其第一个版本发布于 2016 年 8 月, 由于当时 Magisk 刚刚出现, 支持的模块并不多, 且 SuperSu 依然流行, Magisk 还鲜为人知. 直到 SuperSu 的消亡, 人们才想起 Magisk, 此后 Magisk 迅速流行起来, 成为每一个玩机爱好者的必备工具. via: https://www.coolapk.com/feed/17973123?shareKey=OTliMmY4NTlkMWNkNWY0NTExYTQ~

## 原理

Magisk 则另辟蹊径, 通过挂载一个与系统文件相隔离的文件系统来加载自定义内容, 为系统分区打开了一个通往平行世界的入口, 所有改动都只在那个世界 (Magisk 分区) 里发生, 并不直接修改系统分区, 这样大大减小了 Magisk 的变砖概率, 而且就算变砖也可以通过卸载 Magisk 来恢复原来的系统分区. 比如我们的/system/xbin 中没有 su, 我们可以通过刷入相应的模块, 在系统启动初期, 将 su 映射到/system/xbin 下来获取 root.

## 教程

- 通过 rec 刷入 Magisk(推荐)
- 直接安装 (需要 Root 权限)(系统版本小于 Android P, 你可能需要先解锁系统分区)
- 通过修补 boot 安装 (选中 Rom 解压后的 boot.img, 并在 rec 中直接刷入修补后的 boot 文件. )

## Modules

- [[Dr-TSNG-ZygiskNext|ZygiskNext]]
- [[mModule-guide_hma|guide_hma]]
- [[osm0sis-PlayIntegrityFork|PlayIntegrityFork]]
    - 环境修复
        - https://xdaforums.com/t/official-chatgpt-app-not-working-on-rooted-device.4649458/
- TEE 假死，指纹修复
	- [[TheFreeman193-PIFS|PIFS]]
	- [[daboynb-playcurlNEXT]]

## References

- https://www.coolapk.com/feed/17697847?shareKey=ODg2YmRkZmRiNGRmNWY0NTExMTQ~
- https://mp.weixin.qq.com/s/Os8j55GNmazqSt2UYrwy1g

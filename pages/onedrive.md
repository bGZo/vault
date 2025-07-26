---
aliases:
  - onedrive
  - Onedrive
  - OneDrive
changelog: 
created: 2024-07-28T21:12:17
description: 
document: 
modified: 2025-07-20T23:44:48
status: 
tags: []
title: OneDrive
type: tool
---

# OneDrive

## Why

- 跨平台
- 容量大

## How

### How to using on [[pages/linux|linux]]?

- [[abraunegg-onedrive|OneDrive for linux]]

### How to using webdev

不支持, 需要自己折腾，参考：

- [2020年onedrive怎么配置webdav? - 知乎](https://www.zhihu.com/question/388430389)
- [OneDrive 支持 webdav 吗 - V2EX](https://www.v2ex.com/t/285903)
- [Connecting securely to Microsoft OneDrive with WebDAV : WinSCP](https://winscp.net/eng/docs/guide_microsoft_onedrive)

## 小文件同步地狱 #issue/wontfix

思考一个场景：

你有一个前端项目，里面有十几万的 node_modules 文件，或者你有一个 Java 后端项目，每次编译生成的 JAR 包都不一样，如果你要全都放在 Onedrive 上，会有什么问题？

$$429 Too many request$$

尤其是对于自动保存的 IDE 来说，敲击一个字符，就意味着重新上传一次。就像是不断增长的 DB，前期几十 K，几百 K，都是小问题，但是后面变成几百 M，每次往进写一点东西，就需要重新上传，这个无论是流量消耗，还是同步问题，都不好解决 [^database-problem]。

所以如果用 **OneDrive 同步源代码就是一个伪需求**。

我能给的意见只有这几点：

1. 同步文件应该是有区间的；
	1. 不要忽视小文件，去尽量优化 meaningless/small size ($<50KB$) 的文件, 像 `.gitignore` 一样, 就比如说我是用的素材管理工具 Billfish 就存在大量的图片缓存 (30G -> 1G);
	2. $>100M$ 频繁改动的文件不要同步
2. 不要在 pause/reset 状态下删除
	1. 整理 (删除) 文件我给出的建议是
	2. reset 之后, 之前做的编辑会失效, 云端和本地两份文件 merge 失败, 当然也非常恶心...
3. 善用 `link/mklink/ln`
	1. 但这样太累了，每个平台都需要重新创造一遍软链接；
	2. 参考软件开发的思路, 减少给部分的耦合, 那么唯一解就只有**通过链接去指向同一个库这个方法了**;

> [!tip]
> 另外一种同步思路就像时间机器，定时把 `workspace` 目录整体压缩为一个 ZIP 文件，上传到 OneDrive 里面即可

## 是否存在 [[censor|审查]] 的问题

> 世纪互联只提供商业版，个人版和家庭版 365 全都是由微软自营
> via: https://www.v2ex.com/t/751037

## Reference

- [为什么微软的OneDrive云盘那么慢？有什么解决办法吗？ - 知乎](https://www.zhihu.com/question/397284246)
- [如何提取OneDrive文件直链？_勿埋我心的博客-CSDN博客](https://blog.csdn.net/qq_43523315/article/details/109450059)

[^database-problem]: 存在的问题软件 [[billfish]]，所有的缓存缩略图都在.bf 的隐藏文件夹中存着，非常难同步，几十上完的文件同步，网络情况实在是难以跟上，太浪费流量了。事发 20221025，但是 20250720 有重新重蹈覆辙。

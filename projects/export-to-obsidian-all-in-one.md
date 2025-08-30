---
aliases:
  - 黑曜石导入计划
  - 黑曜石倒入计划
  - xiaohongshu-export-to-obsidian
created: 2025-03-23T13:00:00
deadline: 2025-03-23T13:38
modified: 2025-08-30T11:12:36
tags:
  - gtd/doing
title: 黑曜石导入计划
type: project
---

# 黑曜石导入计划

## Why

- 用黑曜石管理收藏夹和自己的数据

## How

1. 导出
2. 备份
3. 清空

## Scope

### [[pages/podcast|播客]]

Powered by [[snipd-podcast-format-for-obsidian|snipd snips linter for obsidian]] to [[snipd]].

```shell
snipd export_xxx.md -o test
```

> [!NOTE]
> 但是播放历史还是会丢失，博客时间线还是会回到解放前；

### [[telegramdesktop-tdesktop|Telegram]]

Powered by [[telegram-message-sync-bot|telegram message archive bot]]

```shell
rsync -avz --progress --delete bgzo@192.168.31.20:/home/bgzo/workspaces/telegram-message-sync/archives/channel/ "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/clippers/telegram/"
```

```shell
rsync -avz --progress --delete bgzo@192.168.31.20:/home/bgzo/workspaces/telegram-message-sync/archives/person/ "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/clippers/telegram/person/"
```

> [!NOTE]
> 不可以随便编辑 `clippers/telegram` 的文件，否则就需要立即回写，否则就会导致文件的丢失：

```shell
rsync -avz --progress --delete bgzo@192.168.31.238:"/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/clippers/telegram/" /home/bgzo/workspaces/telegram-message-sync/archives/channel/
```

```shell
rsync -avz --progress --delete bgzo@192.168.31.238:"/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/clippers/telegram-private/" /home/bgzo/workspaces/telegram-message-sync/archives/person/
```

```shell
scp pieroots.md bgzo@192.168.31.20:/home/bgzo/workspaces
```

### [[weread|微信读书]]

Using [[zhaohongxuan-obsidian-weread-plugin|Obsidian weread plugin]]

### [[pages/youtube|Youtube]] #gtd/todo

Go https://takeout.google.com to download what you need.

> [!tip]
> 更好的办法是对这些文件进行二次处理，比如把字幕也加上去；

开发一个 obsidian-clipper-plus，因为 youtube 无法下载字幕到 vault 里面

### Bangumi 追番记录

```shell
pipx install export_to_obsidian
 export BGM_ACCESS_TOKEN=xxx
eto bangumi -t ../templates/sync-bangumi-template.md -s 4 -o ./bangumi 
```

- [ ] 联邦宇宙替代豆瓣等

### Cnblog 收藏夹

```shell
pipx install export_to_obsidian
export CNBLOG_ACCESS_TOKEN=xxx
eto cnblog --output output/cnblog
```

### [[Ranchero-Software-NetNewsWire|NetNewsWire]] 星标文章 #gtd/todo

Export NetNewsWire stared articles #gtd/todo

<iframe src='https://github.com/Ranchero-Software/NetNewsWire/issues/978' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://github.com/Ranchero-Software/NetNewsWire/issues/978' target='_blank' class='external-link'>https://github.com/Ranchero-Software/NetNewsWire/issues/978</a></center>

### 联邦星球点赞的文章 #gtd/todo

### Bilibili 收藏夹 #gtd/todo

OpenAPI 做不到

### 哈巴姆特动画疯追番记录 #gtd/todo

### 聊天记录 #gtd/todo

十年的历史聊天聊天记录再也找不回来了，我相信 Tencent 一定全都持久化了，但就是不给你开放，好难受啊。

- QQ
- Wechat
- 抖音

### V2EX 收藏主题导出 #gtd/todo

OpenAPI 做不到

### [[copilot]] History #issue/wontfix

https://github.com/microsoft/copilot-intellij-feedback/issues/384

### Android Notes

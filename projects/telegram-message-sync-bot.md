---
title: "bGZo/telegram-message-sync-bot"
aliases: "telegram-message-sync-bot"
created: 2025-03-01T17:05:03
modified: 2025-03-01T17:47:57
description: "a telegram bot for archive messages"
source: "https://github.com/bGZo/telegram-message-sync-bot"
tags:
  - "star"
tags-link:
type: "repo"
---

## Repo Meta

![](https://img.shields.io/github/stars/bGZo/telegram-message-sync-bot?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/bGZo/telegram-message-sync-bot?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/bGZo/telegram-message-sync-bot?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=bGZo&repo=telegram-message-sync-bot&bg_color=00000000)](https://github.com/bGZo/telegram-message-sync-bot)

## Why

过去用 [[logseq]] 一直搭配用一款插件 — [logseq-inbox-telegram-plugin](https://github.com/shady2k/logseq-inbox-telegram-plugin)，用于摘取 TG 上转发的内容。说不上好用 [^not-usefiul]，后来我自己 Fork 了 [一份](https://github.com/bGZo/logseq-inbox-telegram-plugin/releases)，对主要特性修改了一些，即使仍然缺乏对超链接的支持，但也顺手了很多。

可是问题仍然存在，为了在小主机上运行这个服务，必须后台同时跑一个 Logseq，要知道，Electron 可不是什么好东西。加上小主机默认没有屏幕，在启动这类 GUI 软件的时候，必须添加 `DISPLAY` 环境变量，如下：

```shell
Environment=DISPLAY=:0
```

总免得有些画蛇添足，说不上优雅。所以这个项目应运而生，我需要长时间地利用 TG bot 监听我的频道，对频道的信息进行归档。

## Quick start

![](https://raw.githack.com/bGZo/assets/dev/2025/202503011548103.png)

```shell
# install dependencies
go mod tidy

# build the result
go build -o tg main.go

# give the right to run. 
chmod +x ./tg

# run bot
./tg sync -t TG_BOT_TOKEN
```

### Optional: run in background using nohup

```shell
nohup ./tg sync -t 5883330296:AAFCI0jtgH1iHU1zDaL2p3Hj5Z6fkqaRWaU > bot.log 2>&1 &

# kill background
pkill -f tg
```

### Optional: run in background using nohup

```shell
sudo vim /lib/systemd/system/tg@.service
```

Add following config:

```shell
[Unit]
Description=tg message sync bot for %i.
After=network.target

[Service]
Type=simple
User=%i
Restart=on-abort
Environment=http_proxy=192.168.31.20:10800
Environment=https_proxy=192.168.31.20:10800
ExecStart=/home/bgzo/workspaces/telegram-message-sync/tg sync -t 58833029:AAFCI0jiHU1zDaL2p3HaRWaU -o /home/bgzo/workspaces/telegram-message-sync/archives

[Install]
# WantedBy=multi-user.target
WantedBy=graphical-session.target
```

Then restart systemd and enable `-`

```shell
systemctl daemon-reload
systenctl start tg@bgzo
systenctl enable tg@bgzo
```

## Features

- [x] 状态检测
- [x] 后台运行
- [x] 日志支持
- [x] 按频道来源进行归档
- [x] 超文本格式支持
    - [x] EMOJI 特殊处理
- [x] 存档反馈
- [ ] Dockerfile
- [ ] 更多消息格式支持（下划线/加粗文本）
- [ ] 持久化内容
    - [ ] 支持时间排序/倒叙
    - [ ] 输出 MD YAML header
    - [ ] 支持自定义模板

## Notes

### 设计的项目

- [[commandline|命令行支持]]: https://github.com/spf13/cobra
- 语言实现：[[golang]]
- 

[^not-usefiul]: 无法格式化文字超链接，无法读取图片的字幕，结合 logseq 的 API 的特性，插件一直无法对含 `tg@username` 的消息进行处理，并且无法转发频道的信息，必须是经过认证人的消息才会被存档。

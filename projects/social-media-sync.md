---
aliases:
  - Social media Post sync
  - Social media post sync
created: 2025-01-18T16:58:21
deadline: 2025-01-18T16:58:21
modified: 2025-07-16T20:53:41
tags:
  - gtd/doing
title: Social media Post sync
type: project
---

# [[social-media|Social media]] Post sync

Before: [[telegram-message-sync-bot|Telegram Message Archive bot]]

## Why

1. 多个平台发布非常烦，我希望通过一个窗口分发；
2. 多个平台的流量支持，覆盖人群更广；

## How

> [!NOTE]
> 暂不考虑图片发布

Golang + Officical API + Third API

一个窗口： [[telegramdesktop-tdesktop|telegram]] + TelegramBot

### Official API

- [x] [[mastodon-mastodon|Mastodon]]
- [x] [[bluesky|BlueSky]]
- [x] [[twitter]]
- [ ] https://api.cnblogs.com
- [ ] 微信公众号
- [ ] Bangumi

https://bangumi.github.io/api/ 中没有，可以看到 https://github.com/bangumi/api/issues/210

```shell
next.bgm.tv/p1/timeline
next.bgm.tv/p1/users/:username/timeline
```

### Third API

- [ ] Douban
- [ ] Jike
- [ ] Weibo
- [ ] Zhihu
- [ ] Bilibili
- [ ] Xiaohongshu
- [ ] Tiktok
- [ ] Kuaishou

## Alternatives

### 1 MultiPost

<iframe src='https://multipost.app/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://multipost.app/' target='_blank' class='external-link'>https://multipost.app/</a></center>

一开始是浏览器拓展，后来就变成网站了，还需要注册账号，有一定门槛。原理是自动操作 Chrome 浏览器，控制按钮点击，还是需要打开源网站，只不过是程序自动操作。非常有 Spam 的味道；

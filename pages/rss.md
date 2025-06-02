---
aliases:
  - RDF Site Summary
  - Really Simple Syndication
created: 2024-12-08T21:26:22
modified: 2025-04-21T22:11:59
description: a web feed that allows users and applications to access updates to websites in a standardized. computer-readable format
released: 1999-03-15
tags:
  - info
wikipedia: https://en.wikipedia.org/wiki/RSS
---

The first time icon of RSS I see is in the CD show. I even don't know what exactly is it. It appeared in the product birthed in last 10 years in China mainland.

And then, when I have some spare time in 2020, I notice it again. I wonder whether it have some interesting story or not. And at that point, I use a simple and not well reader to subscribe RSS. And just feeling amazing, and feel sad as well, like (by the way, they're sucks)

If you host a RSS link, you've well done. I would appreciate you 😘

## Why

Build self host info flow => only focus on some fields.

## How

### Backup and share your subscription.

https://gist.github.com/bGZo/f16fbc8d22cb77ae8078f8ac09234e03

### RSS [[workflow]]

![draws/flow.book.excalidraw](https://raw.githack.com/bGZo/assets/dev/2024/infoflow.excalidraw-fs8.png)

  - When rss failed, go to [Inoreader - Take back control of your news feed](https://www.inoreader.com/). Subscribe, and find the old articles.
  - When you seeing a good source, you shouldn't subscribe immediately, you should save a read latter and done it as soon as possible. Because it will accumulate while you don't care it. Yet it might be a instant source, so it will be spam in the future.
    In deeper, *I take rss more than a reading tool, but their origional purpose, __notification__*.
    - [ ] How to build a good flow of reading latter? When I meet a good blog.
- RSS + **Raindrop + Export to Each Platform**
  - 依赖 Raindrop 的高亮导致无法在 RSS Reader 内阅读;
    - 我想划线高亮, 我就必须跳转到原网站去阅读,
      传统的 Rss Reader 全文抓取失去了意义
    - 稍后读 Read Latter 无所谓, 因为本来就打算在后者阅读
  - 参考同类竞品 [[Alternative]] [[pages/tools]]
    - [简悦 SimpRead - 如杂志般沉浸式阅读体验的扩展](http://ksria.com/simpread/)
    - [Readwise](https://readwise.io/)
    - [Pocket: Home](https://getpocket.com/en/)
    - [Instapaper](https://www.instapaper.com/)
    - No more free 😭 I only could use raindrop.

### Trash Category

I devided the feed to 2 parts:

- Uninstant messages, which I should read it alone. (moonight would be better)
    - I archived article without images using rsstt telegram bot.
    - I browser social media and most blog on another channel.
- Instant messages, which would never take much time(See ((646a045c-74f6-49d4-bbce-78ec1484d73c)))
    - They have some general features:
        - All page just worth a share link.
        - Comments more than article
    - What I collect it
        - [绅士之庭订阅源](https://gmgard.moe/rss)
        - [豆瓣 - 书评](https://www.douban.com/feed/review/book)
        - [Solidot](https://www.solidot.org/index.rss)
        - [ONE · 一个](https://rsshub.app/one)
        - [4Gamers](https://www.4gamers.com.tw/rss/latest-news)
        - [游戏 – 琉璃神社 ★ HACG.me](https://www.hacg.mom/wp/game.html/feed)
        - [V2EX热门](https://rsshub.app/v2ex/topics/hot)

### Find RSS

Some websites will include element whose type is `application/atom+xml` or `application/rss+xml`. They would include RSS link.

```xml
<link rel="alternate" type="application/atom+xml" title="${source.title}" href="${source.url}">
```

And following are some address they mostly used:

```xml
./feed
./rss.xml
./feed.xml
./atom.xml
./rss/index.xml
./index.xml
./rss
./rss/rss
./rss/rss.xml
<!-- Z-Blog via: https://bbs.zblogcn.com/thread-3527.html-->
./feed.asp?user=userID
./feed.asp?tags=TagID
<!-- Youtube -->
https://www.youtube.com/feeds/videos.xml?channel_id=<channel_id>
https://www.youtube.com/feeds/videos.xml?playlist_id=<playlist_id>
```

## What

- [ ] Build yourself RSS reader

### RSS standards

- XML like https://www.tiangal.com/feed
- Atom like https://gmgard.moe/rss

#### [RFC 4287 - The Atom Syndication Format](https://datatracker.ietf.org/doc/html/rfc4287)
#### [[opml]]

Group with Tags

```xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
   <head>
      <title>Opml Template</title>
   </head>
   <body>
     <outline title="News" text="News">
       <outline type="rss" text="title" xmlUrl="url" />
     </outline>
   </body>
</opml>
```

Attributes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
   <head>
      <title>Opml Template</title>
   </head>
   <body>
      <outline type="rss" text="title" xmlUrl="url" group="group/name" />
   </body>
</opml>
```

### What I used in past and recommend now

I prefer like the brave build-in RSS reader😭

- ✨ [[rongronggg9-rss-to-telegram-bot|rss-to-telegram-bot]]
- ✨ [Feedbro - Chrome Web Store (google.com)](https://chrome.google.com/webstore/detail/feedbro/mefgmmbdailogpfhfblcnnjfmnpnmdfa?hl=en)
- ✨ Inoreader to browser feed history.
- Others
    - [期待 V2RSS by angelia](https://v2rss.com)
    - [yang991178/fluent-reader: Modern desktop RSS reader built with Electron, React, and Fluent UI (github.com)](https://github.com/yang991178/fluent-reader)
    - [HenryQW/Awesome-TTRSS: [maintainer wanted] 🐋 Awesome TTRSS, a powerful Dockerised all-in-one RSS solution. (github.com)](https://github.com/HenryQW/Awesome-TTRSS)
    - [zhaoolee/garss: Github Actions采集RSS, 打造无广告内容优质的头版头条超赞宝藏页](https://github.com/zhaoolee/garss) ![](https://img.shields.io/github/stars/zhaoolee/garss)
    - [己思](https://ohmyrss.com/#)

<iframe src='https://openrss.org/rss-feed-readers' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://openrss.org/rss-feed-readers' target='_blank' class='external-link'>https://openrss.org/rss-feed-readers</a></center>

### Half-text RSS sucks, this is over-design

Some website not support output full-text RSS, so we have to open in browser to read. Luckily, we could get full-text RSS through parse url, most rss reader support that. But even more, they change the output format of HTML, and they wouldn't support full-text fetch. You will always see following page:

I know they want to get more actual views, to get more money ads brings. But it's really likely say:

> "Do you want me to tell this stuff?"
> "Suck my dick first, reader 😝"

They're not solving anything, and having put the situation more complex!

![https://blog.skk.moe/post/say-no-to-meta-keywords/](https://raw.githack.com/bGZo/assets/dev/2024/rss_close_full_text_example.png)

via: [Sukka's Blog](https://blog.skk.moe/atom.xml)

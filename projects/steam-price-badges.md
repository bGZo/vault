---
aliases:
  - Steam Price Badge
created: 2023-07-05T00:00:00
remark: 使用 iframe 嵌入页面更加简单；
modified: 2025-07-02T21:49:20
title: Steam Price Badge
type: project
tags:
  - gtd/canceled
---

# Steam Price Badge

Build a API service like https://shields.io, which will show the price of steam in tl.

> [!NOTE]
> 用 `iframe` 省时省力

```shell
<iframe src="https://store.steampowered.com/widget/427520/" frameborder="0" width="646" height="190"></iframe>
```

<iframe src="https://store.steampowered.com/widget/427520/" frameborder="0" width="646" height="190"></iframe>
<iframe src='https://community.chrono.gg/t/how-to-embed-a-steam-store-page-in-a-post/15016' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://community.chrono.gg/t/how-to-embed-a-steam-store-page-in-a-post/15016' target='_blank' class='external-link'>https://community.chrono.gg/t/how-to-embed-a-steam-store-page-in-a-post/15016</a></center>

## Alternatives #gtd/canceled

### 1 Web service

the steam API: `https://store.steampowered.com/api/appdetails?appids=<id>&cc=tr&l=en`

https://store.steampowered.com/app/921570/_/?l=japanese

自己造轮子无法解决跨域的问题：`Build-in web application cannot fetch / request the right url, it would occur CORS error`

例如这个地址： https://store.steampowered.com/api/appdetails?appids=2138000&cc=tr&l=en

```shell
Access to fetch at 'https://store.steampowered.com/api/appdetails?appids=2138000&cc=tr&l=en' from origin 'http://127.0.0.1:8081' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

### 2 Next.JS API?

Inspired by [Steam上的中文Galgame丨SteamGalgame](https://steamgalgame.com/), there is a [Deals - IsThereAnyDeal](https://isthereanydeal.com/) service.

- 内容是直接爬 Steam，价格是外挂组件更新；
- 由 RSS（Feed）地址判断价格信息不包含在文章之内。

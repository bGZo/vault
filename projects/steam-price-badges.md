---
tags: #steam
created: 2023-07-05
mark: 使用 iframe 嵌入页面更加简单；
type: project
---

## Project Meta
## Why
## How
- Build-in web application cannot fetch / request the right url, it would occur CORS error: #deprecated
  - `https://store.steampowered.com/api/appdetails?appids=2138000&cc=tr&l=en`
    - `Access to fetch at 'https://store.steampowered.com/api/appdetails?appids=2138000&cc=tr&l=en' from origin 'http://127.0.0.1:8081' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.`
- Next.JS API?
- Inspired by [Steam上的中文Galgame丨SteamGalgame](https://steamgalgame.com/), there is a [Deals - IsThereAnyDeal](https://isthereanydeal.com/) service.
  - 内容是直接爬 Steam，价格是外挂组件更新；
    - 由 RSS（Feed）地址判断价格信息不包含在文章之内。
## What
### \# Program Description
Build a API service like [Shields.io | Shields.io --- Shields.io | Shields.io](https://shields.io/), which will show the price of steam in tl.
- the steam API is ``https://store.steampowered.com/api/appdetails?appids=<id>&cc=tr&l=en``
- https://store.steampowered.com/app/921570/_/?l=japanese
#### Input
#### Output
### \# Alternatives
- `<iframe>` 嵌入笔记 via [How to embed a Steam store page in a post? - Site Feedback - Chrono.gg Community](https://community.chrono.gg/t/how-to-embed-a-steam-store-page-in-a-post/15016)
  - `<iframe src="https://store.steampowered.com/widget/427520/" frameborder="0" width="646" height="190"></iframe>`
  - <iframe src="https://store.steampowered.com/widget/427520/" frameborder="0" width="646" height="190"></iframe>
### \# Notes
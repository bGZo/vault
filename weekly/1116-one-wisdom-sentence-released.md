---
title: 一句发布了
aliases: 一句发布了
created: 2023-01-01T11:27:40
modified: 2025-01-01T11:29:19
description: 
status:
  - writing/draft
tags: 
type: writing
---

<iframe src='https://one.bgzo.cc' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'/><center>via: <a href='https://one.bgzo.cc' target='_blank' class='external-link'>https://one.bgzo.cc</a></center>

<iframe src='https://blog.bgzo.cc/one-wisdom-sentence-released.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'/><center>via: <a href='https://blog.bgzo.cc/one-wisdom-sentence-released.html' target='_blank' class='external-link'>https://blog.bgzo.cc/one-wisdom-sentence-released.html</a></center>

2023 新年伊始，整理 2022 的陈年笔记时发现有很多不知名，但是又舍不得丢弃的句子，想着干脆把他们做成引用得了。连着建仓库，设计页面，写脚本一套下来也没花太多时间，一个简单的静态自动部署的网站就建好了: [One](https://one.bgzo.cc/).[^2]

![](https://unpkg.com/bgzo@23.1.1/img/one-preview.png)

## Tech stack

- Jekyll
- Github Action

## Highlights

- [x] Every single page for quote; Detail[^1] is following:

<p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="wvxWKZb" data-user="bgzo" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/bgzo/pen/wvxWKZb">
  quotes</a> by bGZo (<a href="https://codepen.io/bgzo">@bgzo</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

- [x] Generate quote by syncing Github issues with metadata;
- [x] Deploy with [Vercel](https://vercel.com)
- [x] SEO supported by plugin.
- [ ] More functions, like mobile views, share links, quote tags.
- [ ] When the quotes increasing huge, how to generate page smartly? Is possible to make a API service?[^3]

## Why
  - 有大量的引用，来不及回顾，但是又希望分享出去，我相信这是中文互联网中文用户的普遍现状，市面上也存在着大量的产品，作为树洞收集者我们的话语，这只是我的一种实现方式而已。

## How
  - V1.0 Jekyll + Github Action

## What
### \# Program Description
    - [ ] #todo #feat 无需重新构建，首页的句子也可以随机变换；
    - [ ] #todo #feat 添加分析器 [Analytics](https://analytics.google.com/analytics/web/#/a252954726p347875136/admin/changehistory/account)
    - [ ] #todo #feat 支持拷贝分享链接；
    - [ ] #todo #feat 添加标签支持
      - [File: README — Documentation for jekyll-tagging (1.1.0)](https://rubydoc.info/gems/jekyll-tagging/frames)
      - [Jekyll Tags on Github Pages · Long Qian](https://longqian.me/2017/02/09/github-jekyll-tag/)
    - [ ] #todo #pref 适配手机显示；
    - [ ] #todo #pref 当后期引用数量激增，如何保证页面流畅，稳定？[^3]
      - Jekyll 天然支持分页较差（或者我不会写查询？）

[^2]: Name inspired by https://wufazhuce.com, https://wordsofwisdom.app/;
[^1]: Page design parody for [Words of Wisdom](https://wordsofwisdom.app/);
[^3]: Jekyll is just a static website generation. Seem like impossible to deliver value from jekyll to js. More discuss via: [Jekyll - display a random chosen post in index - Stack Overflow](https://stackoverflow.com/questions/31490789);

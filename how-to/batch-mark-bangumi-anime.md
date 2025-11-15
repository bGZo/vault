---
comments: true
draft: true
aliases:
  - 如何批量标记 bangumi 往季新番
  - 如何批量标记往季新番
created: 2025-11-15T12:34:34
modified: 2025-11-15T12:44:13
tags:
  - bangumi
title: 如何批量标记 bangumi 往季新番
---

# 如何批量标记 bangumi 往季新番

本篇指南属于 https://pypi.org/project/bangumi_recovery/ 操作备忘

## 使用场景

你可能是一个多年的追番达人，突然某一天发现了 https://bangumi.tv/ 这样一个网站，你很希望拥有自己的一套收藏夹，但是可能会有如下问题：

1. 手动点格子耗时且容易出错；
2. 代理或网络不稳定会整个过程有点坐牢；

当然，你也有可能是豆瓣难民，迁移来这里，你同样面临如上问题。

## 前置准备

使用本工具你需要一些前置知识，如：

1. 会使用命令行工具（bash/zsh）
2. 已安装 Python 3.11+ 环境并能使用 pipx 或 venv
3. 在 Bangumi `next` [页面](https://next.bgm.tv/demo/access-token) 获取要目标账号的 `access_token`
4. 在 zsh shell 中设置代理与 token：

```bash
# 必填：迁移时切换为源账号
export BGM_ACCESS_TOKEN="xxx"
# 代理（如果需要）
export http_proxy="http://127.0.0.1:1080"
export https_proxy="http://127.0.0.1:1080"
# 局域网或内网地址加入 no_proxy 避免走代理
export no_proxy="localhost,127.0.0.1,::1"
```

## 开始

```bash
# 安装本项目
pipx install bangumi_recovery
# 启动后端服务
bgm-click-server
```

本地浏览器打开运行的项目，效果图如下：

![](https://raw.githack.com/bGZo/assets/dev/2025/202508021025451.png)

## Related

- [[migrate-account-bangumi-to-another|如何迁移 bangumi 账号]]
- [[delete-bangumi-timeline|如何删除清空 bangumi 时间线]]

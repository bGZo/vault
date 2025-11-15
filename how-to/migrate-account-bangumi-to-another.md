---
comments: true
draft: false
aliases:
  - 如何迁移 bangumi 账号
created: 2025-11-13T07:27:54
modified: 2025-11-15T12:42:39
tags:
  - bangumi
title: 如何迁移 bangumi 账号
type: how-to
---

# 如何迁移 bangumi 账号

本篇指南属于 https://pypi.org/project/bangumi_recovery/ 操作备忘

## 使用场景

你想把一个 Bangumi 账号的数据（收藏、评分等）迁移到另一个账号上。传统上你可能需要：

1. 新建或更换账号后想复制历史收藏
2. 陆续把播放/观看进度迁移到主账号
3. 合并旧账号数据到新账号或做横向备份

可能会很蛋疼，因为：

1. 没有一键导入：API 也没有官方的“导入”端点
2. 需要多个多个浏览器去切换账号并保证授权
3. 网络或代理不稳定时，数据抓取与写入容易失败
4. 大批量操作会触发限流，需要节流与重试机制

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

## 开始迁移

```bash
pipx install bangumi_recovery
# 在命令中填入你要迁移的用户 ID
bgm-clone user_id
```

## Related

- [[batch-mark-bangumi-anime|如何批量标记 Bangumi 往季新番]]
- [[delete-bangumi-timeline|如何删除清空 bangumi 时间线]]

---
comments: true
draft: false
aliases:
  - 如何删除清空 bangumi 时间线
created: 2025-11-15T12:24:32
modified: 2025-11-15T12:42:51
tags:
  - bangumi
title: 如何删除清空 bangumi 时间线
---

# 如何删除清空 bangumi 时间线

本篇指南属于 https://pypi.org/project/bangumi_recovery/ 操作备忘

## 使用场景

你可能基于如下场景想要删除自己的活动记录/时间线：

1. 账号被他人查看，想删除敏感活动记录。
2. 更换账号或重置状态前清理历史。
3. 定期清理时间线以维护隐私。

## 前置准备

使用本工具你需要一些前置知识，如：

1. 会使用命令行工具（bash/zsh）
2. 已安装 Python 3.11+ 环境并能使用 pipx 或 venv
3. 获取当前登录用户的 Cookie，使用 `F12` 控制台获取
4. 在 zsh shell 中设置代理与 token：

```bash
# 必填：迁移时切换为源账号
export BGM_ACCESS_COOKIE="xxx"
# 代理（如果需要）
export http_proxy="http://127.0.0.1:1080"
export https_proxy="http://127.0.0.1:1080"
# 局域网或内网地址加入 no_proxy 避免走代理
export no_proxy="localhost,127.0.0.1,::1"
```

> [!warning]
> 跟之前两篇不一样的是，本需求因为没有官方 API 支持，只能利用已登陆的用户 Cookie 进行操作

## 运行项目

```shell
# 安装项目
pipx install bangumi_recovery
# 删除目标用户的时间线
bgm-timeline-delete bool
```

## Related

- [[migrate-account-bangumi-to-another|如何迁移 bangumi 账号]]
- [[batch-mark-bangumi-anime|如何批量标记 Bangumi 往季新番]]

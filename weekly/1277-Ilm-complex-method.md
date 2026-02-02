---
title: 对 ai 的误解
aliases:
  - "20260129"
  - 对 ai 的误解
created: 2026-01-29T22:54:27
modified: 2026-01-29T23:07:54
comments: true
draft: true
description:
tags: []
tags-link:
type: writing
---

# LLM 的为碟醋，包了个饺子

我让 ai 帮我转换下 obsidian 官方模板插件语法的模板文件，要求转换为 templater 支持的 js 语法

我以为他会读取我所有短模板文件，然后一个一个替换出来，这很 silly。

有意思的来了，为了十几个文件，他直接写了 python 脚本；然后执行了一下，然后请求我删除😂

我很震撼，因为这个事情放给我我一定会人肉去核对，但 llm 不一样，他可能考虑节省上下文带宽或是什么，可以几十秒生成一段脚本做这个事情，而我不可以

又是嫉妒 llm 的一个晚上，甚至还有点点焦虑

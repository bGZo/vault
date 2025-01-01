---
aliases:
  - 用 LLM 辅助编程
title: 用 LLM 辅助编程
created: 2024-07-27T02:46:31
modified: 2024-12-29T03:28:06
description: 
tags:
  - llm
status:
  - writing/draft
type: writing
---

启发于：[Title Unavailable \| Site Unreachable](https://linux.do/t/topic/126077/7)

## Local Server

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

### Enable LAN access

```shell
# via: https://aident.ai/blog/how-to-expose-ollama-service-api-to-network
sudo systemctl edit ollama.service
```

```shell
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

Restart

```shell
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Module

- [deepseek-coder-v2:16b](https://ollama.com/library/deepseek-coder-v2:16b)


啓發於：[Title Unavailable \| Site Unreachable](https://linux.do/t/topic/126077/7)

<iframe src="https://www.youtube.com/embed/AV_8czoF3PU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=AV_8czoF3PU' target='_blank' class='external-link'>https://www.youtube.com/watch?v=AV_8czoF3PU</a></center>

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

![](https://x.com/yihong0618/status/1872635893657604391)

### Deepseek by China
- [deepseek-coder-v2:16b](https://ollama.com/library/deepseek-coder-v2:16b)

## Extension

### Continue

high CPU usage cause multi files to build index, via: https://github.com/continuedev/continue/issues/1622, https://github.com/continuedev/continue/issues/866, https://github.com/continuedev/continue/issues/778, https://utgd.net/article/20938

## References

- https://medium.com/@smfraser/how-to-use-a-local-llm-as-a-free-coding-copilot-in-vs-code-6dffc053369d

Source via: https://note.bgzo.cc/how-to/coding-with-llm
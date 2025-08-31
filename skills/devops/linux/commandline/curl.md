---
aliases:
  - Curl
created: 2024-08-11T00:00:00
description: 利用URL规则在命令行下工作的文件传输工具
modified: 2025-08-31T14:05:34
title: Curl
type: command/linux
---

# Curl

<iframe src='https://wangchujiang.com/linux-command/c/curl.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/curl.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/curl.html</a></center>

## Wget-url-not-found

- This is a common problem when working with urls as well.

```shell
  curl http://www.google.com/search?q=rails
  # => zsh: no matches found: http://www.google.com/search?q=rails
```

- However, you can escape it with a backslash or quote it.

```shell
  curl "http://www.google.com/search?q=rails"
```

- I don't know of any config to change this on a case-by-case basis (to keep the wildcard working). Do you?
- **双引网址** 即可.

## More

- [[curl-everything-curl|everything-curl]]: The book documenting the curl project, the curl tool, libcurl and more. Simply put: everything curl.

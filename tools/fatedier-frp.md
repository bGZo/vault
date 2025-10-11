---
aliases:
  - FRP
created: 2025-09-30T22:19:34
description: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.
modified: 2025-10-01T11:32:04
source: https://github.com/fatedier/frp
title: FRP
type: repo
---

# FRP

![](https://img.shields.io/github/stars/fatedier/frp?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/fatedier/frp?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/fatedier/frp?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=fatedier&repo=frp&bg_color=00000000)](https://github.com/fatedier/frp)

内网穿透项目工具

## 快速上手

下载最新版 [^download_address]，善用 `scp` 传输到远程服务器和家用主机，解压

[^download_address]: https://github.com/fatedier/frp/releases

```shell
tar -zvxf frp_0.65.0_linux_amd64.tar.gz
```

参考这里的配置 [^frp_config]，配置自启动 Service:

[^frp_config]:: https://github.com/bGZo/env/tree/main/linux/frp

```shell
sudo mv ./frpc.service /etc/systemd/system/frpc.service
sudo systemctl daemon-reload
sudo systemctl start frpc
sudo systemctl status frpc
sudo systemctl enable frpc
```

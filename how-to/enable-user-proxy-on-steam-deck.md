---
comments: true
draft: false
aliases:
  - 如何在 Steam Deck 上开启一个默认代理
created: 2025-12-08T22:28:59
modified: 2025-12-10T21:03:06
tags: []
title: 如何在 Steam Deck 上开启一个默认代理
---

# 如何在 Steam Deck 上开启一个默认代理

因为种种原因，你需要一个随时都能访问游戏社区的网络环境，这样才能查攻略，下载创意工坊，但是这里是 Steam Deck，你不能总是开手机热点做这个事情。

借鉴 [[enable-user-smb-on-steam-deck|在 Steam Deck 上开启用户级别的 SMB]] 的思路，你可以在 Linux 上开启用户级别的自启动进程，创建配置 `/home/deck/.config/systemd/user/clash.service` 如下：

```shell
[Unit]
Description=You know.
After=network.target

[Service]
Type=simple
Restart=on-failure
ExecStart=/home/deck/proxy/clash-linux-amd64 -d /home/deck/proxy/

[Install]
WantedBy=default.target
```

然后设置开启启动：

```shell
systemctl --user daemon-reload
systemctl --user enable clash
systemctl --user status clash
```

然后在 Steam Deck 上的网络设置里面设置永久的代理地址，即可。

## 参考

https://github.com/Sitoi/SystemdClash

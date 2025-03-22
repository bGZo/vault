---
title: docker
created: 2024-05-24T00:08:44
modified: 2025-03-16T00:26:26
description: 
tags: 
type:
---

## Why

### 开箱即用
### 环境隔离

## [[proxy]]

```shell
# user (works)
mkdir -p ~/.docker
vim ~/.docker/config.json
# sudo
sudo vim /etc/docker/daemon.json
'''
{
  "proxies": {
    "http-proxy": "http://proxy.example.com:3128",
    "https-proxy": "https://proxy.example.com:3129",
    "no-proxy": "*.test.example.com,.example.org,127.0.0.0/8"
  }
}
'''
# registry-mirrors has died in China...
# consider https://blog.csdn.net/NTD_huachen/article/details/141858177
    # https://docker.mirrors.ustc.edu.cn
    # https://ustc-edu-cn.mirror.aliyuncs.com
# systemd environment (ignored)
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo echo "[Service]\nEnvironment='HTTP_PROXY=http://192.168.31.20:10800/'\nEnvironment='HTTPS_PROXY=http://192.168.31.20:10800/'\nEnvironment='NO_PROXY=localhost,127.0.0.1,.example.com,192.168.31.20'" > /etc/systemd/system/docker.service.d/proxy.conf
```

https://github.com/bgzo/docker

## `dockerfile` vs `docker compose`

`dockerfile` 管理**单个**容器的一步步构建应用程序的流程；

`docker compose` 管理**多个**容器之间启动与配置；

> [!note]
> `docker compose` 不可以替代 `dockerfile`，因为 >`docker compose` 总是依赖 `dockerfile` 打包好的文件。

More dockerfile via: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/, https://www.cnblogs.com/rainbowbridge/p/17852138.html

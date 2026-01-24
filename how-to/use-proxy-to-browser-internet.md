---
comments: true
draft: true
aliases:
  - 如何 科学上网
created: 2026-01-24T17:14:20
modified: 2026-01-24T17:23:04
tags: []
title: 如何 科学上网
---

# 如何 [[proxy|科学上网]]

## 核心组件与原理

科学上网的核心在于流量的转发与伪装。通常涉及以下组件：

1. **客户端 (Client):** 运行在你本地设备上，负责拦截本地网络请求。
2. **服务端 (Server):** 运行在境外服务器上，负责接收客户端转发来的请求，并向目标网站发起访问。
3. **协议 (Protocol):** 客户端与服务端之间通信的规则，如 VMess, VLESS, Trojan, Shadowsocks 等。旨在加密数据并伪装成正常流量（如 HTTPS）。

我们这里主要关注**核心 (Core)** 程序，而非图形化界面 (GUI) 客户端，好处有：

1. **理解本质:** 明白分流是在本地通过查表 (Table Lookup) 完成的。
2. **极致轻量:** 没有 Electron 的内存占用。
3. **全平台通用:** 无论是路由器 (OpenWrt)、Linux 服务器还是 Mac/Win，配置文件是通用的。

常见的核心程序有：

- **Xray-core (Project X):** 目前最流行、功能最强大的核心之一，是 V2Ray 的超集。支持 VLESS, VMess, Trojan, Shadowsocks 等多种协议，性能优异。
- **Sing-box:** 新兴的全能型代理平台，配置灵活，性能极高，支持多种协议，正逐渐成为主流。
- **Clash (Premium/Meta):** 虽然 Clash 删库风波不断，但 Clash.Meta (即 Mihomo) 内核依然非常活跃，以其强大的规则分流能力著称。

### 原理简述

1. **Socks5/HTTP 代理:** 核心程序在本地开启一个 Socks5 或 HTTP 端口（例如 1080）。
2. **流量接管:** 你可以通过操作系统设置或浏览器插件（如 SwitchyOmega），将网络流量指向这个本地端口。进阶玩法通过 TUN/TAP 虚拟网卡接管系统所有流量。
3. **路由与分流:** 核心程序根据预定义的**规则 (Rule)**，判断请求的目标地址。
    - 如果是国内地址 (GeoCN)，直接直连 (Direct)。
    - 如果是国外地址，加密封装后发送给境外服务器 (Proxy)。
    - 如果是广告地址，直接丢弃 (Reject)。

## 基础配置流程 (以 Xray-core 为例)

这里演示最纯粹的命令行配置方式，帮助理解底层逻辑。

### 1. 下载核心

前往 GitHub Releases 页面下载对应系统架构的二进制文件。

- Xray-core: https://github.com/XTLS/Xray-core/releases

解压后，你主要关注 `xray` (可执行文件) 和 `config.json` (配置文件)。

### 2. 编写/修改配置文件 (config.json)

一个典型且极简的客户端配置结构如下：

```json
{
  "inbounds": [
    {
      "port": 1080, // 本地监听端口
      "protocol": "socks", // 入站协议，本地应用通过 Socks5 连接这里
      "settings": {
        "auth": "noauth"
      },
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vless", // 出站协议，连接远端服务器
      "settings": {
        "vnext": [
          {
            "address": "your.server.ip", // 你的服务器 IP
            "port": 443,
            "users": [
              {
                "id": "your-uuid-string", // 你的 UUID
                "encryption": "none",
                "flow": "xtls-rprx-vision"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality", // 使用 Reality 协议伪装
        "realitySettings": {
          "fingerprint": "chrome",
          "serverName": "www.microsoft.com", // 偷取的域名
          "publicKey": "your-public-key",
          "shortId": "your-short-id"
        }
      },
      "tag": "proxy"
    },
    {
      "protocol": "freedom", // 直连协议
      "tag": "direct"
    },
    {
      "protocol": "blackhole", // 丢弃协议（用于拦截广告）
      "tag": "block"
    }
  ],
  "routing": {
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {
        "type": "field",
        "ip": ["geoip:private", "geoip:cn"], // 局域网和中国 IP
        "outboundTag": "direct" // 走直连
      },
      {
        "type": "field",
        "domain": ["geosite:cn"], // 中国域名
        "outboundTag": "direct" // 走直连
      }
    ]
  }
}
```

### 3. 理解 GeoIP 和 GeoSite

在上面的配置中，`routing` 模块决定了流量去哪里。这里用到了 `geoip.dat` 和 `geosite.dat` 两个核心资源文件。

- **GeoIP (geoip.dat):** 这是一个二进制文件，里面存储了全球 IP 地址段的归属地信息。
    - `geoip:cn` 表示所有中国大陆的 IP 地址段。
    - 原理：当核心程序拿到一个目标 IP 时，会在这个数据库里查找。如果在 `cn` 列表中，就命中规则。
- **GeoSite (geosite.dat):** 存储了域名列表，按类别分组。
    - `geosite:cn` 包含了常见的大陆网站域名（百度、淘宝、腾讯等）。
    - `geosite:google` 包含了 Google 旗下所有域名。
    - `geosite:category-ads-all` 包含了常见的广告域名。

**配置与更新流程：**

1. **获取文件:** 这两个文件通常随核心程序一起发布，或者可以在 `https://github.com/v2fly/domain-list-community` 和 `https://github.com/v2fly/geoip` 下载增强版。
2. **放置位置:** 将 `geoip.dat` 和 `geosite.dat` 放在 `xray` 可执行文件的同一目录下（或通过环境变量 `XRAY_LOCATION_ASSET` 指定）。
3. **路由匹配逻辑:**
    - 当浏览器发起请求 `www.baidu.com`。
    - Xray 嗅探到域名。
    - 检查 `routing.rules`。发现 `geosite:cn` 规则匹配，`outboundTag` 是 `direct`。
    - 流量交给 `tag: direct` 的 `outbound` 处理 -> `protocol: freedom` -> 直连访问百度（不消耗服务器流量，速度快）。
    - 如果访问 `www.google.com`，不匹配 `cn` 规则，默认走第一条 `outbound` (或者配置兜底规则)，即 `proxy` -> 加密发送给服务器。

## 进阶：运行与维护

1. **启动命令:** `./xray -c config.json`
2. **系统代理:** 此时你的电脑开了个 1080 端口，但系统流量不会自动走这里。你需要：
    - **手动设置:** 系统偏好设置 -> 网络 -> 代理，填入 127.0.0.1 和 1080。
    - **浏览器插件:** Chrome 安装 SwitchyOmega，新建情景模式指向 Socks5 127.0.0.1:1080。
    - **TUN 模式 (高级):** 通过配置 Xray 的入站为 TUN 模式，创建虚拟网卡，强制接管操作系统所有层级的流量（适合终端、游戏等不走系统代理的软件）。

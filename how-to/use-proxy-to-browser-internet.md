---
comments: true
draft: false
aliases:
  - 如何 科学上网
created: 2026-01-24T17:14:20
modified: 2026-01-24T19:47:32
tags:
  - flamewar
title: 如何 科学上网
---

# 如何 [[proxy|科学上网]]

## 核心组件与原理

科学上网的核心在于流量的转发与伪装。通常涉及以下组件：

1. 客户端 (Client): 运行在你本地设备上，负责拦截本地网络请求。
2. 服务端 (Server): 运行在境外服务器上，负责接收客户端转发来的请求，并向目标网站发起访问。
3. 协议 (Protocol): 客户端与服务端之间通信的规则，如 VMess, VLESS, Trojan, Shadowsocks 等。旨在加密数据并伪装成正常流量（如 HTTPS）。

我们这里主要关注核心 (Core) 程序，而非图形化界面 (GUI) 客户端，好处有：

1. 理解本质: 明白分流是在本地通过查表 (Table Lookup) 完成的。
2. 极致轻量: 没有 Electron 的内存占用。
3. 全平台通用: 无论是路由器 (OpenWrt)、Linux 服务器还是 Mac/Win，配置文件是通用的。

常见的核心程序有：

- Xray-core (Project X): 目前最流行、功能最强大的核心之一，是 V2Ray 的超集。支持 VLESS, VMess, Trojan, Shadowsocks 等多种协议，性能优异。
- Sing-box: 新兴的全能型代理平台，配置灵活，性能极高，支持多种协议，正逐渐成为主流。
- Clash (Premium/Meta): 虽然 Clash 删库风波不断，但 Clash.Meta (即 Mihomo) 内核依然非常活跃，以其强大的规则分流能力著称。

### 原理简述

1. Socks5/HTTP 代理: 核心程序在本地开启一个 Socks5 或 HTTP 端口（例如 1080）。
2. 流量接管: 你可以通过操作系统设置或浏览器插件（如 SwitchyOmega），将网络流量指向这个本地端口。进阶玩法通过 TUN/TAP 虚拟网卡接管系统所有流量。
3. 路由与分流: 核心程序根据预定义的规则 (Rule)，判断请求的目标地址。
    - 如果是国内地址 (GeoCN)，直接直连 (Direct)。
    - 如果是国外地址，加密封装后发送给境外服务器 (Proxy)。
    - 如果是广告地址，直接丢弃 (Reject)。

## 基础配置流程

本节演示三种主流内核的最纯粹命令行配置方式。

### 1. Xray-core

特点: V2Ray 的超集，功能最全面，适合服务器和客户端通用。

#### 1. 下载与运行

- 下载: [GitHub Releases](https://github.com/XTLS/Xray-core/releases)
- 运行: `./xray -c config.json`

#### 2. 配置文件详解 (config.json)

```json
{
  // 入站连接：接收本地的流量
  "inbounds": [
    {
      "port": 1080,          // 本地监听端口
      "protocol": "socks",   // 协议类型，通常使用 socks 或 http
      "settings": { "auth": "noauth" },
      "sniffing": {          // 流量嗅探，用于从流量中提取域名，这就让路由可以根据域名分流
        "enabled": true,
        "destOverride": ["http", "tls"]
      }
    }
  ],
  // 出站连接：将流量发送到哪里
  "outbounds": [
    {
      "tag": "proxy",       // 标签，供路由规则引用
      "protocol": "vless",  // 核心代理协议
      "settings": {
        "vnext": [
          {
            "address": "your.server.ip", 
            "port": 443,
            "users": [
              {
                "id": "your-uuid",
                "encryption": "none",
                "flow": "xtls-rprx-vision" // XTLS Vision 流控，防探测能力强
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality", // Reality 伪装，目前最先进的防封锁技术
        "realitySettings": {
          "fingerprint": "chrome",
          "serverName": "www.microsoft.com", // 伪装的目标域名
          "publicKey": "your-public-key",    // 服务器生成的公钥
          "shortId": "your-short-id"
        }
      }
    },
    { "tag": "direct", "protocol": "freedom" },   // 直连出站
    { "tag": "block", "protocol": "blackhole" }   // 阻断出站
  ],
  // 路由规则：决定流量走哪个出站
  "routing": {
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {
        "type": "field",
        "ip": ["geoip:cn", "geoip:private"], // 匹配中国IP和局域网IP
        "outboundTag": "direct"              // 走 direct 出站
      },
      {
        "type": "field",
        "domain": ["geosite:cn"],            // 匹配中国域名
        "outboundTag": "direct"
      }
    ]
  }
}
```

### 2. Sing-box

特点: 新一代通用代理平台，性能极高，配置结构现代化，支持 Tun 模式极佳。

#### 1. 下载与运行

- 下载: [GitHub Releases](https://github.com/SagerNet/sing-box/releases)
- 运行: `./sing-box run -c config.json`

#### 2. 配置文件详解 (config.json)

Sing-box 采用了更现代的 JSON 结构，字段命名更加直观。

```json
{
  "log": { "level": "info", "timestamp": true },
  "inbounds": [
    {
      "type": "socks",        // 入站类型
      "tag": "socks-in",
      "listen": "127.0.0.1",
      "listen_port": 1080
    }
  ],
  "outbounds": [
    {
      "type": "vless",        // 出站类型
      "tag": "proxy",
      "server": "your.server.ip",
      "server_port": 443,
      "uuid": "your-uuid",
      "flow": "xtls-rprx-vision",
      "tls": {
        "enabled": true,
        "server_name": "www.microsoft.com",
        "reality": {
          "enabled": true,
          "public_key": "your-public-key",
          "short_id": "your-short-id"
        }
      }
    },
    { "type": "direct", "tag": "direct" },
    { "type": "block", "tag": "block" }
  ],
  "route": {
    "rules": [
      {
        "geoip": "cn",        // 极简的规则写法
        "outbound": "direct"
      },
      {
        "geosite": "cn",
        "outbound": "direct"
      }
    ],
    // 必须下载 sing-geoip.db 和 sing-geosite.db 才能生效
    "geoip": { "path": "geoip.db" },
    "geosite": { "path": "geosite.db" }
  }
}
```

### 3. Clash.Meta (Mihomo)

特点: 规则分流 (Rule-based) 的鼻祖体系的继承者，配置文件使用 YAML 格式，对用户非常友好，拥有强大的策略组功能。

#### 1. 下载与运行

- 下载: [GitHub Releases](https://github.com/MetaCubeX/mihomo/releases)
- 运行: `./mihomo -f config.yaml`

#### 2. 配置文件详解 (config.yaml)

YAML 格式通过缩进表示层级，注意缩进。

```yaml
port: 7890               # HTTP 代理端口
socks-port: 7891         # SOCKS5 代理端口
allow-lan: false         # 是否允许局域网连接
mode: rule               # 模式：rule(规则), global(全局), direct(直连)
log-level: info

# 代理节点定义
proxies:
  - name: "MyServer"
    type: vless
    server: your.server.ip
    port: 443
    uuid: your-uuid
    network: tcp
    tls: true
    udp: true
    flow: xtls-rprx-vision
    servername: www.microsoft.com
    client-fingerprint: chrome
    reality-opts:
      public-key: your-public-key
      short-id: your-short-id

# 策略组：将节点分组，方便手动切换或自动测速
proxy-groups:
  - name: "Proxy"        # 组名
    type: select         # 类型：select(手动选择), url-test(自动测速选择)
    proxies:
      - "MyServer"       # 包含的节点

# 路由规则
rules:
  # 格式: 类型,参数,策略组/节点
  - GEOSITE,cn,DIRECT    # 中国域名走直连
  - GEOIP,cn,DIRECT      # 中国IP走直连
  - MATCH,Proxy          # 剩下的所有流量走 Proxy 组
```

## 进阶：运行与维护

1. 系统代理设置:
    - 上述配置启动后，只是在本地开启了端口（如 1080 或 7890）。
    - 手动设置: 系统设置 -> 网络 -> 代理，填入 127.0.0.1 和对应端口。
    - 浏览器插件: 推荐 SwitchyOmega (Chrome/Edge)，配置 Proxy 情景模式指向对应端口。

2. TUN 模式 (Transparent Proxy):
    - 原理：创建虚拟网卡，接管系统网络层流量。可以让终端、Git、游戏等不遵循 HTTP_PROXY 环境变量的软件强制走代理。
    - 配置：Clash 和 Sing-box 对 TUN 支持极好，只需在配置中添加 `tun` 字段即可开启。Xray 相对复杂。

## 附录：核心概念与资源

### 路由与分流资源 (GeoIP/GeoSite)

核心程序能够智能分流的关键在于两个数据库文件。

- GeoIP (geoip.dat / geoip.db): IP 地址库。
    - 作用: 存储了全球 IP 地址与地理位置的映射。
    - key: `geoip:cn` (中国大陆 IP), `geoip:private` (局域网 IP)。
    - 原理: 当你访问一个 IP 时，内核查表，如果发现是 CN IP，就按配置走 Direct 出站。
- GeoSite (geosite.dat / geosite.db): 域名库。
    - 作用: 存储了大量域名列表，按类别分组。
    - key: `geosite:cn` (国内常见网站), `geosite:google` (谷歌全家桶), `geosite:category-ads-all` (广告域名)。
    - 更新: 这些文件需要定期更新以保持准确。

### 概念映射表

| 概念 | Xray / V2Ray | Sing-box | Clash / Mihomo |
| :--- | :--- | :--- | :--- |
| 入站 | `inbounds` | `inbounds` | 顶层字段 (`port`, `socks-port`) |
| 出站/节点 | `outbounds` | `outbounds` | `proxies` |
| 分流规则 | `routing` | `route` | `rules` |
| 策略组 | (通过复杂路由实现) | (selector outbound) | `proxy-groups` |
| 透明代理 | 复杂配置 | `tun` inbound | `tun` 字段 |

### 用过以及未来可能用的服务

打勾的是已经跑路或者不用的，真假自辨，如果需要邀请码请写邮件问我要：

- [x] 速鹰云 https://sy168.site
- [x] 速蛙云 https://suwayun.com
- [ ] 跑路云 https://paoluz.link
- [ ] 八戒 https://bajie.pw
- [ ] https://cshjc.top


---
aliases:
  - Web API
created: 2024-08-02T00:00:00
modified: 2025-08-31T10:43:03
title: Web API
wikipedia: https://en.wikipedia.org/wiki/Web_API
---

# Web API

Web 服务器或 Web 浏览器的 API (web 类型的 API)

## Why

## How

## What

- Client side 客户端
- Server side 服务器端
    - Endpoints 端点 => 组成 Web APIs 的最小单位
        - Webhook 是用 URI 作为触发器，本地客户端请求，远程服务器执行回调，提供一种点对点 IPC；
    - Resources versus services 资源与服务
        - Web 2.0 Web API 通常使用基于机器的交互，例如 REST 和 SOAP 。
            - RESTful Web API 使用 HTTP 方法通过 URL 编码的参数访问资源，并使用 JSON 或 XML 传输数据。
            - SOAP 协议由 W3C 标准化，并强制使用 XML 作为有效负载格式，通常通过 HTTP 进行。
                - 此外，基于 SOAP 的 Web API 通过利用 WSDL 文档提供的 XML 模式，使用 XML 验证来确保结构消息的完整性。 WSDL 文档准确地定义了 Web 服务的 XML 消息和传输绑定。
- Example 例子
    - https://api.nasa.gov/planetary/apod

## References

![[image_1668337528771_0.png]]

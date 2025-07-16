---
aliases:
  - 统一资源名称
  - Urn
created: 2024-07-13T00:00:00
description: 与 URL 不同，URN 不提供任何关于如何定位资源的信息；它只是标识它，就像一个纯 URI 一样。具体来说，URN 是一种带有 "urn" 方案的 URI
modified: 2025-07-16T21:08:39
title: Urn
---

# Urn

## Why

## How

## What

### 组成结构？

其结构如 [RFC 2141](https://datatracker.ietf.org/doc/html/rfc2141) 中所述：

`<URN>:<NID>:<NSS>`

- **URN:** 通常为 `urn`。
- **命名空间标识符（ NID ）：** 代表一个唯一的命名空间或标识符系统，定义和管理 URN 。它提供上下文，并确保标识符的唯一性。命名空间的例子包括 ISBN （国际标准书号）等。
- **命名空间特定字符串（ NSS ）：** 它是一个字符串，唯一地在指定的命名空间内标识一个资源。标识符本身并不传达任何关于资源位置或访问方法的信息。

例如，一本非常著名的介绍计算机系统的书 [CS: APP](https://www.isbns.net/isbn/9780134092669/) 的 ISBN 号表示为 URN `urn:isbn:9780134092669`。

URN 经常用于各种标准协议中，如 SAML 协议中的断言，对应于 URN `urn:oasis:names:tc:SAML:2.0:assertion`。

在软件工程中，我们也可以根据 URN 命名规则为我们自己的系统中的特定目的定义 URN 。例如，在 Logto 中，要启用 Organization ，你需要在使用 SDK 时在配置中添加 `urn:logto:scope:organizations` 这个 scope 。每个 Organization 也有自己的专用 URN `urn:logto:organization:{orgId}`。

via: https://www.v2ex.com/t/1050461

---
title: mybatis
aliases:
  - mybatis
created: 2025-03-16T00:29:20
modified: 2025-03-16T00:40:15
description: MyBatis is a first class persistence framework with support for custom SQL, stored procedures and advanced mappings. MyBatis eliminates almost all of the JDBC code and manual setting of parameters and retrieval of results. MyBatis can use simple XML or Annotations for configuration and map primitives, Map interfaces and Java POJOs (Plain Old Java Objects) to database records.
tags: 
type: 
source: https://mybatis.org/mybatis-3/
---

## Why

## How

### 分页

#### 逻辑分页（假分页）

在内存中分页，利用 RowBounds 限制返回数据，在用到的时候再回 DB 滚动查询

#### 物理分页

```sql
select *
from table
where true
limit 20 offset 10
```

现有框架：

- [[pagehelper-Mybatis-PageHelper|Mybatis-PageHelper]]
- [[baomidou-mybatis-plus|mybatis-plus]]
    - 前身 [[Lawnstein-TkMyBatis|TkMyBatis]]

### Mybatis 拦截器

拦截到 `select` 语句, 动态拼接分页的关键字

## What

## References

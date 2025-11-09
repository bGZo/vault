---
draft: true
aliases:
  - postgresql Vs mysql
  - Postgresql-vs-mysql
created: 2024-08-17T00:00:00
modified: 2025-07-19T12:25:23
tags:
  - mysql
  - postgresql
title: postgresql Vs mysql
---
# [[postgresql]] Vs [[mysql]]

## Fuck Mysql

  - 数据类型不丰富
    - **PG** 数据类型丰富
  - 没有序列 (Sequence) 的概念
    - 场景
	    - 主键自增用 auto increase
    - **PG** 有序列的概念
  - 支持的插件不多
    - **PG** 插件特别丰富
  - 性能优化监控工具不多，定位问题的成本高
  - 官方不支持主从复制策略，同步难以解决
    - **PG** 支持主从复制的同步操作，可以实现数据的 0 丢失
  - 开源不够彻底
  - 连接不够丰富
    - MySQL 循环嵌套，8.0 才开始支持 Hash 嵌套；
    - Postgresql 连接丰富；

> [!note]
  > PostgreSQL 的 MVCC 实现和 MySQL 不大一样。PostgreSQL 一行数据会存储多个版本。最多可以存储 40 亿个事务版本。

## Reference

### [[~postgresql修炼之道|PostgreSQL修炼之道：从小工到专家]]

| |**MySQL**| **PostgreSQL**|
|--|--|--|
|**查询**|复杂 SQL 支持弱 | 所有主流的多表连接查询的方式 |
|**性能优化**<br>**度量信息**| 弱 | 强|
|**在线操作**|差|弱|
|**复制逻辑**|异步/半同步|同步|
|**插件扩展**|弱|强|

- [彦祖们， pg 还是 mysql? 到底该怎么选？ - V2EX](https://v2ex.com/t/800592)
	- [[~MySQL-MySQL-Restrictions-and-Limitations-12-Limits-in-MySQL]]
	- [[~PostgreSQL-Limits]]

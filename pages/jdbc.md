---
aliases:
  - Jdbc
  - java database connectivity
created: 2025-03-30T20:57:19
description: a Java API that allows Java programs to connect and execute queries with various databases； a part of JavaSE (Java Standard Edition) and it consists of a set of interfaces and classes written in the Java programming language. JDBC provides a standard abstraction for Java applications to communicate with different database management systems
modified: 2025-08-30T17:03:39
tags:
  - api
  - javase
title: Jdbc
---

# Jdbc

## 流程

  - 通过 IoC 容器创建并管理一个全局 `DataSource` 实例，表示数据库连接池；
  - 在需要读写数据库的方法内部，按如下步骤访问数据库：
    - 从全局 `DataSource` 实例获取 `Connection` 实例；
    - 通过 `Connection` 实例创建 `PreparedStatement` 实例；
      - 查询语句，则通过 `ResultSet` 读取结果集
      - 修改语句，则获得 `int` 结果
  - Spring 提供了一个 `JdbcTemplate`，可以方便地让我们操作 JDBC，因此，通常情况下，我们会实例化一个 `JdbcTemplate`
  - 关键
    - `try ... finally` 释放资源
      - 涉及到事务的代码需要正确提交或回滚事务

## Compare

### Execute vs executeUpdate, executeQuery [^EXE_UPDATE_QUERY]

```java
ResultSet executeQuery(String sql);
// Executes the given SQL statement, which returns a single ResultSet object.
int executeUpdate(String sql);
// Executes the given SQL statement, which may be an INSERT, UPDATE, or DELETE statement or an SQL statement that returns nothing, such as an SQL DDL statement.
boolean execute(String sql);
// Executes the given SQL statement, which may return multiple results.
via: https://docs.oracle.com/javase/8/docs/api/java/sql/Statement.html
```

### Statement vs PreparedStatement [^PRE_VS_STATE]

| **AA** | **Statement**                                                                           | **PreparedStatement**                                                                        |
| ------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **1**  | Used for executing simple SQL statements like CRUD (create, retrieve, update and delete | Used for executing dynamic and pre-compiled SQL statements                                   |
| **2**  | Statement interface cannot accept parameters at run time.                               | PreparedStatement interface accepts input parameters at runtime.                             |
| **3**  | Statement is slower as compared to Prepared Statement                                   | PreparedStatement is faster because it is used for executing pre-compiled SQL statement      |
| **4**  | Statement is suitable for executing DDL commands – CREATE, drop, alter and truncate     | PreparedStatement is suitable for executing DML commands – SELECT, INSERT, UPDATE and DELETE |
| **5**  | It is a base Interface.                                                                 | It is Extends statement interface.                                                           |
| **6**  | Statement can not use for reading binary data.                                          | PreparedStatement used for reading binary data.                                              |
| **7**  | Statement is static                                                                     | PreparedStatement is dynamic.                                                                |
| **8**  | Statement is usually parsed and executed each time.                                     | PreparedStatement is parsed once and executed with different parameters repeatedly.          |
| **9**  | Statement verifies metadata against database every time.                                | PreparedStatement verifies metadata against the database only once.                          |

## Reference

[^EXE_UPDATE_QUERY]: via: [execute,executeUpdate和executeQuery的区别与理解_CCblibo的博客-CSDN博客_executequery什么意思](https://blog.csdn.net/qq_43266465/article/details/102788581)
[^PRE_VS_STATE]: via: [Difference between Statement and PreparedStatement(Comparison Chart)](https://alldifferences.net/difference-between-statement-and-preparedstatement/)

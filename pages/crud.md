---
aliases:
  - CRUD
  - CURD
created: 2025-01-12T11:07:06
modified: 2025-07-19T10:34:01
title: CURD
wikipedia: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete#RESTful_APIs
---

# CURD

> 英文小写的 crud，是指渣滓、水垢、腐蚀污泥

## Create, Read, Update, and Delete, 增删查改 (CRUD)

  - basic operations of persistent storage
  - also sometimes used to describe user interface conventions that facilitate viewing, searching, and changing information using computer-based forms and reports.

| 中文 | 英文 | 意思 | SQL | HTTP | 表现层状态转换 | 资料分散服务 | MongoDB|
| :--: | :----: | :--: | :------------------------------------------------: | :----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------: |
| 增加 | Create | 创建 | INSERT | PUT / POST | POST | WRITE | Insert |
| 删除 | Delete | 删除 | DELETE | DELETE | DELETE | DISPOSE | Remove |
| 查询 | Read | 读取 | SELECT | GET | GET | READ / TAKE | Find |
| 改正 | Update | 更新 | UPDATE | PUT / POST / PATCH | PUT | WRITE | Update |

## 其他变体

- BREADS（也译作：面包）
    - 浏览（Browse）、读取（Read）、编辑（Edit）、创建（Add）、删除（Delete）、搜索（Search）
- ICRUD
	- 索引（Index）、创建（Create）、读取（Read）、更新（Update）、删除（Delete）
- CRAP（也译作：垃圾）
	- 创建（Create）、复制（Replicate）、写入（Append）、处理（Process）
- DAVE
	- 删除（Delete）、创建（Add）、查看（View）、更新（Edit）
- ABCD
	- 创建（Add）、浏览（Browse）、更新（Change）、删除（Delete）
- ACID（也译作：盐酸， 注意这里和保证数据库可靠性的 ACID 不是一回事）
	- 创建（Add）、更新（Change）、查询（Inquire）、删除（Delete）

## [[rest]]ful APIs

The POST method, on the other hand, is a process operation that has target-resource-specific semantics which typically exceed the scope of CRUD operations.

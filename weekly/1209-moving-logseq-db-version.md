---
title: '#1209 迁移 Logseq 数据库版本'
aliases: 迁移 Logseq 数据库版本
created: 2024-10-26T12:00:00
modified: 2024-12-26T09:04:03
status: writing/draft
type: writing
---

Logseq DB 宣布完成已经有两个月的时间了 [^logseq-db-done]。因为还在早期测试阶段，这个去年起草的 PR 一直处在草稿状态。

 <iframe src='https://github.com/logseq/logseq/pull/9858' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'/><center>via: <a href='https://github.com/logseq/logseq/pull/9858' target='_blank' class='external-link'>https://github.com/logseq/logseq/pull/9858</a></center>

数据库版本的诸多新特性，如文章目录、更快的全局搜索、更多的变量类型，高数据量、大页面的性能问题可能被解决，这些当然值得期待，但弊端和新挑战也非常多，比如 Markdown 文件与数据库的同步，如何兼容旧版本的诸多特性（相当于用 DB 重新把以前的功能实现一遍），这光是想想就令人头大。

## 遇到的问题
  - **Properties**: like `icon`, `created`, `file`, `file-path`, `hl-stamp` would be ignored.
  - **Syntax**: org mode, like `<`, would be abandoned.
  - **Value of property**: cannot be macro data.
  - **PDF annotate**: `edn` file would be ignored as well.
  - Others
    - too long assets name with `%xxx`

[^logseq-db-done]: https://discuss.logseq.com/t/why-the-database-version-and-how-its-going/26744, https://discuss.logseq.com/t/its-hard-to-migrate-to-the-logseq-db-version-for-logseq-md-users-logically-speaking-about-the-new-tag-feature-and-removed-namespace/28558

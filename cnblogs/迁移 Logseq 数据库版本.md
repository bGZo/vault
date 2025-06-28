Logseq DB 宣佈完成已經有兩個月的時間了 [^logseq-db-done]。因爲還在早期測試階段，這個去年起草的 PR 一直處在草稿狀態。

 <iframe src='https://github.com/logseq/logseq/pull/9858' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://github.com/logseq/logseq/pull/9858' target='_blank' class='external-link'>https://github.com/logseq/logseq/pull/9858</a></center>

數據庫版本的諸多新特性，如文章目錄、更快的全局搜索、更多的變量類型，高數據量、大頁面的性能問題可能被解決，這些當然值得期待，但弊端和新挑戰也非常多，比如 Markdown 文件與數據庫的同步，如何兼容舊版本的諸多特性（相當於用 DB 重新把以前的功能實現一遍），這光是想想就令人頭大。

## 遇到的問題
  - **Properties**: like `icon`, `created`, `file`, `file-path`, `hl-stamp` would be ignored.
  - **Syntax**: org mode, like `<`, would be abandoned.
  - **Value of property**: cannot be macro data.
  - **PDF annotate**: `edn` file would be ignored as well.
  - Others
    - too long assets name with `%xxx`

[^logseq-db-done]: https://discuss.logseq.com/t/why-the-database-version-and-how-its-going/26744, https://discuss.logseq.com/t/its-hard-to-migrate-to-the-logseq-db-version-for-logseq-md-users-logically-speaking-about-the-new-tag-feature-and-removed-namespace/28558
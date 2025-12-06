---
comments: true
draft: false
aliases:
  - 如何把你的.git 分离出 OneDrive/iCloud
  - How to separate your git directory from onedrive and icloud
created: 2025-11-30T10:20:59
modified: 2025-11-30T10:34:14
tags: []
title: 如何把你的.git 分离出 OneDrive/iCloud
type: how-to
---

# 如何把你的.git 分离出 OneDrive/iCloud

为什么这么做呢？

云同步固然方便，可以让你在任何设备中随时开展工作，但这不是网盘发明的目的，也会带来额外的性能开销，增加设备发热和网络带宽流量。

一个比较好的解决方案就是，保留你本地的副本，你依然可以在各个设备上开展工作，但是你的 git 目录需要存在本地的某个目录，Git 本身给了很好分离支持，如 `--git-dir`[^git-dir]。

[^git-dir]: https://git-scm.com/docs/git

那么接下来的问题就是如何把当前正常的 Git 项目中的 `.git` 目录拆分出去，我们一点点来：

```shell
# 1. 创建分离的 Git 目录，统一存放未来的 git 仓库数据
mkdir ~/workspaces/separate-git-dir/

# 2. 进入网盘挂载点，并把git 目录移动出去
cd ` ~/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian`
mv /.git ~/workspaces/separate-git-dir/obsidian.git

# 3. 编辑 git 文件
vim .git
```

将移动后的路径写进去，比如

```shell
gitdir: /Users/bgzo/workspaces/separate-git-dir/obsidian.git
```

需要注意冒号后面必须有空格，然后刷新你的编辑器，你的版本控制也就正常了，并且 git 的文件不会被网盘同步。

> 当然仍然有个问题，unix 和 windows 的目录构造不一样，就像我示例写的，unix 当然可以通用，但是到了 windows 就是另外一副模样了。需要注意

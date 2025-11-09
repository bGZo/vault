---
draft: true
aliases:
  - Diff-everything
  - How to diff everything
created: 2025-07-01T21:04:56
modified: 2025-07-16T20:27:10
title: How to diff everything
---
# How to diff everything

## Text

### Online

#### [[technikhil314-offline-diff-viewer|offline-diff-viewer]]

<iframe src='https://diffviewer.vercel.app/v2' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://diffviewer.vercel.app/v2' target='_blank' class='external-link'>https://diffviewer.vercel.app/v2</a></center>

<iframe src='https://www.diffchecker.com/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.diffchecker.com/' target='_blank' class='external-link'>https://www.diffchecker.com/</a></center>

## Directories

比较两个目录的文件区别, 不 Care 内容

```shell
diff -rq dir1 dir2
```

比较两个目录的文件区别, Care 内容

```shell
diff -r dir1 dir2
```

## Photos Meta

## Video meta

```shell
diff -u --color <(mediainfo --fullscan wbgm08.mp4) <(mediainfo --fullscan default.mp4)
```

- `-u`
	- Git 比对

```shell
sudo apt install colordiff
diff -u <(mediainfo --fullscan old.mp4) <(mediainfo --fullscan new.mp4) | colordiff
colordiff <(mediainfo --fullscan old.mp4) <(mediainfo --fullscan new.mp4)
```

- 着色 using [colordiff](https://www.colordiff.org/) on [Github](https://github.com/daveewart/colordiff)
	- It's a **wrapper** around `diff` that produces the same output as diff, except that it augments the output using colored syntax highlighting to increase readability

```bash
# alias in .zshrc, remember install colordiff
alias diff=colordiff
```

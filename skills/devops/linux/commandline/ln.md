---
draft: true
created: 2024-08-11
description: 用来为文件创建链接
type: command/linux
---
<iframe src='https://wangchujiang.com/linux-command/c/ln.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/ln.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/ln.html</a></center>

On [[windows]] its called [[mklink]]
hard link
```shell
# ln <源文件路径> <链接路径>
ln recipes.txt newrecipes.txt
```
soft link
```shell
# ln -s <源文件路径> <链接路径>
ln -s recipes.txt newrecipes.txt
```

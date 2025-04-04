---
created: 2024-08-11
description: 将程序以忽略挂起信号的方式运行起来
type: command/linux
---

<iframe src='https://wangchujiang.com/linux-command/c/nohup.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/nohup.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/nohup.html</a></center>
```shell
$ nohup command >out.file 2>&1 &
```
    - `1` -> 文件描述符 1, 标准输出
    - `2` -> 文件描述符 2, 标准错误输出,
    - `2>&1` -> 标准输出和错误输出合并 -> 合并到 `out.file`
    - 最后加一个 &,就表示后台运行
  - 关闭
```shell
$ ps -ef |grep 关键字  |awk '{print $2}'|xargs kill -9
```
      - `ps -ef` -> 列出所有正在运行的程序
      - `awk '{print $2}'` -> 第二列的内容, 是运行的程序 ID
      - `xargs` 传递给 `kill -9`, 也就是发给这个运行的程序一个信号,让它关闭

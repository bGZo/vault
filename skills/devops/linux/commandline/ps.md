---
created: 2024-08-11
description: 报告当前系统的进程状态
type: command/linux
---

<iframe src='https://wangchujiang.com/linux-command/c/ps.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/ps.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/ps.html</a></center>
```shell
ps ax
#  PID TTY      STAT   TIME COMMAND
#    1 ?        Sl     0:00 /init
#   10 ?        Ss     0:00 /init
#   11 ?        S      0:00 /init
#   12 pts/0    Ss     0:00 -zsh
#  476 pts/0    R+     0:00 ps ax
```
    - 1 字段
      - `PID` / 进程 ID
      - 当你想在另一个命令中引用这个进程时，比如说要杀死它，这是关键的
    - 2 字段
      - `TT`
      - 进程所使用的终端 ID
    - 3 字段
      - `STAT` 进程的状态
        - `I` 代表闲置的进程（睡眠时间超过约 20 秒）
        - `R` 代表可运行的进程
        - `S` 代表睡眠时间少于 20 秒的进程
        - `T` 代表已停止的进程
        - `U` 代表处于不间断等待中的进程
        - `Z` 代表已死亡的进程（*zombie*，即僵尸进程）
      - 如果出现一个以上的字母，那么第二个字母代表进一步的、可能非常有技术性的信息。
      - 常见的是 `+` ，它代表相应进程在终端中处于前台。而 `s` 代表相应进程是一个 [会话领头进程（session leader）](https://unix.stackexchange.com/questions/18166/what-are-session-leaders-in-ps).
    - 4 字段
      - `TIME` 则告诉我们进程已经运行了多长时间。
  - Cases
    - 列出所有用户的进程, 不显示终端发起的进程
```shell
ps axww
```
        - `a` 参数用来同时列出其他用户的进程
        - `x` 显示那些未与终端相连的进程（不是由用户通过终端发起的）。
        - soft-wrap 我们需要输入 `w` 两次来应用这个设置

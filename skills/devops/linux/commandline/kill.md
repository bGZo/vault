---
draft: true
created: 2024-08-11
description: 发送信号到进程
type: command/linux
---
<iframe src='https://wangchujiang.com/linux-command/c/kill.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/kill.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/kill.html</a></center>
  - Other commnad: `killall`
  - Linux 进程可以接收信号并做出反应, 这是我们与运行中进程打交道的一种方式
  - 它不只是用来终止程序的, kill 程序可以向任一程序发送多种信号
```shell
kill <PID>
# 向指定的进程 ID 发送 TERM 信号
```
  - 发送 ((b4e590b1-53d3-4c5c-986a-6c0f0d16d08d))
```shell
kill -HUP <PID>
kill -INT <PID>
kill -KILL <PID>
kill -TERM <PID>
kill -CONT <PID>
kill -STOP <PID>
```
- `HUP`
  - **hang up (挂起)**
  - 如果在终止进程之前，先关闭了启动它的终端窗口，这一信号将被自动发送
  - 数字信号 `1`
- `INT`
  - **interrupt (干扰)**
  - 这个信号和在终端中按下 `ctrl-C` 组合键的作用一样，常常用来终结进程
  - 数字信号 `2`
- `KILL`
  - 信号并不直接发送给进程，而是发送到操作系统内核，内核会让指定进程立刻停止并终结
  - 数字信号 `9`
- `TERM`
  - **terminate (终结)**
  - 这是本命令的默认信号，进程收到它会自主终结
  - 数字信号 `15`
- `CONT`
  - **continue (继续)**
  - 它可以用来恢复一个被停止的进程
  - 数字信号 `18`
- `STOP`
  - 信号并不直接发送给进程，而是发送到操作系统内核，内核会让指定进程立刻停止（但不终结）
  - 数字信号 `15`

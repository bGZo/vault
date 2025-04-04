---
created: 2024-08-11
description: 显示数据包到主机间的路径, 用于追踪数据包在网络上的传输时的全部路径，它默认发送的数据包大小是40字节
type: command/linux
---

<iframe src='https://wangchujiang.com/linux-command/c/traceroute.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/traceroute.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/traceroute.html</a></center>
```shell
traceroute <host>
```
- 通常，我们可以看到主机名、IP 地址以及一些性能指标。但并不是所有经过的路由器都会向我们返回信息，此时，`traceroute` 会输出 `* * *`。
- 每个路由器都可以看到 3 个样本，这意味着 traceroute 默认尝试了 3 次，让你很好地了解到达主机所需的时间。
- 这就是对服务器执行 `traceroute` 比简单地执行 `ping` 要花更多时间的原因。
- 你可以用 -q 参数自定义尝试的次数
```shell
traceroute -m 10 www.baidu.comD
```
- 在校园网的作用下, 每个网址输出都大同小异.
```shell
$ traceroute to www.baidu.com (39.156.66.18), 10 hops max, 60 byte packets
    1  _gateway (10.102.176.1)  28.351 ms  28.323 ms  28.299 ms
    2  10.101.1.34 (10.101.1.34)  3.229 ms 10.101.1.42 (10.101.1.42)  3.185 ms 10.101.1.34 (10.101.1.34)  3.645 ms
    3  10.101.1.1 (10.101.1.1)  2.682 ms  2.667 ms 10.101.1.25 (10.101.1.25)  2.652 ms
...
$ traceroute to www.github.com (192.30.255.113), 10 hops max, 60 byte packets
    1  _gateway (10.102.176.1)  4.295 ms  4.267 ms  4.428 ms
    2  10.101.1.42 (10.101.1.42)  8.396 ms 10.101.1.34 (10.101.1.34)  2.777 ms 10.101.1.42 (10.101.1.42)  3.607 ms
    3  10.101.1.1 (10.101.1.1)  2.356 ms 10.101.1.25 (10.101.1.25)  2.342 ms 10.101.1.1 (10.101.1.1)  2.327 ms^C
```
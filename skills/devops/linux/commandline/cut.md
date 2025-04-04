---
created: 2024-08-11
description: 连接文件并打印到标准输出设备上
type: command/linux
---


## 拿到文件的后缀
```shell
basename $file | rev | cut -d . -f 1- | rev
```

<iframe src='https://wangchujiang.com/linux-command/c/cut.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/cut.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/cut.html</a></center>

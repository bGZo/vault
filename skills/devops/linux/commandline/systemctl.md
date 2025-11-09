---
draft: true
created: 2023-10-05
description: 系统服务管理器指令
type: command/linux
---
<iframe src='https://wangchujiang.com/linux-command/c/systemctl.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/systemctl.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/systemctl.html</a></center>
  - **systemctl命令** 是系统服务管理器指令，它实际上将 [[service]] 和 [[chkconfig]] 这两个命令组合到一起。
### 查看所有已启动的服务
```shell
systemctl list-units --type=service # same as `chkconfig --list`
```
  - [systemctl 服务被锁定 masked_systemctl masked-CSDN博客](https://blog.csdn.net/PPlluuttoo/article/details/126781725)
```shell
systemctl mask sleep.target
systemctl unmask sleep.target
```

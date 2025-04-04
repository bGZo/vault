---
created: 2024-08-11
description: 比 find 好用的文件查找工具
type: command/linux
---

<iframe src='https://wangchujiang.com/linux-command/c/locate.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/locate.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/locate.html</a></center>

locaate 指令可以快速定位文件路径。locate 指令利用事先建立的系统中所有文件名称及路径的locate 数据库实现快速定位给定的文件。Locate 指令无需遍历整个文件系统，查询速度较快。为了保证查询结果的准确度，管理员必须定期更新 locate 时刻

由于 locate 指令基于数据库进行查询，所以第一次运行前，必须使用 updatedb 指令创建 locate 数据库。

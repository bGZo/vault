---
draft: true
created: 2024-08-11
description: 显示目录内容列表
type: command/linux
---
<iframe src='https://wangchujiang.com/linux-command/c/ls.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/ls.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/ls.html</a></center>
## Reference
```shell
$ ls -l
drwxr-xr-x 6 root root    4096 Oct 20  2017 apt
-rw-r--r-- 1 root root     211 Oct 20  2017 hosts
```
- 1 字段
  - **文件类型**(1)
    - `-` -> 普通文件
    - `d` -> 目录
    - `l` -> 链接
  - **模式 / 权限位** (access permission bits)(2-10)
    - 3 个值/组, 每组 `rwx` 表示 "读(read), 写(write), 执行(execute)"
    - 三个组
      - 文件**所有者**拥有的权限
      - 文件所关联的**用户组**成员拥有的权限
      - **其他人**拥有的权限
    - 任何被移除的权限会被替换为 `-` ，因此你可以将不同的值，及其代表的相关权限进行组合
      - `-rw-r–r--`
        - 普通文件
        - 所属用户可读可写不能执行
        - 对于所属的组,仅仅可读
        - 对于其他用户,也是仅仅可读
    - 利用 [[chmod]] 修改一个文件的权限
      - 如果想改变权限,可以使用命令 `chmod 711 hosts`
    - 利用 [[umask]] 修改一个文件权限的默认值
- 2 字段
  - **硬链接**(hard link)**数目**, via [[os/file-system]]
- 3 字段
  - **所属用户**
  - Change -> [[chown]]
- 4 字段
  - **所属组**
  - Change -> [[chgrp]]
- 5 字段
  - 文件的大小
- 6 字段
  - **文件被修改的日期**
- 7 字段
  - **文件名**
- id: 62515057-455a-4083-bfc4-b439da391075
```shell
ls -al |grep "^-" | wc -l
# 查询当前目录下的文件个数
ls -F |grep "*"
# 查询当前目录下的可执行文件
ls -F |grep "@"
# 查询当前目录下的符号链接文件
ls -al |grep "^-"
# 查询当前目录下的文件
ls -al |grep "^d"
# 查询当前目录下的文件夹
ls -F |grep "/"
# 查询当前目录下的文件夹
ls -F |grep "/$"
# 查询当前目录下的文件夹
```
- 在每个文件名后附上一个字符以说明该文件的类型
  - / 表明是一个目录
  - @ 表明是到其它文件的符号链接
  - = 表示套接字 (sockets)
  - | 表示 FIFOs
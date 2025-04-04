---
created: 2024-08-11
description: 将许多文件一起保存至一个单独的磁带或磁盘归档，并能从归档中单独还原所需文件。
type: command/linux
tags: #[[compress]]
---

<iframe src='https://wangchujiang.com/linux-command/c/tar.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/tar.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/tar.html</a></center>
  - tape archive (磁带档案)
  - -r：向压缩归档文件末尾追加文件
  - -u：更新原压缩包中的文件
  - 下面的参数是根据需要在压缩或解压档案时可选的。
    - -j：有bz2属性的
    - -Z：有compress属性的
    - -v：显示所有过程
    - -O：将文件解开到标准输出
  - cases
    - 打包文件
```shell
tar -cf archive.tar file1 file2
```
- `-c`
  - create
  - 建立压缩档案
- `-f`
  - 必须
  - 使用档案名字
  - 参数后面只能接档案名 (最后 1 个参数)
    - 提取文件
```shell
tar -xf archive.tar -C directory
```
- `-x`
  - extract
  - 提取
- 可以识别压缩的档案包, 完成解压
    - 不提取文件，只罗列某个档案包里含有的文件列表
```shell
tar -tf archive.tar
```
- `-t`
  - list
  - 查看内容
    - 创建**压缩**档案包
```shell
tar -czf archive.tar.gz file1 file2
```
- `-z`
  - gzip
      - 这就像是先创建了一个 tar 档案包，再运行 gzip 来压缩它

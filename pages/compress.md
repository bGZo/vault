---
aliases:
  - 压缩
  - Compress
created: 2025-06-07T15:33:09
description: 
modified: 2025-07-19T10:06:30
tags: []
title: Compress
type:
---

# Compress

## Why

- Save money (memory, bandwidth)
- increase performance
- encryption
- trans easy rather then multi files

## Compression File Type

| Name    | 概括特点                                                                                                               | 创始人                                                                                    | 备注                   |
| :------ | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :------------------- |
| zip     | 压缩数据段 + 中央目录区 + 中央目录区尾部                                                                                            | [菲尔·卡茨](https://zh.m.wikipedia.org/zh-hans/%E8%8F%B2%E5%B0%94%C2%B7%E5%8D%A1%E8%8C%A8) | unzip                |
| gzip    | GNU 计划的实现，gzip 代表 GNU zip                                                                                          | Jean-loup Gailly / Mark Adler                                                          |                      |
| rar     | 压缩比 \> ZIP ，但压缩/解压缩速度较慢&&分卷压缩&&固实压缩&&恢复记录&&AES-128-cbc                                                             | 尤金·罗谢尔                                                                                 | unrar e              |
| 7z      | Max 压缩比 && 开源 && AES-256 加密 && 支持 16EB && 多线程压缩                                                                    | -                                                                                      |                      |
| tar     | Unix 和类 Unix 系统上的压缩，可将多个文件合并为一个文件，打包后的文件后缀亦为“tar”。tar 已经成为 POSIX 标准，当前是 POSIX.1-2001。名字的含义是将文件备份到磁带上（tape archive） | 自由软件基金会                                                                                | tar –xvf             |
| gz      | GZ 是 UNIX 系统中的压缩文件，ZIP 的 Gnu 版本                                                                                    | gzip fileName                                                                          | gzip -d 或者 gunzip    |
| *.bz2   | tar 打包，gzip 程序压缩的文件。数据压缩算法及程序。在 1996 年 7 月第一次公开发布了 bzip2 0.15 版，2000 年 1.0 版                                       | Julian Seward                                                                          | bzip2 -d 或者用 bunzip2 |
| tar.gz  | tar 打包，gzip 程序压缩的文件                                                                                                | tar zcvf FileName.tar.gz dirName                                                       | tar –xzf（tgz）        |
| tar.xz  | tar 打包，xz 程序压缩的文件                                                                                                  | tar cvJf fileName.tar.xz dirName                                                       |                      |
| tar.bz2 | tar 打包，bzip2 程序压缩的文件                                                                                               | tar jcvf FileName.tar.bz2 dirName                                                      | tar –xjf             |
| Z       | compress 命令解压缩 rar 文件                                                                                              | compress fileName                                                                      | uncompress           |
| tar.Z   |                                                                                                                    |                                                                                        | tar –xZf             |

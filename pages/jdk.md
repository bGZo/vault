---
aliases:
  - java development kit
  - JDK
created: 2024-08-05T00:00:00
modified: 2025-08-30T17:03:16
title: JDK
wikipedia: https://en.wikipedia.org/wiki/Java_Development_Kit
---

# JDK

jre 的超集，内含更多工具，如 `javac`, `jconsole`, `jvisualvm`, `javadoc`, `jdb` 等

- Java 运行 => JRE
- Java 编程 => JDK
- 特例: JSP 部署 Web 应用程序
    - 应用程序服务器会将 JSP 转换为 Java servlet，并且需要使用 JDK 来编译 servlet

```shell
javac         # 编译器，将后缀名为.java的源代码编译成后缀名为“.class”的字节码
java          # 运行工具，运行.class的字节码
jar           # 打包工具，将相关的类文件打包成一个文件
javadoc       # 文档生成器，从源码注释中提取文档，注释需符合规范
jdb debugger  # 调试工具
jps           # 显示当前java程序运行的进程状态
javap         # 反编译程序
appletviewer  # 运行和调试applet程序的工具，不需要使用浏览器
javah         # 从Java类生成C头文件和C源文件。这些文件提供了连接胶合，使Java和C代码可进行交互
javaws        # 运行JNLP程序
extcheck      # 一个检测jar包冲突的工具
apt           # 注释处理工具
jhat          # java堆分析工具
jstack        # 栈跟踪程序
jstat         # JVM检测统计工具
jstatd        # jstat守护进程
jinfo         # 获取正在运行或崩溃的java程序配置信息
jmap          # 获取java进程内存映射信息
idlj          # IDL-to-Java编译器。将IDL语言转化为java文件[4]
policytool    # 一个GUI的策略文件创建和管理工具
jrunscript    # 命令行脚本运行
```

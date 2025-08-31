---
aliases:
  - java virtual machine
  - JVM
created: 2025-03-23T13:44:37
modified: 2025-08-30T17:32:19
title: JVM
---

# JVM

## Java 的语言 => JIT（just-in-time compilation） 编译器

- 运行时编译
	- 当 JIT 编译器完成第一次编译后，其会将字节码对应的机器码保存下来，下次可以直接使用
	- 机器码的运行效率 > Java 解释器
- HotSpot VM 原理 -> **二八定律** (大部分系统资源的只消耗在 **小部分的代码 (热点代码)** 上)
	- 惰性评估 (Lazy Evaluation) 的做法
- JVM 会根据代码每次被执行的情况收集信息并做出优化，因此 执行次数 和 速度 成正比
- AOT(Ahead Of Time Compilation)
	- From JDK 9
	- 它是直接将字节码编译成机器码，这样就避免了 JIT 预热等各方面的开销
	- [[jdk]] 支持分层编译和 AOT 协作使用
	    - 编译质量 < JIT 编译器

## Java Virtual Machine

运行 Java 字节码 的虚拟机

$$ 传统解释型语言 < Java 运行效率 < 编译性语言(C++，Rust，Go...)$$

$$Awesome => 运行效率 > 解释型语言高 + 保留了 解释型语言 可移植的特点$$

  $$跨平台 == 字节码 + JVM_{ Win + Linux + Mac + ... } == 一次编译, 随处运行$$

## 实现

- JVM 规范
    - 可以在 Java SE Specifications 上找到各个版本的 JDK 对应的 JVM 规范。
- 例子
	- HotSpot VM
	- J9 VM
	- Zing VM
	- JRockit VM
- [ ] Comparison of Java virtual machines

## References

- [Java JVM怎么学习啊？从哪方面入手？ - 知乎](https://www.zhihu.com/question/20097631)
- [实战Java虚拟机 (豆瓣)](https://book.douban.com/subject/26354292/)
- [深入理解Java虚拟机（第3版） (豆瓣)](https://book.douban.com/subject/34907497/)

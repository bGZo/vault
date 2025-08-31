---
aliases:
  - java virtual machine
  - JVM
created: 2025-03-23T13:44:37
modified: 2025-08-31T13:42:57
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

## 类加载

- Class Life Cycle
    - Class Loading Process
        - 加载
        - 连接
            - 验证
            - 准备
            - 解析
        - 初始化
    - 使用
    - 卸载
- Process
    - Class Loading Process
        - 任务
            - 通过全类名获取定义此类的二进制字节流
            - 将字节流所代表的静态存储结构转换为方法区的运行时数据结构
            - 在内存中生成一个代表该类的 `Class` 对象，作为方法区这些数据的访问入口
- 初始化
	- ???
- Class Loader
	- 总结
	- 双亲委派模型
	- 自定义类加载器

## 内存模型

![[Java-Memory-Model.png]]

### Young Generation

the place where all the new objects are created

- GC => **Minor GC**

#### Java Memory Model

- Eden Memory
- Survivor Memory(S0, S1)

### Old Generation, Tenured

- GC => **Major GC**

#### Stop the World Event

**all GC is this event**, which means all application threads are stopped until the operation completes.

#### Java Memory Model

- 永久代 Permanent Generation, Perm Gen: contains the application metadata required by the JVM to describe the classes and methods used in the application

> [!warning]
> Perm Gen is not part of Java Heap memory, and changed name to **Metaspace** since [[java08]]. The most significant difference is **how it handles memory allocation**. Specifically, this native memory region grows automatically by default.
> 永久代不是堆内存，最显着的区别是它如何处理内存分配。具体而言，默认情况下，此本机内存区域会自动增长
> via: [Permgen vs Metaspace in Java | Baeldung](https://www.baeldung.com/java-permgen-metaspace)

- We also have new flags to tune the memory:
    - *MetaspaceSize* and *MaxMetaspaceSize –* we can set the Metaspace upper bounds.
    - *MinMetaspaceFreeRatio – *is the minimum percentage of class metadata capacity free after [garbage collection](https://www.baeldung.com/jvm-garbage-collectors)
    - *MaxMetaspaceFreeRatio *– is the maximum percentage of class metadata capacity free after a garbage collection to avoid a reduction in the amount of space
- 方法区 Method Area: Store class structure (runtime constants and static variables) and code for methods and constructors.
- 常量池 Runtime Constant Pool: per-class runtime representation of constant pool in a class. (类中常量池的每个类运行时表示形式). It contains class runtime constants and static methods.
- 内存池 Memory Pool: Create a pool of immutable objects if the implementation supports it. like String Pool.

> [!warning]
> Memory Pool can belong to Heap or Perm Gen, depending on the JVM memory manager implementation.
> 属于堆还是永久代取决于 JVM 内存管理的实现

- 栈内存 Java Stack Memory: used for execution of a thread. They contain method specific values that are short-lived and references to other objects in the heap that is getting referred from the method.

> [!warning]
> Stack memory belongs to the non-heap memory of JVM. It is allocated for each thread that runs in the JVM. Stack memory is used to store local variables and method calls for each thread.

- [Difference between Stack and Heap Memory](https://www.digitalocean.com/community/tutorials/java-heap-space-vs-stack-memory)

#### Memory Management in Java

| VM Switch         | VM Switch Description                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| -Xms              | initial heap size <br>堆初始值                                                                            |
| -Xmx              | maximum heap size <br>堆最大值                                                                            |
| -Xmn              | size of the Young Generation, <br>rest of the space goes for Old Generation. <br>设置年轻一代的大小，其余的空间用于老一代 |
| -XX:PermGen       | initial size of the Perm Gen <br>永久代初始值                                                               |
| -XX:MaxPermGen    | maximum size of Perm Gen <br>永久代最大值                                                                   |
| -XX:SurvivorRatio | ratio of Eden space and Survivor Space (8(:1:1) default) <br>伊甸园和幸存区比率                                |
| -XX:NewRatio      | ratio of old/new generation sizes (2 default)                                                         |

- Java Heap Memory Switches
    - Java provides a lot of memory switches that we can use to set the memory sizes and their ratios. Some of the commonly used memory switches are:
    - `-XX:SurvivorRatio` example
      - if Young Generation size is 10m and VM switch is -XX:SurvivorRatio=2 then 5m will be reserved for Eden Space and 2.5m each for both the Survivor spaces. The default value is 8.
  - Most of the times, above options are sufficient, but if you want to check out other options too then please check [JVM Options Official Page](https://www.oracle.com/technetwork/java/javase/tech/vmoptions-jsp-140102.html).
- Java Garbage Collection
  - **Marking**
    - Identifies which objects are in use and which ones are not in use.
  - **Normal Deletion**
    - removes the unused objects and reclaim the free space to be allocated to other objects.
  - **Deletion with Compacting**
    - For better performance, after deleting unused objects, all the survived objects can be moved to be together. This will increase the performance of allocation of memory to newer objects.
  - 2 problems with a simple mark and delete approach.
    - Not efficient
      - most of the newly created objects will become unused
    - 在多个垃圾回收周期中使用的对象也最有可能在未来的周期中使用
      Secondly objects that are in-use for multiple garbage collection cycle are most likely to be in-use for future cycles too.
- Java Garbage Collection Types
  - **Serial GC (-XX:+UseSerialGC)**
    - Serial GC uses the simple **mark-sweep-compact** approach for young and old generations garbage collection i.e Minor and Major GC.Serial GC is useful in client machines such as our simple stand-alone applications and machines with smaller CPU. It is good for small applications with low memory footprint.
  - **Parallel GC (-XX:+UseParallelGC)**
    - Parallel GC is same as Serial GC except that is spawns N threads for young generation garbage collection where N is the number of CPU cores in the system. We can control the number of threads using `-XX:ParallelGCThreads=n` JVM option.Parallel Garbage Collector is also called throughput collector because it uses multiple CPUs to speed up the GC performance. Parallel GC uses a single thread for Old Generation garbage collection.
  - **Parallel Old GC (-XX:+UseParallelOldGC)**
    - This is same as Parallel GC except that it uses multiple threads for both Young Generation and Old Generation garbage collection.
  - **Concurrent Mark Sweep (CMS) Collector (-XX:+UseConcMarkSweepGC)**
    - CMS Collector is also referred as concurrent low pause collector. It does the garbage collection for the Old generation. CMS collector tries to minimize the pauses due to garbage collection by doing most of the garbage collection work concurrently with the application threads.CMS collector on the young generation uses the same algorithm as that of the parallel collector. This garbage collector is suitable for responsive applications where we can’t afford longer pause times. We can limit the number of threads in CMS collector using `-XX:ParallelCMSThreads=n` JVM option.
  - **G1 Garbage Collector (-XX:+UseG1GC)**
    - The Garbage First or G1 garbage collector is available from Java 7 and its long term goal is to replace the CMS collector. The G1 collector is a parallel, concurrent, and incrementally compacting low-pause garbage collector.Garbage First Collector doesn’t work like other collectors and there is no concept of Young and Old generation space. It divides the heap space into multiple equal-sized heap regions. When a garbage collection is invoked, it first collects the region with lesser live data, hence “Garbage First”. You can find more details about it at [Garbage-First Collector Oracle Documentation](https://docs.oracle.com/javase/7/docs/technotes/guides/vm/G1.html).
- Java Garbage Collection Monitoring
- Java Garbage Collection Tuning (调优)

## [[java-interview]]

- 介绍下 Java 内存区域（运行时数据区）
- Java 对象的创建过程（五步，建议能默写出来并且要知道每一步虚拟机做了什么）
- 对象的访问定位的两种方式（句柄和直接指针两种方式）

## References

- [[~Java-Memory-Management-Explained|Java Memory Management Explained]]
- 深入理解 Java 虚拟机：JVM 高级特性与最佳实践 第二版
- [Java 内存区域详解 | JavaGuide](https://javaguide.cn/java/jvm/memory-area.html)
- 《自己动手写 Java 虚拟机》
- Chapter 2. The Structure of the Java Virtual Machine：https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html
- JVM 栈帧内部结构 - 动态链接：https://chenxitag.com/archives/368
- Java 中 new String(" 字面量 ") 中 " 字面量 " 是何时进入字符串常量池的? - 木女孩的回答 - 知乎： https://www.zhihu.com/question/55994121/answer/147296098
- JVM 常量池中存储的是对象还是引用呢？ - RednaxelaFX 的回答 - 知乎： https://www.zhihu.com/question/57109429/answer/151717241
- [http://www.pointsoftware.ch/en/under-the-hood-runtime-data-areas-javas-memory-model/open in new window](http://www.pointsoftware.ch/en/under-the-hood-runtime-data-areas-javas-memory-model/)
- [https://dzone.com/articles/jvm-permgen-–-where-art-thouopen in new window](https://dzone.com/articles/jvm-permgen-%E2%80%93-where-art-thou)
- [https://stackoverflow.com/questions/9095748/method-area-and-permgen](https://stackoverflow.com/questions/9095748/method-area-and-permgen)
- https://blog.newnius.com/java-garbage-collection-what-why-how.html
- [类加载过程详解 | JavaGuide](https://javaguide.cn/java/jvm/class-loading-process.html)
- [https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-5.html](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-5.html)
- Class Life Cycle 为什么搜不到国外的教材内容???
- [Java JVM怎么学习啊？从哪方面入手？ - 知乎](https://www.zhihu.com/question/20097631)
- [实战Java虚拟机 (豆瓣)](https://book.douban.com/subject/26354292/)
- [深入理解Java虚拟机（第3版） (豆瓣)](https://book.douban.com/subject/34907497/)

---
aliases:
  - Java Version
created: 2024-08-01T00:00:00
modified: 2025-08-30T16:13:37
title: Java Version
wikipedia: https://en.wikipedia.org/wiki/Java_version_history
---

# Java Version

## Branch

- [[javase|JavaSE]] / Java Platform, Standard Edition / ~~J2SE~~
	- SE 主要包含语言特性，标准库和虚拟机 [[jvm]]
- **Jakarta EE** / Java Platform, Enterprise Edition / ~~[[javaee|JavaEE]]~~ / ~~J2EE~~
	- EE 主要包含企业级 API，如 servlet、 jsp、EJB、JMS、JPA、 cdi 等。
- **Java ME** / Java Platform, Micro Edition / ~~J2ME~~
	- ME 主要面向移动设备进行开发，正转向其他平台；
	- 注意 JavaME != Android != 嵌入系统开发

> [!note]
> [[javaee]] *J2SE / J2EE / J2ME* 均是 java02 时代的称呼，自 [[java05]] 之后集体更名为 *JavaSE / JavaEE / JavaME*； JavaEE 在 [[java08]] 之后被 Oracle 移交 eclipse 基金会管理，故更名为 Jakarta；

## 01

- [[java-beans]]
- exception
- [[java-reflection]]

### Feats

- 内部类 (inner classes)
- 声明最终的局部变量 (final local variables)、方法参数 (method parameters,) 和捕获子句参数 (catch clause parameters)
- 实例容器化 (Instance initializers)
- 最终变量声明不需要包括初始化器 final variable declarations do not have to include initializers
- 匿名数组 (anonymous array)

### More

- [(Chapter 1) 1.2 New Language Features in Java 1.1](https://docstore.mik.ua/orelly/java/langref/ch01_02.htm)

## 05

  - [[java-reflection]]
  - [[java concurrency]]
    - [[java-multithreading]]

### Feats

- 修改命名方式（1.5 -> 5）；
- 泛型 (Generics) => [[java-generics]]
- 增强循环（Enhanced for Loop）

```java
int[] array = {1, 2, 3, 4, 5};
for (int i : array) {
    System.out.println(i);
}
```

- 自动封箱拆箱 (Autoboxing/Unboxing)
    - 八大基本类型和它们的包装类能够自动的相互转换
    - 自动装箱 (Autoboxing): 把一个基本类型变量直接赋给对应的包装类变量，或者赋给 Object 变量 (Object 是所有类的父类，子类对象可以直接赋给父类变量)

```java
public class AutoBoxingUnboxing{
  public static void main(String[] args){
    //直接把一个基本类型变量赋给Integer对象
    Integer inObj=5;
    //直接把一个boolean类型变量赋给一个Object类型变量
    Object boolObj=true;
    //直接把一个Integer对象赋给int类型变量
    int it=inObj;
    if (boolObj instanceof Boolean){
      //先把Object对象强制类型转换为Boolean类型，再赋给boolean变量
      boolean b=(Boolean)boolObj;
      System.out.println(b);
    }
  }
}
```

- int 类型变量只能自动装箱成 Integer 对象（即使赋给 Object 类型变量，那也只是利用了 Java 的**向上自动转型特性**），不要试图装箱成 Boolean 对象
- 枚举 (Typesafe Enums): **枚举是一种实现线程安全的单例模式的好方式**
    - 单例模式：因为 Java 中的枚举本质上是一个类，并且只有一个实例，所以没有多线程的问题
    - 线程安全
      - 此外，枚举在运行时不能被反射或序列化，从而额外的保证了单例的安全
        - 枚举是 Java 中特殊的类，它的实现机制与普通类有很大的不同。
          - 枚举类型是通过编译器生成一个类来实现的
            - 该类继承自 Java.lang.Enum，且构造函数是私有的
            - 通过反射创建枚举实例是不可能的
        - 枚举不能被序列化，因为它的实例在整个 JVM 范围内是唯一的，因此不需要序列化

```java
enum TestEnum{
    one,
    two;
    TestEnum() {
    }
}
```

- 可变参数 (Varargs)
  - 语法：`(type... arguments)`
  - 可变参数本质仍然是用一个数组存储参数，只是 java 隐藏了这一过程
  - 需要注意的是如果一个方法声明中含有可变参数，那必须放在最后一个位置。
- 静态导入（Static Import）
  - 通过 import 类来使用类里的静态变量或方法（直接通过名字，不需要加上 `类名.`）,简化了代码的书写
  - ps: 过去的版本中只能通过继承类或实现接口才能使用。
- 注解（Annotations）
  - 关键字 `@interface`
- 新的线程模型和并发库（`java.util.concurrent`)

### More

- [Java 5.0 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/Java_5.0)
- [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)

## 06

### Feats

- 集合框架增强。
  - 为了更好的支持双向访问集合。添加了许多新的类和接口。
  - 新的数组拷贝方法。`Arrays.copyOf` 和 `Arrays.copyOfRange`

```shell
# 以下为添加的新接口和类
Deque
BlockingDeque
NavigableSet
NavigableMap
ConcurrentNavigableMap
ArrayDeque
ConcurrentSkipListSet
ConcurrentSkipListMap
ConcurrentSkipListMap
AbstractMap.SimpleEntry
AbstractMap.SimpleImmutableEntry
```

- Scripting. 可以让其他语言在 java 平台上运行。 java6 包含了一个基于 Mozilla Rhino 实现的 javascript 脚本引擎。
- 支持 JDBC4.0 规范

### More

- [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)

## 07

### Feats

- 二进制前缀 `0b` / `0B`；
  - 整型（byte, short, int, long）可以直接用二进制表示

```JAVA
//二进制字面值前缀0b / 0B
int i = 0b010; //10进制值为2
int j = 0B010;
```

- 字面常量数字的下划线；
  - 用下划线连接整数提升其可读性，自身无含义，不可用在数字的起始和末尾。

```java
//数字间的下划线不影响实际值
int k = 1_1;//值为11
```

- switch 支持 String 类型；
- 泛型实例化类型自动推断；

```java
Map<String, List<String>> myMap = new HashMap<String, List<String>>();    // Before
Map<String, List<String>> myMap = new HashMap<>();                        // Now
```

- try-with-resources 语句；

```java
/*
 * 声明在try括号中的对象称为资源，在方法执行完毕后会被自动关闭,
 * 相对与之前必须在finally关闭资源，这一特性大大提高了代码的简洁性。
 * 所有实现java.lang.AutoCloseable接口的类都作为资源被自动关闭。
*/
try (BufferedReader reader=new BufferedReader(new FileReader("d:1.txt"))){
  return reader.readLine();
}
```

- 单个 catch 中捕获多个异常类型（用 `|` 分割）并通过改进的类型检查重新抛出异常；

### More

- [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)

## 08 #lts

### Feats

- [[java-lambda]] | 表达式 (Lambda Expressions)
- **方法引用 (Method references)**
  - 方法引用提供了非常有用的语法，可以直接引用已有 Java 类或对象（实例）的方法或构造器。与 lambda 联合使用，方法引用可以使语言的构造更紧凑简洁，减少冗余代码。
- **默认方法 (Default methods)**
  - 默认方法就是一个在接口里面有了一个实现的方法。
- **新工具**
  - 新的编译工具，如：Nashorn 引擎 jjs、 类依赖分析器 jdeps。
- **Stream API**
  - 新添加的 Stream API（java.util.stream） 把真正的函数式编程风格引入到 Java 中。
- **Date Time API**
  - 加强对日期与时间的处理。
- **Optional 类**
  - Optional 类已经成为 Java 8 类库的一部分，用来解决空指针异常。
- **Nashorn, JavaScript 引擎**
  - Java 8 提供了一个新的 Nashorn javascript 引擎，它允许我们在 JVM 上运行特定的 javascript 应用。
- 重复注解（Repeating Annotations）。重复注解提供了在同一声明或类型中多次应用相同注解类型的能力。
- 类型注解（Type Annotation）。在任何地方都能使用注解，而不是在声明的地方。
- 类型推断增强。
- 方法参数反射（Method Parameter Reflection）。
- HashMap 改进，在键值哈希冲突时能有更好表现。
- java.util 包下的改进，提供了几个实用的工具类。
  - 并行数组排序。
  - 标准的 Base64 编解码。
  - 支持无符号运算。
- java.util.concurrent 包下增加了新的类和方法。
  - `java.util.concurrent.ConcurrentHashMap` 类添加了新的方法以支持新的 StreamApi 和 lambada 表达式。
  - `java.util.concurrent.atomic` 包下新增了类以支持可伸缩可更新的变量。
  - `java.util.concurrent.ForkJoinPool` 类新增了方法以支持 common pool。
  - 新增了 `java.util.concurrent.locks.StampedLock` 类，为控制读/写访问提供了一个基于性能的锁，且有三种模式可供选择。
- HotSpot
  - 删除了 永久代（PermGen）.
  - 方法调用的字节码指令支持默认方法。

### More

- [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)
  - [JDK Release Notes](http://www.oracle.com/technetwork/java/javase/jdk-relnotes-index-2162236.html)
  - [What’s New in JDK 8](http://www.oracle.com/technetwork/java/javase/8-whats-new-2157071.html)
  - [What’s New in JDK 9](https://docs.oracle.com/javase/9/whatsnew/toc.htm#JSNEW-GUID-C23AFD78-C777-460B-8ACE-58BE5EA681F6)
  - [JDK 10 Release Notes](http://www.oracle.com/technetwork/java/javase/10-relnote-issues-4108729.html#NewFeature)
  - [JDK 11 Release Notes](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#NewFeature)
- [Java 8 新特性 | 菜鸟教程](https://www.runoob.com/java/java8-new-features.html)

## 10

2018 年 3 月 21 日, Oracle 官方宣布 JAVA10 正式发布

JAVA9 和 java10 都不是 LTS (Long-Term-Support) 版本.和过去的 JAVA 大版本升级不同,这两个只有半年左右的开发和维护时间. 而 JAVA11 也是就是 18.9,才是 JAVA 之后的第一个长期支持版本

JAVA10 一共定义了 109 个新特性,其中包含 JEP,对程序员来说,真正的新特性也就一个,还有一些新的 API 和 JVM 规范以及 JAVA 语言规范上的改动.

JAVA10 的 12 个 JEP (JDK Enhancement Proposal 特性加强协议) ,可参阅官方文档 http://openjdk.java.net/projects/jdk/10/

![[1630388526815.png]]

> 286: 局部变量类型推断
> 296: JDK 库合并
> 304: 统一的垃圾回收接口
> 307: 为 G1 提供并行的 Full GC
> 310: 应用程序类数据共享
> 312: ThreadLocal 握手交互
> 313: 移除 JDK 中附带的 javah 工具
> 314: 使用附加的 Unicode 语言标记拓展
> 316: 能将对内存占用分配给用户指定的备用内存设备
> 317: 使用基于 JAVA 的 JIT 编译器
> 319: 根证书
> 322: 基于时间的发布版本

## 11

### Feats

2018 年 9 月 26 日,Oracle 官方发布 JAVA11.这是 JAVA 大版本周期变化后的第一个长期支持版本,非常值得关注.最新发布的 JAVA11 将带来 ZGC HttpClient 等重要特性,一共 17 个需要我们关注的 JEP,参考文档 http://openjdk.java.net/projects/jdk/11/

![[1630397289057.png]]

- 181: [Nest-Based Access Control](https://openjdk.org/jeps/181)
	- 基于嵌套的访问控制
- 309: [Dynamic Class-File Constants](https://openjdk.org/jeps/309)
	- 动态类文件常量
- 315: [Improve Aarch64 Intrinsics](https://openjdk.org/jeps/315)
	- 改进 Aarch64 Intrinsics
- 318: [Epsilon: A No-Op Garbage Collector](https://openjdk.org/jeps/318)
	- Epsilon: 一个无操作的垃圾收集器
- 320: [Remove the Java EE and CORBA Modules](https://openjdk.org/jeps/320)
	- 移除 Java EE 和 CORBA 模块
- 321: [HTTP Client (Standard)](https://openjdk.org/jeps/321)
	- HTTP 客户端 (标准)
- 323: [Local-Variable Syntax for Lambda Parameters](https://openjdk.org/jeps/323)
	- 本地变量语法 Lambda 参数
- 324: [Key Agreement with Curve25519 and Curve448](https://openjdk.org/jeps/324)
	- 与 Curve25519 和 Curve448 的密钥一致
- 327: [Unicode 10](https://openjdk.org/jeps/327)
	- Unicode 10
- 328: [Flight Recorder](https://openjdk.org/jeps/328)
	- 飞行记录器
- 329: [ChaCha20 and Poly1305 Cryptographic Algorithms](https://openjdk.org/jeps/329)
	- ChaCha20 和 Poly1305 密码算法
- 330: [Launch Single-File Source-Code Programs](https://openjdk.org/jeps/330)
	- 启动单文件源代码程序
- 331: [Low-Overhead Heap Profiling](https://openjdk.org/jeps/331)
	- 低开销堆分析
- 332: [Transport Layer Security (TLS) 1.3](https://openjdk.org/jeps/332)
	- TLS (Transport Layer Security) 1.3
- 333: [ZGC: A ScalableLow-Latency Garbage Collector (Experimental)](https://openjdk.org/jeps/333)
	- ZGC: 一个可伸缩的低延迟垃圾收集器 (实验)
- 335: [Deprecate the Nashorn JavaScript Engine](https://openjdk.org/jeps/335)
	- 已弃用 Nashorn JavaScript 引擎
- 336: [Deprecate the Pack200 Tools and API](https://openjdk.org/jeps/336)
	- 已弃用 Pack200 工具和 API

## 22

- IDE: https://www.jetbrains.com/idea/download/download-thanks.html?platform=windowsZip&code=IIC
- JDK: https://download.java.net/java/GA/jdk22.0.2/c9ecb94cd31b495da20a27d4581645e8/9/GPL/openjdk-22.0.2_windows-x64_bin.zip

### Feats

- 423: Region Pinning for G1 via: https://openjdk.org/jeps/423
  - 通过在 G1 中实现区域钉扎来减少延迟，这样在 Java Native Interface（JNI）关键区域期间就不需要禁用垃圾收集。
  - 使用 JNI 时，Java 线程无需在 G1 GC 操作完成之前等待，从而提高开发人员的工作效率。
- 454: Foreign Function & Memory API via: https://openjdk.org/jeps/454
  - 引入 API，Java 程序可以通过该 API 与 Java 运行时之外的代码和数据进行互操作。通过有效地调用外部函数（即 JVM 外部的代码），并通过安全地访问外部内存（即不受 JVM 管理的内存），API 使 Java 程序能够调用本机库并处理本机数据，而不会出现 JNI 的脆弱性和危险性。
  - via: https://blog.csdn.net/nanxiaotao/article/details/136863342
  - **价值**
    - 生产力：用简洁、可读且纯 Java API 取代脆弱的本机方法和 Java 本机接口 (JNI)。
    - 性能：提供对外部函数和内存的访问，其开销与 JNI 和 sun.misc.Unsafe 相当（如果不是更好的话）。
    - 广泛的平台支持：允许在 JVM 运行的每个平台上发现和调用本机库。
    - 一致性：提供在多种内存（例如本机内存、持久内存和托管堆内存）中操作无限大小的结构化和非结构化数据的方法。
    - 健全性：保证没有释放后使用错误，即使在多个线程之间分配和释放内存时也是如此。
    - 完整性：允许程序使用本机代码和数据执行不安全的操作，但默认警告用户此类操作。
- 456: Unnamed Variables & Patterns 未命名变量和模式
  - 使用未命名变量和未命名模式增强 Java 编程语言，当需要变量声明或嵌套模式但从未使用时，可以使用这些变量和模式。两者都用下划线字符 _ 表示。
  - 表明声明的该变量创建者无意使用，并告知后开者也不该使用，之前我们可能写 `ignored variable`. 现在统一写 `_`
  - `_` 在 Java 8 中是警告，在 Java 9 中是错误；
    via: https://stackoverflow.com/questions/23523946
    - `use of '_' as an identifier is not supported in releases since java 9`
  - 适用场景
    - 块内局部变量；
    - 异常处理；
      - `try()` 块内（resource specification）
      - `catch()` 块内
    - `for` 循环；
      - 增强 for 循环；
    - `lambda` 表达式
  - **价值**
    - 捕获开发人员的意图，即未使用给定的绑定或 lambda 参数，并强制执行该属性以澄清程序并减少出错的机会。
    - 通过识别必须声明（例如，在 catch 子句中）但未使用的变量，提高所有代码的可维护性。
    - 允许多个模式出现在单个 case 标签中，如果它们都没有声明任何模式变量。
    - 通过消除不必要的嵌套类型模式来提高记录模式的可读性
- 458: Launch Multi-File Source-Code Programs 启动多文件源代码程序
  - > 增强 java 应用程序启动器，使其能够运行作为 java 源代码的多个文件提供的程序。这将使从小程序到大程序的过渡更加渐进，使开发人员能够选择是否以及何时配置构建工具。
  - JDK 11 针对 Java 应用启动器做过优化，可以直接跑 `.java` 的 `source` 文件:
    - 局限是这些类必须放在一个文件中
  - JDK 22 打破了这个限制
- 447: Statements before super(...) (Preview)
  - 允许没有应用实例的语句出现在显式构造函数调用之前（explicit constructor invocation）
        via: https://openjdk.org/jeps/447
  - 457: Class-File API (Preview) via: https://openjdk.org/jeps/457
    - 提供一个标准的 API，用于解析、生成和转换 Java 类文件。这是一个预览 API。
    - ASM???
    - https://jameshamilton.eu/programming/build-compiler-jep-457-class-file-api
    - https://github.com/mrjameshamilton/jep457-hello-world/blob/master/Main.java
- 459: String Templates (Second Preview)
  - > 使用字符串模板增强 Java 编程语言。字符串模板通过将文本与嵌入的表达式和模板处理器耦合来产生专门的结果，从而补充 Java 现有的字符串文本和文本块。这是一个预览语言功能和 API。
  - 之前的方案
    - `+`
    - `StringBuilder`
    - `String:format`
    - `MessageFormat`
- 462: Structured Concurrency (Second Preview)
	- 通过引入用于结构化并发的 API 来简化并发编程。结构化并发将在不同线程中运行的相关任务组视为单个工作单元，从而简化错误处理和消除，提高可靠性，并增强可观察性。这是一个预览 API。
- 463: Implicitly Declared Classes and Instance Main Methods (Second Preview)
  - 发展 Java 编程语言，使学生无需理解为大型程序设计的语言功能即可编写第一个程序。学生们可以为单类程序编写精简的声明，而不是使用单独的语言方言，然后随着技能的发展，无缝地扩展程序，使用更高级的功能。这是一个预览语言功能。
- 464: Scoped Values (Second Preview)
  - > 引入作用域值，使不可变数据能够与同一线程中的子帧和子线程进行托管共享。作用域值比线程本地变量更容易推理，并且空间和时间成本更低，尤其是与虚拟线程和结构化并发结合使用时。这是一个预览 API。
  - Java 20 中的孵化功能（ [JEP 429）](https://openjdk.org/jeps/429) 引入，作为 Java 21 中的预览功能 [（JEP 446）](https://openjdk.org/jeps/446) 引入，目前处于 Java 22 中的第二轮预览（ [JEP 464）](https://openjdk.org/jeps/464)。
  - via: https://davidvlijmincx.com/posts/java-scoped-values-tutorial/
- 460: Vector API (Seventh Incubator) via: https://openjdk.org/jeps/460
- Java 机器学习
  - https://time.geekbang.org/column/article/464927

### More

- https://waylau.com/jdk-22-released/
- https://openjdk.org/projects/jdk/22/
- https://www.didispace.com/java-features/java22/#statements-before-super-preview-jep-447

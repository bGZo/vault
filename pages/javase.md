---
draft: true
aliases:
  - java standard edition
  - JavaSE
created: 2024-08-02T00:00:00
modified: 2025-08-30T16:29:54
title: JavaSE
wikipedia: https://en.wikipedia.org/wiki/Java_Platform,_Standard_Edition
---
# JavaSE

## Nomenclature, standards and specifications 术语、标准和规范

## General purpose packages

- contains [[java-library]]
    - [Object](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Object.html) – the class that is the root of every class hierarchy.
    - [Enum](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Enum.html) – the base class for [enumeration classes](https://en.wikipedia.org/wiki/Enumerated_type) (as of J2SE 5.0).
    - [Class](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Class.html) – the class that is the root of the Java [reflection](https://en.wikipedia.org/wiki/Reflection_(computer_science)) system.
    - [Throwable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Throwable.html) – the class that is the base class of the exception class hierarchy.
    - [Error](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Error.html), [Exception](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Exception.html), and [RuntimeException](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/RuntimeException.html) – the base classes for each exception type.
    - [Thread](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Thread.html) – the class that allows operations on threads.
    - [String](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/String.html) – the class for [strings](https://en.wikipedia.org/wiki/String_(computer_science)) and [string literals](https://en.wikipedia.org/wiki/String_literal).
    - [StringBuffer](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StringBuffer.html) and [StringBuilder](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StringBuilder.html) – classes for performing [string manipulation](https://en.wikipedia.org/wiki/StringBuffer_and_StringBuilder) (`StringBuilder` as of J2SE 5.0).
    - [Comparable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Comparable.html) – the interface that allows generic comparison and ordering of objects (as of J2SE 1.2).
    - [Iterable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Iterable.html) – the interface that allows generic iteration using the [enhanced `for` loop](https://en.wikipedia.org/wiki/Foreach#Java) (as of J2SE 5.0).
    - [ClassLoader](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/ClassLoader.html), [Process](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Process.html), [Runtime](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Runtime.html), [SecurityManager](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/SecurityManager.html), and [System](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/System.html) – classes that provide "system operations" that manage the [dynamic loading](https://en.wikipedia.org/wiki/Dynamically_loaded_library) of classes, creation of external [processes](https://en.wikipedia.org/wiki/Process_(computing)), host environment inquiries such as the time of day, and enforcement of [security policies](https://en.wikipedia.org/wiki/Security_policy).
    - [Math](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Math.html) and [StrictMath](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StrictMath.html) – classes that provide basic math functions such as [sine](https://en.wikipedia.org/wiki/Sine), [cosine](https://en.wikipedia.org/wiki/Cosine), and [square root](https://en.wikipedia.org/wiki/Square_root) (`StrictMath` as of J2SE 1.3).
    - The [primitive wrapper classes](https://en.wikipedia.org/wiki/Primitive_wrapper_class) that [encapsulate](https://en.wikipedia.org/wiki/Encapsulation_(computer_science)) [primitive types](https://en.wikipedia.org/wiki/Primitive_type) as [objects](https://en.wikipedia.org/wiki/Object_(computer_science)).
    - The basic exception classes thrown for language-level and other common exceptions.
- `java.lang`
    - `java.lang.ref`
        - 提供了比其他方式更灵活的 [引用](https://en.wikipedia.org/wiki/Reference_(computer_science)) 类型，允许应用程序和 [Java 虚拟机](https://en.wikipedia.org/wiki/Java_virtual_machine)(JVM)[垃圾收集器](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) 之间进行有限的交互。
        - `java.lang.ref` 包定义了其他三种类型的引用——软引用、[弱引用](https://en.wikipedia.org/wiki/Weak_reference) 和幻像引用 (soft, weak, and phantom references)。每种类型的参考都是针对特定用途而设计的。
    - `java.lang.reflect` [[java-reflection]]
        - basic techniques involved in reflection:
      - Discovery
      - Use by name
- [`java.io`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/package-summary.html)
    - 中心类: 读取和写入字节流的抽象基类
        - [InputStream](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/InputStream.html)
        - [OutputStream](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/OutputStream.html)
    - 相关类
        - [Reader](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/Reader.html) 和 [Writer](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/Writer.html) 是分别用于读取和写入字符流的抽象基类
    - 杂项类来支持与主机文件系统的交互。
    - `Streams`
        - 流类遵循 [装饰器模式](https://en.wikipedia.org/wiki/Decorator_pattern)，通过扩展基子类向流类添加功能。
    - Random access
        - [`RandomAccessFile`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/RandomAccessFile.html)
    - File system
        - [`File`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/File.html)
        - [`FileDescriptor`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileDescriptor.html)
- `java.nio`
    - 在 J2SE 1.4 中，添加了 [`java.nio`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/package-summary.html) 包（NIO 或非阻塞 I/O）来支持 [内存映射 I/O](https://en.wikipedia.org/wiki/Memory-mapped_I/O) ，使 [I/O](https://en.wikipedia.org/wiki/Input/output) 操作更接近底层硬件，有时性能显着提高。 `java.nio` 包提供了对多种缓冲区类型的支持。子包 [`java.nio.charset`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/charset/package-summary.html) 提供对字符数据的不同 [字符编码](https://en.wikipedia.org/wiki/Character_encoding) 的支持。子包 [`java.nio.channels`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/channels/package-summary.html) 提供对 _ 通道的支持，_ 通道表示与能够执行 I/O 操作的实体（例如文件和套接字）的连接。 `java.nio.channels` 包还提供对文件细粒度锁定的支持。
- `java.math`
    - [`BigDecimal`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/BigDecimal.html)
    - [`BigInteger`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/BigInteger.html)
    - [`MathContext`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/MathContext.html)
    - [`RoundingMode`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/RoundingMode.html)
- `java.net`：网络提供了特殊的 IO 例程 (routines)，允许 HTTP 请求以及其他常见事务。
- `java.text`：字符串的解析例程，并支持各种人类可读的语言和特定于语言环境的解析。
- `java.util`：[Collections API](https://en.wikipedia.org/wiki/Collections_API) ，这是一种受 [设计模式](https://en.wikipedia.org/wiki/Design_pattern_(computer_science)) 考虑因素影响很大的有组织的数据结构层次结构。

| Source/Destination                                                                                                                                 | Name        | Stream types   | In/out  | Classes                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`byte`](https://en.wikipedia.org/wiki/Byte) [array](https://en.wikipedia.org/wiki/Array_data_type) (`byte[]`)                                     | `ByteArray` | `byte`         | in, out | [`ByteArrayInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ByteArrayInputStream.html), [`ByteArrayOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ByteArrayOutputStream.html)                                                                                                                                                                                                 |
| `char` array (`char[]`)                                                                                                                            | `CharArray` | `char`         | in, out | [`CharArrayReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/CharArrayReader.html), [`CharArrayWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/CharArrayWriter.html)                                                                                                                                                                                                                       |
| [file](https://en.wikipedia.org/wiki/Computer_file)                                                                                                | `File`      | `byte`, `char` | in, out | [`FileInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileInputStream.html), [`FileOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileOutputStream.html), [`FileReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileReader.html), [`FileWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileWriter.html)         |
| [string](https://en.wikipedia.org/wiki/String_(computer_science)) ([`StringBuffer`](https://en.wikipedia.org/wiki/StringBuffer_and_StringBuilder)) | `String`    | `char`         | in, out | [`StringReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/StringReader.html), [`StringWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/StringWriter.html)                                                                                                                                                                                                                                   |
| [thread](https://en.wikipedia.org/wiki/Thread_(computer_science)) (`Thread`)                                                                       | `Piped`     | `byte`, `char` | in, out | [`PipedInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedInputStream.html), [`PipedOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedOutputStream.html), [`PipedReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedReader.html), [`PipedWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedWriter.html) |

| Operation                                                                                       | Name       | Stream types   | In/out  | Classes                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------- | ---------- | -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [buffering](https://en.wikipedia.org/wiki/Buffer_(computer_science))                            | `Buffered` | `byte`, `char` | in, out | [`BufferedInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedInputStream.html), [`BufferedOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedOutputStream.html), [`BufferedReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedReader.html), [`BufferedWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedWriter.html) |
| "push back" last value read                                                                     | `Pushback` | `byte`, `char` | in      | [`PushbackInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PushbackInputStream.html), [`PushbackReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PushbackReader.html)                                                                                                                                                                                                                                         |
| read/write [primitive types](https://en.wikipedia.org/wiki/Primitive_type)                      | `Data`     | `byte`         | in, out | [`DataInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/DataInputStream.html), [`DataOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/DataOutputStream.html)                                                                                                                                                                                                                                             |
| [object serialization](https://en.wikipedia.org/wiki/Object_serialization) (read/write objects) | `Object`   | byte           | in, out | [`ObjectInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ObjectInputStream.html), [`ObjectOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ObjectOutputStream.html)                                                                                                                                                                                                                                     |

## Special purpose packages

- `java.applet`
- `java.beans` [[java-beans]]
    - [`java.beans`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/java/beans/package-summary.html) 包中包含用于开发和操作 bean 的各种类，以及由 [JavaBeans 体系结构](https://en.wikipedia.org/wiki/JavaBeans) 定义的可重用组件。该架构提供了操纵组件属性并在这些属性更改时触发事件的机制。
- `java.awt`
    - [`java.awt`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/java/awt/package-summary.html) （或抽象窗口工具包）提供对一组基本 [GUI](https://en.wikipedia.org/wiki/GUI) 小部件的访问，这些小部件基于底层本机平台的小部件集、GUI 事件子系统的核心以及本机窗口系统和 Java 应用程序之间的接口。它还提供了几个基本的 [布局管理器](https://en.wikipedia.org/wiki/Layout_manager)、与 [剪贴板](https://en.wikipedia.org/wiki/Clipboard_(software)) 和 [拖放](https://en.wikipedia.org/wiki/Drag_and_drop) 一起使用的数据传输包、[输入设备](https://en.wikipedia.org/wiki/Input_device)（例如 [鼠标](https://en.wikipedia.org/wiki/Mouse_(computing)) 和 [键盘）](https://en.wikipedia.org/wiki/Keyboard_(computing)) 的接口以及对支持系统上的 [系统托盘](https://en.wikipedia.org/wiki/System_tray) 的访问。该包与 `javax.swing` 一起包含 JDK 6 中最多数量的枚举（总共 7 个）。
- `java.rmi`
    - [`java.rmi`](https://docs.oracle.com/en/java/javase/19/docs/api/java.rmi/java/rmi/package-summary.html) 包提供 [Java 远程方法调用，](https://en.wikipedia.org/wiki/Java_remote_method_invocation) 以支持在不同 [JVM](https://en.wikipedia.org/wiki/JVM) 中运行的两个 Java 应用程序之间的 [远程过程调用](https://en.wikipedia.org/wiki/Remote_procedure_call)。
- `java.security`
    - 对安全性的支持（包括消息摘要算法）包含在 [`java.security`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/security/package-summary.html) 包中。
- `java.sql` [[jdbc]]
- `javax.rmi`
    - [`javax.rmi`](https://docs.oracle.com/javase/8/docs/api/javax/rmi/package-summary.html) 包使用 RMI over IIOP 协议为应用程序之间的远程通信提供支持。该协议结合了 RMI 和 CORBA 功能。
    - http://java.sun.com/javase/technologies/core/corba/index.jsp
- `javax.swing`
    - 基于 `java.awt` 构建的例程集合，用于提供独立于平台的 [小部件工具包](https://en.wikipedia.org/wiki/Widget_toolkit)。 [`javax.swing`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/javax/swing/package-summary.html) 使用 2D 绘图例程来呈现用户界面组件，而不是依赖于底层本机 [操作系统](https://en.wikipedia.org/wiki/Operating_system)GUI 支持。
- `javax.swing.text.html.parser`
    - 提供了容错 HTML 解析器，用于编写各种 Web 浏览器和 Web 机器人。
- `javax.xml.bind.annotation`
    - 定义了用于自定义 Java 程序元素到 XML 模式映射的注释。
- OMG packages -> remove on [[java11]]
- `org.omg.CORBA`
- `org.omg.PortableInterceptor`

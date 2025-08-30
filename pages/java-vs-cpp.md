---
aliases:
  - Java-vs-cpp
created: 2024-08-02T00:00:00
description: 
modified: 2025-07-25T23:19:50
tags:
  - cpp
  - java
title: Java-vs-cpp
wikipedia: https://en.wikipedia.org/wiki/Comparison_of_Java_and_C%2B%2B
---

# [[java|Java]] vs [[cpp|Cpp]]

| Items                 | Java    | cpp     |
| --------------------- | ------- | ------- |
| 面向对象 (封装/继承/多态)        | ✔       | ✔       |
| 方法重载                  | ✔       | ✔       |
| 指针 (直接访问内存)            | ✖       | ✔       |
| 类多继承                  | ✖(接口替代) | ✔       |
| 操作符重载                 | ✖       | ✔(复杂 ++) |
| 内存管理垃圾回收机制 (GC) / 内存安全 | ✔       | ✖       |


- **虚函数**
  description: 为了多态
  - Java 没有虚函数的概念 -> Java 普通函数 == C++ 虚函数
	- **动态绑定**是 Java 的默认行为
	- 如果 Java 中不希望某个函数具有虚函数特性，可以加上 final 关键字变成非虚函数
- **抽象函数(纯虚函数)**
  description: 为了定义接口

```cpp
        virtual void print() = 0;
```

```java
  abstract void print();
```

- **抽象类**
  description: "父类中既包括子类共性函数的具体定义，也包括需要子类各自实现的函数接口"
  - C++ 中抽象类只需要包括纯虚函数，既是一个抽象类。如果仅仅包括虚函数，不能定义为抽象类，因为类中其实没有抽象的概念。
  - Java 抽象类是用 abstract 修饰声明的类。
- **接口**
  description: "为了形成一种规约, 不能有 普通成员变量 + 非纯虚函数"
  - C++ 中接口其实就是全虚基类。
  - Java 中接口是用 interface 修饰的类。
- **小结**
  - C++ 虚函数    ==  Java 普通函数
  - C++ 纯虚函数  ==  Java 抽象函数
  - C++ 抽象类    ==  Java 抽象类
  - C++ 虚基类    ==  Java 接口
- [JAVA – 虚函数、抽象函数、抽象类、接口](https://www.runoob.com/note/40084)

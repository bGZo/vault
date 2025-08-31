---
aliases:
  - 注解
  - Java 注解
created: 2025-01-13T20:06:17
description: Java 注解；放在Java源码的类、方法、字段、参数前的一种特殊“注释”；注解是一种用作标注的 "元数据"；被编译器直接忽略，被打包进入class文件
modified: 2025-08-31T13:32:45
title: Java 注解
---

# Java 注解

## 分类

- 编译器使用 (编译即丢)
    - `@Override`：让编译器检查该方法是否正确地实现了覆写；
    - `@SuppressWarnings`：告诉编译器忽略此处代码产生的警告
- 由工具处理 `.class` 文件使用的注解
	- 被编入 `.class`, 但不会常驻内存
	- 被一些底层库使用，一般不必处理
- (**最常用**) 在程序运行期能够读取的注解，它们在加载后一直存在于 JVM 中
    - 一个配置了 `@PostConstruct` 的方法会在调用构造方法后自动被调用
      （Java 提供，JVM 并不识别）
      - ` @PostConstruct`
        description: java/5 提供；是和@PreDestroy 两个作用于 Servlet 生命周期的注解；实现 Bean 初始化之前和销毁之前的自定义操作
        source: https://blog.csdn.net/skh2015java/article/details/117751380

## 定义

- 使用 `@interface` 语法来定义
- 注解的参数类似无参数方法，可以用 `default` 设定一个默认值

## 元注解 (meta annotation)

- `@Target`: 定义 `Annotation` 能够被应用于源码的哪些位置
    - 类或接口：`ElementType.TYPE`；
    - 字段：`ElementType.FIELD`；
    - 方法：`ElementType.METHOD`；
    - 构造方法：`ElementType.CONSTRUCTOR`；
    - 方法参数：`ElementType.PARAMETER`。
    - 只有一个元素时，可以省略数组的写法????
- `@Retention`: 定义了 `Annotation` 的生命周期
	- 仅编译期：`RetentionPolicy.SOURCE`；
	- 仅 class 文件：`RetentionPolicy.CLASS`；(default)
	- 运行期：`RetentionPolicy.RUNTIME`。(more)
- `@Inherited`: 子类是否可继承父类
- `@Repeatable`: 这个元注解可以定义 `Annotation` 是否可重复

## Collections

- [[~Spring-Boot中最常用的-100-个注解-程序员晓凡-博客园|Spring Boot 中最常用的 100 个注解 - 程序员晓凡]]
- ` @Autowired`: 对成员变量、方法和构造函数进行标注，来完成自动装配的工作；@Autowired 是根据类型进行自动装配的，如果需要按名称进行装配，则需要配合@Qualifier 使用；Since Spring 2.5；[@Autowired 的作用是什么？ - 知乎](https://zhuanlan.zhihu.com/p/91654572)

## References

- [处理注解 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1252599548343744/1265102026065728)

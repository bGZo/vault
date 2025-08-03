---
aliases:
  - Java Vs Python
  - java-vs-python
  - python-vs-java
created: 2025-07-25T23:19:30
modified: 2025-07-25T23:49:01
title: Java Vs Python
---

# [[java|Java]] Vs [[python|Python]]

## Python 没有像 Hutool 一样的工具类？

> Python 没有像 Hutool（Java 的工具库）那样的“工具类”概念，但 Python 有很多功能强大的标准库和第三方库，能实现 Hutool 的大部分功能。Python 更倾向于“函数式”工具方法，而不是 Java 的静态工具类。[^function-vs-statio] #copilot

- 字符串处理：`str`、`re`（正则表达式）
- 日期时间：`datetime`、`dateutil`
- 文件操作：`os`、`shutil`、`pathlib`
- 集合工具：`collections`
- 加密解码：`hashlib`、`base64`
- 网络请求：`requests`
- JSON/XML 处理：`json`、`xml.etree.ElementTree`

如果你需要类似 Hutool 的“工具类”，可以自己封装 Python 的函数或使用第三方库（如 `toolz`、`boltons`）。

## 最大的区别：

本质区别是语言的组织方式和语法习惯，功能上其实都能实现类似的灵活性。

### 一等公民

Python 中，函数是一等公民；可以随意定义、传递、组合，无需类包裹，语法更简洁。

Java 中，类是一等公民；虽然支持函数式编程，但工具方法必须放在类里，函数式语法也比 Python 更繁琐。

### 面向对象

1. Python 时动态语言，所以类型在运行时决定，静态语言的 Java 则是在编译时决定；
2. Python 可以多继承，Java 不可以
3. 语法上 Python 更加简单，无需显式声明类型和访问修饰符。
	1. 没有修饰符导致 Python 的保护机制不严格
	2. 主要靠约定，（如下划线）
4. 构造函数与析构函数
	1. Python 用 `__init__` 和 `__del__`
	2. Java 用类名和 `finalize()`
5. 抽象类
	1. Java 有专门的接口和抽象类语法，Python 用抽象基类（ABC）或鸭子类型实现类似功能。

---

[^function-vs-statio]: java 把工具类方法封装在类中，通过类名调用，如 `StringUtil.isEmpty(str)`；Python 放在模块内，通过模块名调用，如 `os.path.join(a, b)`；前者更加面向对象，后果更加面向组合式调用；

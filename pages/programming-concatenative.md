---
draft: true
aliases:
  - 串接式编程语言
  - Concatenative
created: 2024-12-26T21:01:32
modified: 2025-08-31T00:19:52
title: 串接式编程语言
wikipedia: https://en.wikipedia.org/wiki/Concatenative_programming_language
---
# 串接式编程语言

串接式（concatenative）编程语言，是无点的计算机编程语言，在其中所有表达式都指示为函数，而表达式的并列指示函数复合。串接式编程语言将常见于其他编程样式中的函数应用，替代为函数复合，作为建造子例程的缺省方法。

point-free computer programming language in which all expressions denote functions, and the juxtaposition of expressions denotes function composition

```shell
y = foo(x)
z = bar(y)
w = baz(z)
x foo bar baz
```

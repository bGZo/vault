---
draft: true
aliases:
  - 函数级编程
  - 无点（point-free）样式
  - 隐式编程
  - Programming-tacit
created: 2024-12-15T11:24:00
modified: 2025-08-31T00:18:35
title: 隐式编程
wikipedia: https://en.wikipedia.org/wiki/Tacit_programming
---
# 隐式编程

是一种编程范型。其中函数定义不标示所要运算的被称为“点”的参数，转而函数定义只是其他函数的复合，比如那些操纵参数的组合子。隐式编程有着理论价值，因为严格的使用复合导致程序适配于等式推理。隐式编程是特定编程语言的天然样式，这包括了 APL 的一些现代实现和方言，和串接式语言比如 Forth。由于缺少参数命名，认为这种风格导致了不必要的晦涩难懂的人，给它起了个绰号叫做“无意义”（pointless）风格。

point-free style, is a programming paradigm in which function definitions do not identify the arguments (or "points") on which they operate

## Support

  - [[python]]
  - [[programming-functional]]
  - APL family
  - Stack-based
  - Unix [[ipc]] PIPE

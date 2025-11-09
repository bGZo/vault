---
draft: true
aliases:
  - 块编程
  - Programming-block
created: 2025-08-30T20:19:29
modified: 2025-08-30T20:39:53
title: 块编程
wikipedia: https://en.wikipedia.org/wiki/Block_(programming)
---
# 块编程

在计算机编程中，块（block）或译为程序区块、代码块，是将源代码组织在一起的词法结构。块构成自一个或多个声明和语句。编程语言允许创建块，包括嵌入其他块之内的块，就叫做块结构编程语言。块和子程序是结构化编程的基础，结构化所强调的控制结构可以用块来形成的。

在编程中块的功能，是确使成组的语句被当作如同就是一个语句，限定在一个块中声明的对象如变量、过程和函数的词法作用域，使得它们不冲突于在其他地方用到的同名者。在块结构编程语言中，在块外部的对象名字在块内部是可见的，除非它们被声明了相同名字的对象所遮掩。

- 块和子程序是结构化编程的基础
- 结构化所强调的控制结构是用块来形成的

## Syntax

  - ALGOL blocks are delimited by the keywords "`begin`" and "`end`" or equivalent
    - ALGOL 68 uses parentheses.
  - [[system-c]], blocks are delimited by curly braces - "`{`" and "`}`".
  - MS-DOS Batch Lang
    - `()`
  - [[python]]
    - indentation (越位规则)
    - 源于 ISWIM 使用缩进表示块结构
    - Lang -> occam / Genie
  - Lisp s-expressions
    - with a syntactic keyword such as prog or let (as in the Lisp family)
  - 1974 年 Edsger W. Dijkstra 的守卫命令语言中，条件和迭代代码块可使用块保留字反写来终止
    - `if ~ then ~ elif ~ else ~ fi`
    - `case ~ in ~ out ~ esac`
    - `for ~ while ~ do ~ od`

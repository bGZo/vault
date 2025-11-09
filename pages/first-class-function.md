---
draft: true
aliases:
  - 头等函数
created: 2025-03-22T16:28:35
modified: 2025-08-30T18:58:21
title: 头等函数
wikipedia: https://en.wikipedia.org/wiki/First-class_function#Assigning_functions_to_variables
---
# 头等函数

函数被当作 [头等公民](https://zh.wikipedia.org/wiki/%E5%A4%B4%E7%AD%89%E5%85%AC%E6%B0%91 "头等公民")。这意味着，函数可以作为别的函数的参数、函数的返回值，赋值给变量或存储在数据结构中。

- have first-class functions if it treats functions as first-class citizens
  - supports passing functions as arguments to other functions
  - returning them as the values from other functions
  - assigning them to variables or storing them in data structures
- There are certain implementation difficulties in passing functions as arguments or returning them as results, especially in the presence of non-local variables introduced in nested and anonymous functions
  - Historically, these were termed the **funarg problems**, the name coming from "function argument"

## Concepts

- Higher-order functions: passing functions as arguments
- Anonymous and nested functions
- Non-local variables and closures | 非局部变量和闭包
- Higher-order functions: returning functions as results
- Assigning functions to variables
- Equality of functions
    - Extensional equality | 外延相等
    - Intensional equality | 内涵相等
    - Reference equality | 引用相等

## [[skills/language/index]] Support

![[image_1656431254761_0.png]]


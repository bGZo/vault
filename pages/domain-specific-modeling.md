---
draft: true
aliases:
  - 领域专用建模
  - 特定域建模
  - domain specific modeling
  - Domain-specific
  - DSM
created: 2022-01-01T00:00:00
modified: 2025-08-31T12:51:16
tags:
  - lang-programming
title: 领域专用建模
wikipedia: https://en.wikipedia.org/wiki/Domain-specific_modeling
---
# 领域专用建模

它系统使用图形化特定域语言（DSL），表现系统的各个方面。DSM 的语言倾向于支持比通用建模语言更高级别的抽象，因此需要较少的 effort 和更少的底层细节来描述特定系统。

1. **核心是 [[language-domain-specific|DSL]] （领域专用语言）**
    - DSM 不是简单的“按领域思路设计”，而是 **为特定领域设计一种专门的建模语言**。
    - 这门语言通常是图形化的（但也可能是文本化的），它的抽象程度比 UML、BPMN 这种通用建模语言更高。
2. **模型 = 程序生成的源**
    - 在 DSM 中，开发者不直接写低层代码（或只写很少），而是通过 DSL 来描述业务/系统。
    - 工具链会根据这些模型自动生成运行的系统代码（或很大一部分）。
3. **与通用建模的区别**
    - UML 等通用建模语言 → 面向“所有领域”，但抽象不够贴近某个具体领域，导致需要很多细节。
    - DSM → 针对一个特定领域定制语言，表达更直接、抽象更高，工程效率更高。

## References

- http://dsl-course.org/zoo-of-dsls/
- [[language-specification|规约语言]]

---
aliases:
  - lang/modeling/unified
  - Uml
  - UML
created: 2025-03-22T16:28:35
description: Unified Modeling Language; UML打算成為可以對並發和分布式系統的標準建模語言; UML使用一套與Java語言或其他面向對象語言等價物. 同時也是本體論等價物的圖形標記
modified: 2025-07-17T21:46:41
tags:
  - [software-pattern]
title: UML
---

# UML

画类图（Class Diagram）的

## Outline

### History

- 1997 年
    - UML 被對象管理組織接納為標準，並在此之後受該組織管理
- 2005 年
    - UML 被國際標準化組織接納為一種標準自此，該標準被定期修訂以涵蓋 UML 的最新版本
    - 軟件工程中，大多數從業者不使用 UML，而是產生非正式的手繪圖
    - 不過，這些圖例中仍往往包括 UML 的元素

### Module 模型 (3)

- 功能模型
    - 从用户的角度展示系统的功能
    - 用例图
- 对象模型
    - 采用对象，属性，操作，关联等概念展示系统的结构和基础
    - 类别图
    - 对象图
- 动态模型
    - 展现系统的内部行为
    - 序列图
    - 活动图
    - 状态图

### Shape 图形

- ![[image_1655795835076_0.png]]
- 结构性图形（Structure diagrams）强调**系统式的建模**
    - 静态图（static diagram）
    - 类图（Class Diagram）
      - ![[image_1655796205788_0.png]]
      - 依赖 (Dependency)
        - ![[image_1655796723111_0.png]]
      - 关联 (Association)
        - ![[image_1655796730332_0.png]]
      - 聚合 (Aggregation)
        - ![[image_1655796737007_0.png]]
      - 组合 (Composition)
        - ![[image_1655796742972_0.png]]
      - 继承 (Generalization)
        - ![[image_1655796754787_0.png]]
      - 实现 (Implementation)
        - ![[image_1655796763181_0.png]]
    - 对象图（Object diagram）
      - ![[image_1655796219356_0.png]]
    - 包图（Package diagram）
      - ![[image_1655796229157_0.png]]
    - 实现图（implementation diagram）
    - 组件图（Component diagram）
      - ![[image_1655796253349_0.png]]
    - 部署图（Deployment diagram）
      - ![[image_1655796261640_0.png]]
    - 剖面图
    - 复合结构图
- 行为式图形（Behavior diagrams）强调**系统模型中触发的事件**
    - 活动图
    - 状态图
    - 用例图
- 交互性图形（Interaction diagrams）强调**系统模型中的资料流程**:
    - 属于行为图形的子集合
    - 通信图
    - 交互概述图（UML 2.0）
    - 时序图（UML 2.0）
    - 时间图（UML 2.0）

### Use Case 用例

- ![[image_1648016765556_0.png]]

## References

- [Unified Modeling Language - Wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
- [设计模式之 UML 类图 - 知乎](https://zhuanlan.zhihu.com/p/24576502)
- https://www.youtube.com/watch?v=R9SXpaD_aB4
- [UML类图的6种连线示意 - 简书](https://www.jianshu.com/p/48de81a8f0ab)
- [er图 和 类图 区别 - Google Search](https://www.google.com.hk/search?q=er%E5%9B%BE+%E5%92%8C+%E7%B1%BB%E5%9B%BE+%E5%8C%BA%E5%88%AB&newwindow=1)

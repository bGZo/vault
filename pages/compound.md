---
draft: true
title: 复利
aliases:
  - 复利
  - 利滚利
  - 驴打滚
created: 2022-05-25T11:37:00
modified: 2025-03-16T21:52:11
wikipedia: https://en.wikipedia.org/wiki/Compound_interest
---
我们可以通过减少复利的时间间隔，来达到利息的最大化. (PS: 有上限)

![[2a6gDHfWQGA-人生中最重要的概念-复利-是什么-想贷款和分期就必须要了解它；李永乐老师讲自然对数的底e#Source]]

### 自然对数的底 / 欧拉数 e

假设有这样一个式子

$\begin{align}  (1 + \frac{1}{n} )^n = x  \tag{1} \end{align}$

- 当 $n=1$ 时, $x=2$
- 当 $n \rightarrow \infty$ 时，得到 $x = e = 2.7 1828 1828 45 90 45 ...$ 即 $e = \lim_{n \rightarrow \infty} (1+\frac{1}{n})^n$

泰勒展开: $e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + ...$

### 复利

单利即一年到头结算利息。而多利则将一年分为多次结算利息。即我们可以得到一个公式:

$\begin{align}  PV \times ( 1 + \frac{r}{n} ) ^ n = FV  \tag{2} \end{align}$

$PV(Present Value)$ 为初值

$r$ 为名义利率

$n$ 为期数

$FV(Future Value)$ 为终值

则我们假设有 100 的本金，银行说明具有 $10\%$ 的利率

月复利 $(n=12)$: $100 \times ( 1 + \frac{0.1}{12} )^{12} = 110.47$

日复利 $(n=365)$: $100 \times ( 1 + \frac{0.1}{365} )^{356} = 110.51$

连续复利 ($n \rightarrow \infty$), 此时 $(2)$ 后半部分 $(1 + \frac{r}{n} )^n = e ^ r$, 存在上限.

后记: 我们可以将 周期内的固定 利率/回报率 定义为 $i(interest)$, 则 $(2)$ 将简化为:

$\begin{align}  PV \times ( 1 + i ) ^ n = FV \tag{3} \end{align}$

从而得到回报率公式

$\begin{align} \sqrt[n]{ ( \frac{FV}{PV} ) } - 1 \tag{4} \end{align}$

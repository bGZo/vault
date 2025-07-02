---
title: 字体
aliases:
  - 字体
created: 2023-08-21T12:54:40
modified: 2025-06-07T13:38:44
description: 
tags: 
type:
---

## [[skills/fundamantal/index|扫盲]]

### 衬线 (serif)

字母结构笔画之外的装饰性笔画

### 无衬线体 (sans-serif)

没有衬线的字体

### 磅转换

1 磅约等于 0.35 毫米, 即一个 10 磅的文字, 其高度约等于 3.5 毫米

| **磅（1-1638）** | **字号** |
| :--------------: | :------: |
| 42 | 初号 |
| 36 | 小初 |
| 26 | 一号 |
| 24 | 小一号 |
| 22 | 二号 |
| 18 | 小二号 |
| 16 | 三号 |
| 15 | 小三号 |
| 14 | 四号 |
| 12 | 小四号 |
| 10.5 | 五号 |
| 9 | 小五号 |
| 7.5 | 六号 |
| 6.5 | 小六号 |
| 5.5 | 七号 |
| 5 | 八号 |

## Collections

### 英文字体

| Sence           | Fonts                                         |
| --------------- | --------------------------------------------- |
| Standard （标准）   | Times New Roman                               |
| Sans-serif（非衬线） | [Arial](https://zh.wikipedia.org/zh-cn/Arial) |
| Serif（衬线）       | Times New Roman                               |
| Monospaced（等宽）  | Sarasa Mono SC                                |
| Cursive（草书）     | Comic Sans MS                                 |
| Fantasy（艺术字）    | Impact                                        |

- Press Start 2P: OFL, 位图字体, [Google](https://fonts.google.com/specimen/Press+Start+2P#standard-styles).
- Lato Regular: OFL, [Google](https://fonts.google.com/specimen/Lato).
- Roboto: AL, [Google](https://fonts.google.com/specimen/Roboto)

### 中文字体
- 文泉驿的字体虽然是开放的，但似乎不可随便商用, 方正黑体、方正书宋、方正仿宋、方正楷体这四款方正的字体可以免费商用
- 方正黑体
- 方正楷体
- 方正书宋
- 方正仿宋
- 思源黑体
- 文泉驿字体
- 华文黑体
- Verdana: Microsoft Corporation, 需要购买
- Yu Gothic UI: LM([License Microsoft fonts](https://www.fonts.com/content/microsoft-typography)), [MircoSoft](https://docs.microsoft.com/en-us/typography/font-list/yu-gothic).

> [!note]
> **微软公司斥巨资委托方正字体公司专门为 Vista 系统设计制作了微软雅黑 (方正兰亭黑)**, 微软公司只拥有微软雅黑的使用权, 而版权在方正手中. 我们仅可以在 Windows 系统中使用微软雅黑！脱离 Windows 平台的一切商业行为, 都属于侵权行为, 同时在 Windows 系统下, 商业行为也不被允许, 包括网页设计中, 主动调用微软雅黑字体, 更不可以以图片的形式在网页中用到微软雅黑！
>
> via: [微软雅黑字体侵权？推荐20款无版权的开源字体！ - 知乎](https://zhuanlan.zhihu.com/p/49049779)

### 编程字体 —— Mono / Nerd Fonts

留意对字体编码 Unicode 要优先考虑简中, 否则会出现字体变形的难受字样.

- 版权方面, 微软雅黑是从 Window 上面提取的版本, 所以存在版权问题. 只可以个体使用, 不可用于商业环境; 更纱黑体由 兆邦中国 (Zhaobang China) 在 [微软商店免费下载](https://www.microsoft.com/zh-cn/p/%E6%9B%B4%E7%BA%B1%E9%BB%91%E4%BD%93/9mw0m424ncz7) 使用.
- [Microsoft Yahei Mono | 微软雅黑官方等宽字体 ](https://github.com/cheny-m/Microsoft-Yahei-Mono).
- [Sarasa Gothic / 更纱黑体 / 更紗黑體](https://github.com/be5invis/Sarasa-Gothic).
- [FiraCode | 符号连体](https://github.com/tonsky/FiraCode).
- [Adobe Fonts-Source Code Pro | 全英文环境较好](https://github.com/adobe-fonts/source-code-pro).
- [Google Font](https://fonts.google.com)
- [中文字体 Ubuntu](https://wiki.ubuntu.org.cn/%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87%E5%AD%97%E4%BD%93)
- [Free-Chinese-Fonts](http://zenozeng.github.io/Free-Chinese-Fonts/)
- [coding-fonts](https://github.com/chriscoyier/coding-fonts)
- [[JetBrains-JetBrainsMono|JetBrainsMono]]

> [!tip]
> MD > FA > CODI >...

<iframe src="https://www.youtube.com/embed/w9wqIEk5Cqo" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=w9wqIEk5Cqo' target='_blank' class='external-link'>https://www.youtube.com/watch?v=w9wqIEk5Cqo</a></center>

[[ryanoasis-nerd-fonts]] 的核心特点是将众多常见图标库（如 Font Awesome、Devicons、Octicons 等）合并到字体中，以便程序员、系统管理员和开发者在终端、编辑器和命令行工具中使用。

==如果我的 General / Mono 字体没有现成的打包 Nerd 字体, 怎么办?==

### 字体选择 20221020

我将浏览器默认字体换成 LXGW 之后, 发现有很多网站混杂了相当多的字体, 当然阅读体验被毁得一团乱, 但是, 我发现绝大多数 网站都有在使用 Arial 这个字体, 尤其是在国外, 频率非常高. 之后查了查资料, 关于这个字体和非衬线字体有较大的争论, 尤其是人们在互相争论使用哪一个字体的时候.

一个具体的研究表明在 12px 之下的阅读还是衬线字体比较好辨别, 但是随着字体大小的变化, 人对两者的阅读体验开始持平, 甚至可以说, 在字体大小非常大的时候, 两者的区别已经无所谓了.

再者关于 阅读体验 是一个非常主观的东西, 目前这个东西还没有什么定论, 有的人面对美观的字体, 阅读速度反而可以升高, 但是有人则不然.

<iframe src="https://www.youtube.com/embed/41i9EN9l8uc" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=41i9EN9l8uc' target='_blank' class='external-link'>https://www.youtube.com/watch?v=41i9EN9l8uc</a></center>

### 方块字的历史怪象 —— 中竖门 & 门

![](https://raw.githack.com/bGZo/assets/dev/2025/202501311258809.png)

微软雅黑默认状态下部分字符显示为日文字符, 如 `门` 就会显示 ' 中间一竖的 `门`'. 纠正方法换字体 --`文泉译米` 即可

Profromence differences are related with [**CJK Unified Ideographs**](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs), and relating to [CJK Font](https://en.wikipedia.org/wiki/List_of_CJK_fonts). And Some Font display the Japan Font as default pattern, such this `Mircosoft YaHei` in ubuntu when the sys encoding is `US_Utf-8`, but why the window is not such situation?<sup>[3](#j3)</sup>. Some more details [FAQ](https://www.unicode.org/faq/han_cjk.html) with it. By th way, Japan encodes CIJ and Chinese encodes GB.

## References

- https://fonts.google.com
    - [ ] 创建一个在线免费字体预览网站
        - 背景：说实话中文字体界实在是太乱了, 在使用过 Google Fonts 之后一直想找替代的网站, 简中 SEO 较高的总是指向诸如 xxx 下载站, pc 下载站, 第一字体网 之类的质量较低下 (缺乏**字体介绍**, **使用许可**, **作者详情**, **官方网站**等) 的网站, 这种资源德不配位真的让我有点受不了. 简中的铜臭气也渗透了出来.
        - 我们总是不把版权问题摆在前面, 总是先入为主地 " 拿来就用 ", 也不问有什么代价, 乐于做伸手党, 久而久之真的沦为了理所当然的事情. 因为每一片雪花都很小, 所以雪崩不怪任何人, 甚至伸手党们拉帮结伙开始反攻作者, 真的让人啼笑皆非.
- http://www.fonts.net.cn
- https://v2ex.com/t/517747
- https://jedi.org/opera/FontTest/
- https://v2ex.com/t/627989
- [[~The-Type—Basics-衬线]]
- [[~一条命令搞定Linux字体渲染——Ubuntu系发行版微软雅黑+宋体终极解决方案]]
- [[~serif-sans-serif-monospace-cursive和fantasy]]

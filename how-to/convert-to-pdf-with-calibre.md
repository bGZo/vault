---
aliases:
  - 如何用 Calibre 转化为 PDF
created: 2023-04-12T10:06:04
draft: false
modified: 2025-11-14T06:39:41
title: 如何用 Calibre 转化为 PDF
---

# 如何用 [[kovidgoyal-calibre|Calibre]] 转化为 PDF

简单的讲，直接在操作栏选择转换书籍，然后选择 PDF 即可，但是导出书籍的格式不一，最好还是有一些约定好的配置，兼顾阅读和打印，也可以避免版权问题。

## 需要准备的字体

- https://source.typekit.com/source-han-serif/cn/
- https://github.com/be5invis/Sarasa-Gothic
- https://github.com/laishulu/Sarasa-Term-SC-Nerd

善用 Brew：

```shell
# 思源宋体
brew install --cask font-noto-serif-cjk
brew install --cask font-source-han-serif-vf
# 更纱黑体
brew install --cask font-sarasa-gothic
# 更纱黑体等宽
brew tap laishulu/homebrew
brew install font-sarasa-nerd
# 源流明體
brew install --cask font-genryumin
```

## 配置

- 转换书籍 -> 输出格式 PDF
- 界面外观 -> 字体 -> 最小行高 -> 180%
- 页面设置
    * 输出配置文件 -> 默认配置文件
    * 输入配置文件 -> 默认配置文件
* PDF 输出
    * 纸张大小 -> A4
    * 衬线字体（正文） -> 思源宋体（Noto Serif CJK SC / Source Han Serif SC VF）/ 源流明體（GenRyuMin2 TC）[^why-song-font]
    * 非衬线字体（标题/普通 UI） -> 更纱黑体（Sarasa Gothic SC）
    * 等宽字体（代码/表格/CLI） -> 更纱黑体 Mono SC（Sarasa Mono SC）
    * 默认字体大小 -> 16 px
    * 等宽字体大小 -> 12 px

[^why-song-font]: 在实际转换的过程中，一些字体其实会印象文字的排版，具体原理不清楚，在转换某本 EQUB 的时候，使用思源宋体在一些段落中就无法正常划线，复制下来文字顺序也是乱的，尝试 Pandoc 之后。觉得 pandoc 的排版太难弄了，最后换了个源流明體就好多了。这方面还没有一个定论 #gtd/todo

## 参考

- [[adobe-fonts-source-han-serif|source-han-serif]]
- [[ButTaiwan-genryu-font|genryu-font]]
- [[be5invis-Sarasa-Gothic|Sarasa-Gothic]]
- [[lxgw-LxgwWenKai|LxgwWenKai]]
- https://lishouzhong.com/article/note/uncategoried/Calibre%20%E7%9B%B8%E5%85%B3/
- [calibre有替代品吗 (bgm.tv)](https://bgm.tv/group/topic/373701) #calibre
- [借助 Calibre 处理电子书的流程和技巧 - 少数派 (sspai.com)](https://sspai.com/post/57005)
- [Use advanced book creation options in Pages - Apple Support](https://support.apple.com/en-us/HT202066)
- [Export InDesign documents to an EPUB format](https://helpx.adobe.com/indesign/using/export-content-epub-cc.html)
- https://commandnotfound.cn/linux/1/519/mutool-%E547D%E4EE4
- https://github.com/qpdf/qpdf
- https://www.v2ex.com/t/913812
- https://ghostscript.com/releases/index.html

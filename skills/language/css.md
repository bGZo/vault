---
aliases: Cascading Style Sheets, 层叠样式表, 串样式列表, 级联样式表, 串接样式表, 阶层式样式表
tags: domain-specific-modeling web
description: W3C 的推荐标准; 一种用来为结构化文档（如HTML文档或XML应用）添加样式（字体、间距和颜色等）的计算机语言，由W3C定义和维护
type: lang/programming
created: 2024-12-08T21:26:21
modified: 2025-03-22T16:13:02
---

## What

### Standards 显示统一标准化
### [[csstools-sanitize.css]]
#### [[csstools-normalize.css]]

是一个很小的 CSS 文件，但它在默认的 HTML 元素样式上提供了跨浏览器的高度一致性。相比于传统的 `CSS reset` ， `Normalize.css` 是一种现代的、为 HTML5 准备的优质替代方案。 `Normalize.css` 现在已经被用于 [Twitter Bootstrap](http://getbootstrap.com/) 、 [HTML5 Boilerplate](http://html5boilerplate.com/) 、 [GOV.UK](http://www.gov.uk/) 、 [Rdio](http://www.rdio.com/) 、 [CSS Tricks](http://css-tricks.com/) 以及许许多多其他框架、工具和网站上。

使用：

- 将 `normalize.css` 作为你自己项目的基础 CSS，自定义样式值以满足设计师的需求
- 引入 `normalize.css` 源码并在此基础上构建，在必要的时候用你自己写的 CSS 覆盖默认值
参考：
- [http://nicolasgallagher.com/about-normalize-css/](http://nicolasgallagher.com/about-normalize-css/)
- [https://jerryzou.com/posts/aboutNormalizeCss/](https://jerryzou.com/posts/aboutNormalizeCss/)

> [!note]
> [normalize.css](https://github.com/csstools/normalize.css) and [sanitize.css](https://github.com/csstools/sanitize.css) correct browser bugs while carefully testing and documenting changes.
  normalize.css styles adhere to css specifications.
  sanitize.css styles adhere to common developer expectations and preferences.
  [reset.css](http://meyerweb.com/eric/tools/css/reset/) unstyles all elements.
  Both sanitize.css and normalize.css are maintained in sync.
  via: [csstools/sanitize.css: A best-practices CSS foundation](https://github.com/csstools/sanitize.css)

### unit:%, em, rem, px, vh, vw

- **% –** The % unit is used to set the font-size relative to the current font-size.
- **em –** It is used to set the relative size. It is relative to the font-size of the element.
**Note:** Here 2em meaning 2times the size of current font.
- **rem –** Relative to the browser base font-size.

> [!note]
> Inside a sinlge document, **the length of a REM unit is everywhere the same**, it can just differ between documents. EM on the other side can differ between every element, because it is relative to the elements own font-size (excpetion is the font-size itself, in it **EM is relative to the parent**).
REM is the newer unit, older browsers don't support it.
via: [PX to REM converter (instantly and bidirectional)](https://nekocalc.com/px-to-rem-converter)

- **px –** It mark: s the font-size in terms of pixels. (96px = 1in)
- **vh –** Relative to 1% of the height of the viewport.
- **vw –** Relative to 1% of the width of the viewport.

参考

- [CSS units - %, em, rem, px, vh, vw - GeeksforGeeks](https://www.geeksforgeeks.org/css-units-em-rem-px-vh-vw/)
- [PX to REM converter (instantly and bidirectional)](https://nekocalc.com/px-to-rem-converter)

### Document
- `position`: the position of an element in a document
    - static
    - relative
    - absolute
    - fixed
    - sticky
- `z-index`

## References

  - [CSS（层叠样式表） | MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS)
  - [CSS 合法颜色值](https://www.w3school.com.cn/cssref/css_colors_legal.asp)
  - [CSS 颜色](https://www.w3school.com.cn/cssref/css_colors.asp)
  - [CSS Zen Garden: The Beauty of CSS Design](http://www.csszengarden.com/)

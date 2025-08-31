---
aliases:
  - 色彩
  - 颜色
  - Color
created: 2025-04-05T23:45:45
modified: 2025-08-30T23:21:49
title: 颜色
---

# 颜色

## Palette 调色板 🎨🔴🟠🟡🟢🔵🟣🟤

### Custom

```dataviewjs
const raw = `
#FEDFE1 樱
#f09199 Bangumi
#cf577b Money(RMB)
#268dcd Douban Movie
#58402a Douban Book
`;

const colors = raw.trim().split("\n").map(line=>{
  const [hex,...rest] = line.trim().split(/\s+/);
  return {hex, label: rest.join(" ")};
});

const wrap = dv.el("div","");
for (const {hex,label} of colors){
  const item = wrap.createEl("span", { text: label + ':' + hex });
  Object.assign(item.style, {
    display: "inline-block",
    padding: "4px 10px",
    margin: "4px",
    borderRadius: "6px",
    background: hex,
    color: "#fff",
    fontWeight: "500"
  });
  item.setAttribute("title", hex); // hover 可见色号
}
```

### [[ozh-github-colors|Github Colors]]

```dataviewjs
const raw = `
#d4a788 Rust
#555555 C
#e0587e C++
#a77530 Java
#3e8622 C#
#4eaad3 Go
#a17dfb Kotlin
#3f7287 TypeScript
#f0e16a JavaScript
#6b1b1b Ruby
#4672a1 Python
#d15735 HTML
#514077 CSS
#4e7729 Makefile
#4495c4 Perl
#000078 Lua
#525e92 PHP
`;

const colors = raw.trim().split("\n").map(line=>{
  const [hex,...rest] = line.trim().split(/\s+/);
  return {hex, label: rest.join(" ")};
});

const wrap = dv.el("div","");
for (const {hex,label} of colors){
  const item = wrap.createEl("span", { text: label + ':' + hex });
  Object.assign(item.style, {
    display: "inline-block",
    padding: "4px 10px",
    margin: "4px",
    borderRadius: "6px",
    background: hex,
    color: "#fff",
    fontWeight: "500"
  });
  item.setAttribute("title", hex); // hover 可见色号
}
```

## [[terminal|终端]]

- [brewer](https://github.com/adi1090x/termux-style/blob/master/colors/base16-brewer-dark.properties)
- [eighties](https://github.com/adi1090x/termux-style/blob/master/colors/base16-eighties-dark.properties)
- [materia](https://github.com/adi1090x/termux-style/blob/master/colors/base16-materia.properties)
- [tomorrow](https://github.com/adi1090x/termux-style/blob/master/colors/base16-tomorrow-dark.properties)
- [ocean](https://github.com/adi1090x/termux-style/blob/master/colors/base16-ocean-dark.properties)
- [grayscale](https://github.com/adi1090x/termux-style/blob/master/colors/base16-grayscale-dark.properties)
- [greenscreen](https://github.com/adi1090x/termux-style/blob/master/colors/base16-greenscreen-dark.properties)
	- replace logic: https://github.com/adi1090x/termux-style/blob/233d39b5129f67fb42debc09433ccfbb11ab9c3a/tstyle#L98-L105

## [[navigation|Navigation]]

- [Color Palettes](https://www.color-hex.com/color-palettes/)
- [NIPPON COLORS - 日本の伝統色](https://nipponcolors.com/)
	- 山寨 | [zhongguose － 传统颜色](http://zhongguose.com/)
- 护眼色 | [Solarized](https://ethanschoonover.com/solarized/)
	- [GitHub - jan-warchol/selenized: Solarized redesigned: fine-tuned color palette for programmers with focus on readability.](https://github.com/jan-warchol/selenized)
- 渐变色 | [ghosh/uiGradients: 🔴 Beautiful colour gradients for design and code](https://github.com/Ghosh/uiGradients)
- 渐变色 | [Fresh Background Gradients | WebGradients.com 💎](https://webgradients.com/)
- 色轮 | [Paletton - The Color Scheme Designer](https://paletton.com/#uid=1000u0kllllaFw0g0qFqFg0w0aF)
- [Design Seeds](https://www.design-seeds.com/)
- [ShapeFactory | Simple tools to enrich creativity](https://shapefactory.co/)
- [yeun/open-color: Color scheme for UI design.](https://github.com/yeun/open-color)

## References

- via: [大家有什么好的配色网站或者软件推荐吗？ - V2EX](https://www.v2ex.com/t/525939)
- [ ] Github Markdown was not supported for color rendering(via [github](https://docs.github.com/cn/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#disabling-markdown-rendering)). Yet you could use some third-party markdown web rendering tools (same with milkdown.dev):
    - https://github.com/pandao/editor.md / https://pandao.github.io/editor.md
    - * Inspiring by making labels for https://github.com/bGZoCg/2021/issues. *

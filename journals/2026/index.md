---
title: "2026"
aliases:
  - "2026"
created: 2026-01-10T22:55:17
modified: 2026-01-29T22:58:47
comments: true
draft: true
description: 
tags: []
---

# 2026

## 周记

因为我认为每天创建一个日记实在是有点浪费，所以决定使用 `utils/`

```button
name New writing V3
action
<%*
const templatePath = "templaters/writing.md";
const targetFolder = "weekly";
const filename = tp.date.now("YYYYMMDD");
const targetPath = `${targetFolder}/${filename}.md`;

// 如果目标文件已存在：直接打开，结束
const existedFile = app.vault.getAbstractFileByPath(targetPath);
if (existedFile) {
  await app.workspace.getLeaf(true).openFile(existedFile);
  return;
}

// 确保模板存在
const templateFile = tp.file.find_tfile(templatePath);
if (!templateFile) {
  new Notice(`Template not found: ${templatePath}`);
  return;
}

// 先创建（在哪都行）
const newFile = await tp.file.create_new(templateFile, filename, false);

// 再移动到目标目录
try {
  await tp.file.move(`${targetFolder}/${filename}`, newFile);
} catch (err) {
  new Notice("Failed to move file to weekly folder");
  return;
}

// 打开新文件
const finalFile = app.vault.getAbstractFileByPath(targetPath);
if (finalFile) {
  await app.workspace.getLeaf(true).openFile(finalFile);
}
%>
templater open true
```

- [x] W01: [[journals/2026/20260103|20260103]]
- [x] W02: [[journals/2026/20260110|20260110]]
- [x] W03: [[journals/2026/20260117|20260117]]
- [x] W04: [[journals/2026/20260124|20260124]]
- [x] W05: [[journals/2026/20260131|20260131]]
- [ ] W06: [[journals/2026/20260207|20260207]]
- [ ] W07: [[journals/2026/20260214|20260214]]
- [ ] W08: [[journals/2026/20260221|20260221]]
- [ ] W09: [[journals/2026/20260228|20260228]]
- [ ] W10: [[journals/2026/20260307|20260307]]
- [ ] W11: [[journals/2026/20260314|20260314]]
- [ ] W12: [[journals/2026/20260321|20260321]]
- [ ] W13: [[journals/2026/20260328|20260328]]
- [ ] W14: [[journals/2026/20260404|20260404]]
- [ ] W15: [[journals/2026/20260411|20260411]]
- [ ] W16: [[journals/2026/20260418|20260418]]
- [ ] W17: [[journals/2026/20260425|20260425]]
- [ ] W18: [[journals/2026/20260502|20260502]]
- [ ] W19: [[journals/2026/20260509|20260509]]
- [ ] W20: [[journals/2026/20260516|20260516]]
- [ ] W21: [[journals/2026/20260523|20260523]]
- [ ] W22: [[journals/2026/20260530|20260530]]
- [ ] W23: [[journals/2026/20260606|20260606]]
- [ ] W24: [[journals/2026/20260613|20260613]]
- [ ] W25: [[journals/2026/20260620|20260620]]
- [ ] W26: [[journals/2026/20260627|20260627]]
- [ ] W27: [[journals/2026/20260704|20260704]]
- [ ] W28: [[journals/2026/20260711|20260711]]
- [ ] W29: [[journals/2026/20260718|20260718]]
- [ ] W30: [[journals/2026/20260725|20260725]]
- [ ] W31: [[journals/2026/20260801|20260801]]
- [ ] W32: [[journals/2026/20260808|20260808]]
- [ ] W33: [[journals/2026/20260815|20260815]]
- [ ] W34: [[journals/2026/20260822|20260822]]
- [ ] W35: [[journals/2026/20260829|20260829]]
- [ ] W36: [[journals/2026/20260905|20260905]]
- [ ] W37: [[journals/2026/20260912|20260912]]
- [ ] W38: [[journals/2026/20260919|20260919]]
- [ ] W39: [[journals/2026/20260926|20260926]]
- [ ] W40: [[journals/2026/20261003|20261003]]
- [ ] W41: [[journals/2026/20261010|20261010]]
- [ ] W42: [[journals/2026/20261017|20261017]]
- [ ] W43: [[journals/2026/20261024|20261024]]
- [ ] W44: [[journals/2026/20261031|20261031]]
- [ ] W45: [[journals/2026/20261107|20261107]]
- [ ] W46: [[journals/2026/20261114|20261114]]
- [ ] W47: [[journals/2026/20261121|20261121]]
- [ ] W48: [[journals/2026/20261128|20261128]]
- [ ] W49: [[journals/2026/20261205|20261205]]
- [ ] W50: [[journals/2026/20261212|20261212]]
- [ ] W51: [[journals/2026/20261219|20261219]]
- [ ] W52: [[journals/2026/20261226|20261226]]

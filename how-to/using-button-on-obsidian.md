---
title: 如何在 Obsidian 中增加按钮
aliases:
  - 如何在 Obsidian 中增加按钮
created: 2026-02-01T14:42:45
modified: 2026-02-01T15:50:27
comments: true
draft: false
description:
tags: []
type: how-to
---

# 如何在 Obsidian 中增加按钮

电脑有键盘，可以绑定快捷键，可以很方便地插入模版，但是手机端不行，手机端的操作主要是「点击」，所以这个操作场景是针对手机端的：

> 在页面上渲染一个按钮，每次点击它就可以自动地按既定模板创建一片文章。

方案有：

1. ==Buttons + Templater==
2. QuickAdd（更偏命令）

对于方案 1，下载安装 [Buttons](https://github.com/shabegom/buttons) 和 Templater，并用下面的案例测试下自己当前的 Vault 是否工作正常：

```button
name Add Current Time
type append text
action Current time: <% tp.date.now("HH:mm:ss") %>
templater true
```

正常情况会插入当前时间，如：`Current time: 14:49:53`，如果出现了其他东西，打开命令台看下报错，可能是本地什么文件冲突了。

我们假设你已经提前在某个文件夹定义了 Templater 的模板文件，接着我们需要在某个文件夹下面创建一篇文章，假如我想新增一条随笔，放在周记里，按钮可以这样写：

```button
name New Writing V1
action
<%*
const templatePath = "templaters/writing.md";
const folder = "/weekly";
const filename = tp.date.now("YYYYMMDD");
const notePath = `${folder}/${filename}`;

const existedFile = app.vault.getAbstractFileByPath(notePath);
if (existedFile) {
  // 已存在：直接打开
  await app.workspace.getLeaf(true).openFile(existedFile);
} else {
  // 不存在：用模板创建
  const templateFile = tp.file.find_tfile(templatePath);
  const newFile = await tp.file.create_new(
    templateFile,
    notePath,
    false
  );
  // 创建完顺手打开
  await app.workspace.getLeaf(true).openFile(newFile);
}
%>
templater open true
```

这个按钮又一个 BUG：判断存在逻辑失效，原因是实际创建的文件根目录不是当前知识库，而是我全局设置的 `/pages` 文件夹，即最终创建的文件都在 pages/weekly 下面，我理想的位置是根目录 /weekly。

目前没有特别好的方案，只能增加一段移动文件的逻辑进去，即先随便创建一个文件，然后移动到这个目录中去，最终版本如下：

```button
name New writing V2
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

## References

Templater 和 Button 还有更多用户，比如 Button 其实可以替代 slash 命令，比如下面的按钮：

```button
name 打开模板选择框
type command
action Templater: Open Insert Template modal
```

- https://buttonslovesyou.com/usage/templater
- https://forum.obsidian.md/t/trying-to-create-a-button-that-runs-a-specific-templater-template/49472/5
- https://forum.obsidian.md/t/buttons-showcase/18044/2
- https://medium.com/@ConstructByDee/i-added-buttons-to-obsidian-and-i-love-it-d3625cc58879
- https://forum.obsidian.md/t/my-home-base-tutorial/108759

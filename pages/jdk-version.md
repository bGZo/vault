---
draft: true
aliases:
  - JDK Version
created: 2025-08-30T15:38:27
modified: 2025-08-30T15:41:44
title: JDK Version
---
# JDK Version

![](https://raw.githack.com/bGZo/assets/dev/2024/image_1652343742216_0-or8-or8-or8.png)

## Oracle JDK vs OpenJDK

| Items    | Oracle JDK | OpenJDK |
| -------- | ---------- | ------- |
| Licences | BCL / OTN  | GPL v2  |

- BCL (Oracle Binary Code License Agreement)
	- 可以使用 JDK (支持商用), 但是不能进行修改
- OTN (Oracle Technology Network License Agreement)
	- \>= JDK 11
	- 可以自己私下用，但是商用需要付费

![](https://raw.githack.com/bGZo/assets/dev/2024/image_1652343266064_0.png)

- `8u211` vs `8u202`
- Oracle JDK 关键补丁更新 (CPUs, Critical Patch Updates) 版本号
	- **奇数**编号
	- 安全漏洞修复和重要漏洞修复
- Oracle JDK 补丁集更新 (PSUs, Patch Set Updates) 版本号
	- **偶数**编号
	- 包含相应 CPUs 中的所有修复以及其他非重要修复
	- 仅当受到 Oracle JDK 关键补丁更新 (CPUs) 版本之外的其他漏洞的影响时才用

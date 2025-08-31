---
aliases:
  - 登录档
  - 注册表
  - Regedit
created: 2024-12-15T20:49:29
modified: 2025-08-31T10:53:34
title: Regedit
---

# Regedit

## Why

## How

### Edit

- 注册表编辑器
	- `win+r+regedit` / `%systemroot%\regedit.exe`
- 命令行工具 (CLI)
	- `reg`
- 脚本
	- \> Windows 98
- 第三方或自行编写的软件
	- `reg` 文件

## What

### Windows Operating System Registry

- Microsoft Windows 中的一个**数据库**

### History

- Windows 3.0 推出 OLE 技术的时候, 注册表就已经出现
- nt 是第一个从系统级别广泛使用注册表的操作系统
- Windows 95 开始，注册表才真正成为 Windows 用户经常接触的内容

### Data Category

| 显示类型（在编辑器中） |   数据类型   |                             说明                             |
| :--------------------: | :----------: | :----------------------------------------------------------: |
|         REG_SZ         |  **字符串**  |                          文本字符串                          |
|       REG_BINARY       |   二进制数   |              不定长度的二进制值，以十六进制显示              |
|       REG_DWORD        |     双字     |        一个 32 位的二进制值，显示为 8 位的十六进制值         |
|      REG_MULTI_SZ      |   多字符串   | 含有多个文本值的字符串，此名来源于字符串间用 nul 分隔、结尾两个 nul |
|     REG_EXPAND_SZ      | 可扩展字符串 |                     含有环境变量的字符串                     |

- 此外，注册表还有其他的数据类型，但是均不常用：
	- REG_DWORD_BIG_ENDIAN - DWORD 的 [大头](https://zh.wikipedia.org/wiki/字节序) 版本，下面同理
	- REG_DWORD_LITTLE_ENDIAN
	- REG_FULL_RESOURCE_DESCRIPTOR
	- REG_QWORD - DWORD 的四字（64 位）版本
	- REG_FILE_NAME

### Branch

5 个 1 级分支

|        名称         |                             作用                             |
| :-----------------: | :----------------------------------------------------------: |
|  HKEY_CLASSES_ROOT  | 存储 Windows 可识别的文件的文件名后缀和与之相关联的应用程序：一类是已经注册的各类文件的扩展名、另一类是各类文件类型有关信息。 |
|  HKEY_CURRENT_USER  | 存储当前**登录用户**设置的信息。这些信息保证不同的用户登录计算机时，使用自己的个性化设置，例如自己定义的墙纸、自己的收件箱、自己的安全访问权限等 |
| HKEY_LOCAL_MACHINE  | 包括安装在**计算机**上的硬件和软件的信息，包括所安装的硬件以及软件的设置。这些信息是为所有的用户登录系统服务的。（**最庞大也是最重要的根键**） |
|     HKEY_USERS      |    包含使用计算机的用户的信息。（所有以前登录用户的信息）    |
| HKEY_CURRENT_CONFIG | 这个分支包含计算机当前的硬件配置信息。其中存放的是计算机当前设置，如显示器、打印机等外设的设置信息等。它的子键与 HKDY_LOCAL_MACHINE\Config\0001 分支下的数据完全一样 |

还有一个隐藏分支 ` HKEY_PERFOR-MANCE_DA<wbr>TA `。

| 名称                   | 作用                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------ |
| `HKEY_DYN_DA<wbr>TA` | 保存每次系统启动时，创建的系统配置和当前性能信息。这个根键只存在于 Windows 9x 中。系统自带的注册表编辑器无法看到此键，但可以用专门的程序来查看此键，比如使用性能监视器。 |

## References

  - [注册表 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E6%B3%A8%E5%86%8C%E8%A1%A8)

---
draft: false
aliases:
  - How to choose package management
  - Package-management
created: 2025-04-06T15:30:19
modified: 2025-07-16T20:44:21
title: How to choose package management
---
# How to choose package management

## 跨平台

|                             | Windows | Debian | [[archlinux]] | MacOS | Mark                            |
| --------------------------- | :-----: | :----: | :-----------: | :---: | ------------------------------- |
| winget                      |    ✅    |   ❌    |       ❌       |   ❌   |                                 |
| [[ScoopInstaller-Scoop\|scoop]]      |    ✅    |   ❌    |       ❌       |   ❌   |                                 |
| apt                         |    ❌    |   ✅    |       ❌       |   ❌   | 系统核心组件、稳定性要求高的软件                |
| [[Homebrew-brew\|homebrew]] |    ❌    |   ✅    |       ✅       |   ✅   | 快速获取稳定环境的软件或新版本、开发工具、个人开发环境     |
| aur                         |    ❌    |   ❌    |       ✅       |   ❌   | 适合追求最新软件、需要高度定制的用户，或者喜欢滚动更新的环境。 |

## [[windows|Windows]]

### Winget

### Scoop

## [[debian]]

### 系统自带 APT 原理

1. .deb 二进制包：
    1. 软件和依赖都打包成 .deb 文件，包含安装路径、依赖信息、脚本等。
2. 中央仓库
    1. 官方仓库由 Ubuntu/Debian 官方维护，经过严格测试和签名验证。
3. 系统级安装
    1. 安装位置固定，通常在 /usr/bin、/etc 等系统路径，和系统核心组件共处。
4. 依赖和版本冲突处理复杂
    1. 系统级更新会导致依赖冲突或升级问题，包冲突可能影响整个系统稳定性。

## [[archlinux|Archlinux]]

### Pacman

专门处理 .pkg.tar.zst 格式的**已编译包**，不支持直接安装源码。

1. 读取官方仓库元数据（如 core, extra, community）。
2. 下载软件的二进制包。
3. 自动处理依赖关系。
4. 解压到系统路径（/usr/bin, /etc, /lib 等）。

#### AUR 的原理

> [!note]
> AUR 和 pacman 的本质区别
>
> AUR 不是包管理器，是一个**社区托管的源码包仓库**，提供了构建软件的“说明书”——PKGBUILD。

| **项目** | **pacman**                      | **AUR**                         |
| ------ | ------------------------------- | ------------------------------- |
| 类型     | **包管理器（Package Manager）**       | **用户维护的源代码仓库（Repository）**      |
| 管理对象   | 已构建好的 .pkg.tar.zst 二进制包         | **源码 + 构建脚本（PKGBUILD）**         |
| 安装方式   | 直接下载并安装二进制包                     | 克隆源码仓库，执行构建脚本，再安装               |
| 更新机制   | 统一由官方仓库控制                       | 完全由社区用户贡献和维护                    |
| 工具命令   | pacman -S, pacman -R, pacman -U | 需配合 AUR helper（如 yay, paru）     |
| 速度     | 极快（下载即装）                        | 相对较慢（clone -> build -> install） |

1. **PKGBUILD 文件**
    1. 每个包由一个名为 PKGBUILD 的脚本文件定义，说明如何下载源码、编译和安装。
2. **用户编译源码**
    1. 使用 makepkg 命令读取 PKGBUILD，从源码编译生成 .pkg.tar.zst 二进制包。
3. **辅以 AUR Helper**
    1. 如 yay, paru 等工具提供自动解析依赖、编译安装、更新等操作。
4. **系统级安装**
    1. 最终通过 pacman 安装，和系统包共存，不像 Homebrew 那样自成体系。

## [[macos|Macos]]

### Homebrew

1. **Formula 配方**
    1. 每个软件都有一个称为 **formula** 的 Ruby 脚本，描述了如何安装这个软件（包括下载地址、依赖、编译参数等）。
    2. 举例：brew install neovim 会查找 Neovim 的 formula，决定用源码编译还是下载预编译包。
2. **安装路径**
    1. 默认安装在 /home/linuxbrew/.linuxbrew（或 macOS 上的 /usr/local/Cellar），**不影响系统自带的包和依赖**。
    2. 使用软链接将软件链接到可执行路径，如 /home/linuxbrew/.linuxbrew/bin。
3. **依赖管理**
    1. Homebrew 会为每个软件管理独立的依赖，**避免全局污染**，适合构建隔离的开发环境。
4. **Binary Bottles**
    1. 通常直接从预编译的二进制包（bottle）安装，无需源码编译。
    2. 当然也支持从源码编译（用 --build-from-source）。

## 总结 #chatGPT

|                | APT                                                           | [[Homebrew-brew]]                                                       | AUR                                               |
| -------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------- |
| 软件包数量和社区活跃度    | **APT** 仓库中的软件通常是经过严格测试的稳定版本，但更新较慢，有时可能滞后于官方版本。               | 软件包数量虽然多，但整体远不及 AUR，尤其是一些小众或定制软件可能找不到。<br>                              | 拥有极其庞大的软件包数量和社区支持，几乎任何软件都能在 AUR 找到，而且更新速度非常快。<br> |
| 软件包多样性和覆盖度     |                                                               | 主要维护稳定版，开发版或实验性版本较少。                                                    | 涵盖范围极广，既有稳定版、开发版、甚至是测试版或实验性软件。                    |
| 定制化            |                                                               | 虽然可以修改 formula，但定制过程不如 AUR 灵活，且复杂度更高                                    | 用户可以直接修改 PKGBUILD 文件，自定义编译参数，轻松打造符合自己需求的软件包。      |
| 滚动更新           |                                                               | 虽然更新快，但不如 AUR 那么前沿                                                      | 滚动更新模式，用户总能使用到最新版本的软件。                            |
| 依赖管理           |                                                               | 依赖管理较严格，依赖链由 Homebrew 维护                                                | 依赖管理非常灵活，可以从源码编译，完全控制依赖版本。                        |
| 安装方式           |                                                               | 主要提供二进制包，源码编译不是默认选项。                                                    | 用户可以选择从源码编译安装，也可以直接安装二进制包。源码编译更灵活。                |
| 独立于系统          | APT 直接影响系统库和组件，容易引发系统依赖问题。                                    | Homebrew 安装在 /home/linuxbrew 或 /usr/local 下，不影响系统自带的软件，避免因系统升级或包冲突导致问题。 |                                                   |
| 软件版本管理         | APT 主要通过 apt install package=version 来安装指定版本，但不如 Homebrew 直观。 | Homebrew 支持多版本软件共存和切换，比如通过 brew link/unlink 选择不同版本。                     |                                                   |
| 跨平台一致性         | APT 仅限于 Debian 系系统（Ubuntu、Debian 等）                           | Homebrew 提供一致的体验，可以在 macOS 和 Linux 之间无缝切换。                               |                                                   |
| 更容易安装非官方或第三方软件 | APT 需要手动添加 PPA 源或编译安装，步骤较繁琐。                                  | Homebrew 支持**自定义 formula**（配方），允许轻松安装 GitHub 上的开源项目或个人开发的软件包。           |                                                   |
| 简洁和统一的命令管理     | APT 的命令虽然功能强大，但语法有时较复杂，比如 apt-get 和 apt 的区别容易让人混淆。            | Homebrew 的命令非常直观，如 brew install、brew upgrade、brew uninstall，操作简单。       |                                                   |

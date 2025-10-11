---
title: Macbook Pro 祛魅
aliases:
  - Macbook Pro 祛魅
cover: 
created: 2024-01-13T13:41:04
modified: 2025-03-22T13:42:20
description: 
cpu: M2Pro
ram: 32G
ssd: 512G
price: 20000
tags: 
- consume/refund
type: 3c
wikipedia:
---

> [!note]
> 乔布斯最大的成就就是让一帮连 vi 都用不利索的人自以为是 geek
  https://www.v2ex.com/t/166440

 时值春运回家，前前后后折腾了两次 [[archlinux]]，均以失败告吹，ARM 笔记本还遥遥无期，10 月极其昂贵的 M3 MAX 发布后，M2Pro 翻新被一抢而空，病急乱投医，信用卡分期 ¥18799 入手了 [16inch M2 Pro 32 + 512 的MBP](https://www.apple.com.cn/shop/product/G1770CH/A)。周六日使用两天后，决定退款。这注定是一场祛魅的体验。

## 动机

### ARM 架构

ARM 架构本就是借鉴手机移动芯片，如果把移动端的**能耗比**也带来给笔电，加上比手机大得多的电池，续航也能拉到非常长的时间；

无需转译，支持原生支持 iOS 应用，但这不是完全免费的，最终的决定权在开发者那边，如果开发者不愿意应用在 Mac 上运行，那么这就是完全不可能的，用户无法侧载相关 App。这是 Apple 尊重开发者的决定，是一个高明的决定 [^ios-app-run-on-mac]。

### 联合统一架构

内存可以当显存使用，因为不熟悉炼丹，拿到手后也没有测试跑 AI 的能力，但是逛论坛后发现，Mac 在训练 AI 上还是打不过 CUDA，只在部署和推理层面有优势，加上生态也没有建立起来（苹果只手写了一个 [tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/) 的引擎，听说也是半死不活的，提 ISSUE 没有人管），基本没法和 NVIDIA 那边玩。对于这些点 「林亦」只字不提，已经把他拉黑了； [[20231202]]

- https://v2ex.com/t/959841
- https://v2ex.com/t/864729

### 统一通知系统

Mac 也可以走统一消息平台而无需后台挂起；

### 14 寸功耗墙

Mac 默认用充电器功率限制处理器功耗，14 寸的功耗墙在 60w 左右，16 寸的功耗墙在 140w 左右；14 寸用 96w 的充电器只能提升充电速度，TDP 是定死的；😆[^power_wall]

## 数不尽的槽点

### Everything everywhere paid

之前买过一台 iPad Pro ([[ipad-pro-6-m2-11inch]])，两者的体验如出一辙，都有种难以忽视的铜臭味。

用户设备中的应用只能来自 AppStore，开发者需要每年向 Apple 提供订阅费才可以持续分发自己的应用。开发者没有开发免费应用的动力，至少开发者得想法从用户们手中把今年的订阅费赚回来，要不然未来一年都是为爱发电，是难以持续的。

对用户来说，其实几乎没有真正意义上免费的应用，这相当《监视资本主义》，那些你免费使用的软件，很大概率上，你就是商品本身。也就是说，如果你需要什么真正的东西，那么你就得掏钱解决。

这是一个合适的生态模式吗？我不知道，但可以肯定的是，他可持续。也是让苹果极具号召力的原因。

  - 16 inch 并不轻便的 **体重**；
    id: 66d29d71-3685-4d6e-bcb9-045e6256c024
    - 我的旧游戏本，体重大约为 2.35kg，而我手上这台大概 2.1kg，
      - 相差无几，甚至只是一个 iPad 的重量！
    - 唯一可圈可点的期就只剩这块屏幕和扬声器了。

## 边角设计

16 寸的边角过渡非常硌手。尤其是触控板下方的凹槽处，给人一种能被划伤的感觉。很难想象这是两万块的笔记本所带来的用户体验，如果你在膝盖，或者肚皮上码字，配合 2.1 kg 的压强，你将获得在钉板上打字的体验。胳膊会被勒出显而易见的红印，并且非常难受。

<iframe src="https://www.youtube.com/embed/NnGAlf1hjs4" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=NnGAlf1hjs4' target='_blank' class='external-link'>https://www.youtube.com/watch?v=NnGAlf1hjs4</a></center>

## 统一内存焦虑

第一次拿到机器后体验一番后，打开内存一看已经占用 `20/32` 之多，内存压力虽然还是绿的，但还是有点吓坏了。

重启重新跑软件后，发现开了 Safari 用一段时间后，确实会这样。跟 FF 很像啊 ）

## 文件系统驱动阉割

无法相信的是，macOS 无法读写 NTFS 和 EXT4，用上了 Macbook 之后，基本可以抛弃 Windows 和 Ext4 格式的硬盘了，只能用专有格式 APFS。在 Apple 的目标用户中，是不存在用 Linux 和 Windows 的。

最让人生气的是，在十多年前的 10.13 版本中，是可以支持写入的 [^Old_Support]，This is a totally artificial limitation，Apple 拒绝给出任何解释。

> The real question is what would Microsoft/Apple gain?
  https://www.reddit.com/r/linuxquestions/comments/p3bxne/why_isnt_ext4_readablemountable_on_mac_nor_windows/

### [Mounty for NTFS](https://mounty.app)

### [BuhoNTFS](https://www.drbuho.com/buhontfs) [[20240615]]

### UTM

虚拟机 [^UTM]

**文件系统** 驱动支持匮乏；

## 无剪切板概念

这真的是用了就回不去的设计，你很难想象如果你剪切错了一段文本，在无法撤销的情况下，你将永远丢失该文本。

http://github.com/p0deje/Maccy

## Finder 没有剪切文件的概念

- 统一走复制 [^move_file]
- 在第二个目录选择移动到这里（快捷键 `command+option+v`）

## Custom Settings

### ZSH

Mac 现在开局就是 ZSH，所以不需要额外的下载。但 Mac 下的 ZSH 略有不同。（`.zshrc` 和 `.zprofile` 的区别）

> For mac users running ZSH, the ~/.zshrc file is evaluated every time a shell is launched. The ~/.zprofile file is only evaluated when you login to your mac user account
  https://ss64.com/mac/syntax-profile.html

#### Install

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

https://zhuanlan.zhihu.com/p/354385629

#### Option

```shell
echo >> /Users/bgzo/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/bgzo/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Disk write status

```shell
brew install smartmontools
smartctl -s on disk0
smartctl -a disk0
```

https://zhuanlan.zhihu.com/p/354385629

## Shortcuts

- 截图
    - 全屏，Shift、Command、3
    - 区域，Shift、Command、4
    - 窗口，Shift、Command、4、Space
- https://support.apple.com/zh-cn/102646

## Waiting for features

- 更多侧载软件
    - 拼多多
    - 淘宝
    - 美团
    - Snpid
    - **已经支持并由衷的推荐**：
        - 得到
        - 微信读书
        - 酷安
- 更多的 ARM 原生应用：
    - 阿里云盘
    - [Apple Silicon 准备好了吗](https://isapplesiliconready.com/for/productivity)

## Conculision

关于最后 [[hp-starbook]]，我还是放弃了购买 MacbookPro M1Pro 64GB 的版本，大概需要 2 万，感觉不需要。

也有人推荐用 MBA 丐版 SSH 到服务器做开发，不知道是为了什么？为什么我一万块钱买了一台电脑还用不爽？

未来如果大模型起来之后散热，功耗墙，能耗比会是一个巨大的问题，我更希望新款的 MBP 还是以前那种静音的状态，现在这个苹果让人非常不舒服，有点作呕。

考虑以下产品做替代：

  - Dell https://www.dell.com/zh-cn/shop/
  - Surface https://www.microsoftstore.com.cn/surface/surface-pro-9
    - 品控堪忧，https://v2ex.com/t/911230
  - ThinkPad https://shop.lenovo.com.cn/
  - [Dell XPS 和 Surface Book 哪个替代 MBP 更好一些？ - V2EX](https://v2ex.com/t/570244)

## Reference

  - Safari 下载自动解压 ZIP via: https://zhuanlan.zhihu.com/p/349504217
  - Dell 显示器控制驱动 via: https://www.dell.com/support/home/zh-cn/product-support/product/dell-display-peripheral-manager/drivers
  - 清洁 Mac: https://support.apple.com/zh-cn/HT204172
  - intel mac 生存记录 via: {{nav-ri https://www.v2ex.com/t/1008425}}
  - [我这个 16 寸 M1 Pro 的 MBP 续航很差 - V2EX](https://v2ex.com/t/925060)
  - [2021 款 16 寸 M1 Pro 钙版。续航只有 4 个半小时 - V2EX](https://v2ex.com/t/834059)
  - https://www.apple.com.cn/shop/product/G175BCH/A
    - 正好 24499；
    - https://strongbugman.github.io/
    - https://v2ex.com/t/807782

[^ios-app-run-on-mac]: via: https://www.ithome.com/0/534/909.htm, 完全可以理解，如果一个开发者无法控制自己应用的分发渠道，那么将没有人愿意再为 Mac OS 开发软件；
[^power_wall]: http://post.smzdm.com/p/az68nq70/
[^Old_Support]: https://www.zhihu.com/question/365552114, with official discuss on https://discussions.apple.com/thread/253707407
[^UTM]: https://www.v2ex.com/t/894750, https://www.v2ex.com/t/896725, PD 太贵，开源的 UTM 较好，使用文档 https://docs.getutm.app/guides/windows/
[^move_file]: https://sspai.com/post/28389

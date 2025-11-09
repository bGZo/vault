---
draft: true
aliases:
  - Taichi
  - Xposed-taichi
created: 2025-08-30T23:56:37
modified: 2025-08-31T00:00:01
title: Taichi
---
# Taichi

TaiChi is a framework to use Xposed module with or **without** Root/Unlock bootloader, it currently supports Android 5.0 ~ **10.0**.

In simple words, TaiChi is a **Xposed-Styled** Framework, it can load Xposed modules, do hooks and so on.

> Magisk 的原理简单的说就是在系统 boot 时将其 img 挂载到自己的分区下, 构建一个虚拟文件系统, 和 system 分区无关, 以不修改系统文件为前提, 从而达到修改系统文件的效果. 通过这种方式绕过谷歌安全机制, 系统 OTA 升级, 部分 " 被禁 " 软件都可以正常使用. 而 Xposed 相反, 框架一旦被加载就会修改系统, 改动会影响在安全机制保护下的 APP, 所以一些理财软件,比如某某银行可能就无法使用, 这些应用对 root 权限非常敏感. 总的来说 Magisk 是通过 systemless 方式获取 root, xposed 则需要 root 才可以工作. 所以 magisk 虽然集合了各种功能, 但延展性上不如 Xposed, 两者虽有一些相似之处, 但本质上完全不同, Magisk 是创建新的分区而 Xposed 是直接修改系统文件. 现在最好的结果就是二者相辅相成, 按自己需要. via: https://www.coolapk.com/feed/19489640?shareKey=MDUzNjMzMzk2ZTVmNWY0NTExNTA~

**Xpose**: Xposed 框架的原理就是替换安卓系统的 app_process 文件, 从而实现对系统的接管, 通过回调模块的方式来达到不用修改 APK 就能改变其表现行为的目的. 用通俗的话来说就是是在任意进程启动之前, 能加载特定 Xposed 模块的代码, 从而控制任意进程的行为. 这些特定的 Xposed 模块, 能在 App 进程启动之前执行特定代码. app_process 其实是存放在 systen/bin 目录下的一个程序, 其作用就是启动 zygote, 在 Android 中, zygote 是整个系统创建新进程的核心进程. Xposed 框架 Hook 了核心进程 Zygote, 而其他应用启动都是从 Zygote 进程 fork 而来, 就够达到针对系统上所有的应用程序进程的 Hook. 举个例子, 比如很著名的某微信模块, 就是你在启动微信之前, 首先要运行模块内的一些脚本, 这些脚本会劫持微信这个 APP 里的所有行为, 所以最终能够实现微信内容防撤回, 自定义微信摇骰子和石头剪刀布.

## MODULE

- [QNotified|QQ辅助性功能增强](https://github.com/ferredoxin/QNotified)
- [Zhiliao|知乎去广告Xposed模块](https://github.com/shatyuka/Zhiliao)
- [ChiMi|MIUI扩展插件(xposed)](https://github.com/yonghen/chimi-)
- [其他](https://repo.xposed.info/module-overview)

## References

- https://github.com/taichi-framework/TaiChi
- https://taichi.cool
- https://www.zhihu.com/question/316497403

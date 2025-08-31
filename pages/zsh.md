---
aliases:
  - Zsh
  - ZShell
created: 2024-07-28T12:00:00
modified: 2025-08-31T14:05:37
title: ZShell
type: tool
---

# ZShell

<iframe src='https://zsh.sourceforge.io/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://zsh.sourceforge.io/' target='_blank' class='external-link'>https://zsh.sourceforge.io/</a></center>

## What

Install https://github.com/bGZo/dotfiles => via README

## Prompt

```shell
    # In bashrc you should write folling:
    # export PS1="%K{red}%n@%m%k%B%F{cyan}%(4~|...|)%3~%F{white}\$#%b%f%k" #{blue}
    # export PS1="\[\033[0;31m\]\342\224\214\342\224\200$([[ $? != 0 ]] && echo "[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200")[\[\033[0;39m\]\u\[\033[01;33m\]@\[\033[01;96m\]\h\[\033[0;31m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[01;33m\]\$\[\e[0m\]"
    # Initialize command prompt
    export PS1="%n@%m:%~%# "
    # not oh-my-zsh's prompt
    # first: %K{blue}%n@%m%k %B%F{cyan} %(4~|...|)%3~%F{white} %# %b%f%k
    # then : %K{blue}%n@%m%k%B%F{cyan}%(4~|...|)%3~%F{white}%#%b%f%k
    # `man zshmisc`
    # - `%F-%f`: 如果支持，则使用其他前景色开始（停止） 通过终端
    # `％F {red}`
    # - `％K-%k`: 使用其他背景色开始（停止）
    # - `%n`: 用户名
    # - `%m`: 主机名（在第一个句号之前截断）
    # - `%B-%b`: 粗体打印
    # - `36 cyan 46 bg-cyan`
    #
    # also in bash is
    # PS1='\[\033[0;31m\]\342\224\214\342\224\200$([[ $? != 0 ]] && echo "[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200")[\[\033[0;39m\]\u\[\033[01;33m\]@\[\033[01;96m\]\h\[\033[0;31m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[01;33m\]\$\[\e[0m\]'
    # refer: https://github.com/zsh-users/zsh/blob/master/Functions/Misc/colors
    # https://unix.stackexchange.com/questions/32273/16-colors-in-zshell/32304
    # more could see: https://blog.csdn.net/u014218108/article/details/51195582
```

## Reference

- [linux-command|Linux命令大全搜索工具](https://github.com/jaywcjlove/linux-command)
- [如何在Ubuntu 18.04 LTS中安装和美化ZSH Shell - 系统极客](https://www.sysgeek.cn/install-zsh-shell-ubuntu-18-04/)
- [Oh-My-Zsh及主题、插件安装与配置美化 - 破碎虚空的个人空间 - OSCHINA - 中文开源技术交流社区](https://my.oschina.net/u/2266513/blog/3103451)
- [iTerm2 + Oh My Zsh 打造舒适终端体验 - 知乎](https://zhuanlan.zhihu.com/p/37195261)
- [ubuntu切换shell命令 - 简书](https://www.jianshu.com/p/b61473e22c8b)
- [ZSH-输出整个历史记录？](https://qastack.cn/superuser/232457/zsh-output-whole-history)
- [zsh: no matches found: -? · Issue #31 · ohmyzsh/ohmyzsh · GitHub](https://github.com/ohmyzsh/ohmyzsh/issues/31)
- [配置bashrc简易教程 | Carpe's Garden](https://comery.github.io/2017/07/20/A-easy-guide-bashrc/)
- [git - zsh+on-my-zsh配置教程指南（程序员必备）【已备份】 - michael翔的IT私房菜 - SegmentFault 思否](https://segmentfault.com/a/1190000013612471)
- [Oh My Zsh 教程 - 掘金](https://juejin.im/post/6844903669578596359)
- [Tab key == 4 spaces and auto-indent after curly braces in Vim]([whitespace - Tab key == 4 spaces and auto-indent after curly braces in Vim - Stack Overflow](https://stackoverflow.com/questions/234564/tab-key-4-spaces-and-auto-indent-after-curly-braces-in-vim))

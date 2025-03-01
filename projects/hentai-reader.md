---
created: 2023-06-14T00:00:00
description: 变态阅读器
tags:
  - rss
  - github
  - action
  - crawler
  - hentai
  - python
  - jekyll
  - tailwind
  - javascript
type: product
modified: 2025-02-16T14:27:41
---

> [!warning]
> ⚠️ NSFW 警告：本篇文章可能包含暴力，性描写等仅供 18 岁以上阅览的内容。

## Repo Meta

![](https://img.shields.io/github/stars/bGZo/hentai?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/bGZo/hentai?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/bGZo/hentai?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=bGZo&repo=hentai&bg_color=00000000)](https://github.com/bGZo/hentai)

## Why

我很喜欢色情内容，但如果把它和其他订阅源放在一起，我一定不会再花时间琢磨别人的博客了，加上本人自制力差，容易被性暗示唤起性欲，所以对我来说，色情内容需要做隔离。

那为什么不用 RSSHub，还要自己用 Python 写规则呢？

1. 定制化：我需要对拉去下来的源做附加的逻辑，比如过滤器，预览图替换，防盗链 (todo)
2. 版权：RSShub 已经算是一个知名的项目了，且对一些版权性 PR 持保守态度，树大招风，我觉得你一定懂。
3. 周期：开发周期会被 RSShub 上游卡着，或者我本地需要部署一个 RSShub 实例，比较麻烦，加上本身菜，就当练手了。

当然，这个项目不可能盈利，仅仅是继 [个人博客](https://blog.bgzo.cc/) 后，出于兴趣探索的再一款 jekyll 博客。

有非常多局限，如内容排版，目录导航，视觉设计等等，还有非常多待改进的地方

![](https://raw.githack.com/bGZo/assets/dev/2025/202502150013399.png)

## How

### Vercel host via https://hentai.bgzo.cc
### Source via: https://github.com/bGZo/hentai

## What

### Features

1. Fetch RSS feeds and keep the latest resource daily
2. Persist feeds in repo and support API with following (`http://rss.bgzo.cc`) with json

| Name | Route | Description | Method | Note |
|-------|------|------|------|------|
| Feed  | `/feeds/${tag_name_with_hyphen_and_lower}` | RSS feed, return xml | `GET` | `${tag_name_with_slash_and_lower}` is the url string handle by `lower()` and hyphen(`-`). <br/>For example, we have a `DLsite Game Ranking.xml` file in server, then the correct full url address will be `http://rss.bgzo.cc/feeds/alsite-game-ranking.xml`; |
| Contents | `/archives/${year}/${month}/${day}.json` | Contents, return JSON response | `GET` | **NOTE**: The timezone of response is GMT, format it whatever you want |

### Todos

- [ ] #doing Support more sources
    - [x] https://www.dlsite.com
    - [x] https://www.4gamers.com.tw
    - [x] https://mingqiceping.com (Feed 地址失效)
    - [ ] Telegram
- [ ] #todo More usable
    - [x] Separate from RSS sources configuration from codes

### Wontfix

#### 防盗链

一些网站本身开启了防盗链，如: [灵梦御所](https://blog.reimu.net/feed)。除非单独构建应用，或是添加请求头 `Referer: https://blog.reimu.net`，否则在一般的浏览器，是无法绕过的。

比如以下图片，你无法把它嵌入到你的博客，却能正常通过鼠标右键新建标签页打开浏览。

```
https://img.reimu.net/uploads/2023/06/6499957d1a902.png
```

#### How to deal with the content only show for the user login?

So the way RSS is bankruptcy, how does you request content using common method? How do you recognize the different websites? There are too much details.

#### How to deal with the copyright?

Considered the risk of copyright, I should not build any mirror site for business content.

### Alternatives

- https://nodetics.com/feedbro
- Telegram pron channel

## Tech Stack #tech-debt

- [[jekyll]]
    - [How to show the latest post as the homepage? - Help - Jekyll Talk --- 如何将最新的帖子显示为首页？ - 帮助 - Jekyll Talk](https://talk.jekyllrb.com/t/how-to-show-the-latest-post-as-the-homepage/2199/3)
- [[python]]
    - date
        - [Python datetime (With Examples) (programiz.com)](https://www.programiz.com/python-programming/datetime)
        - [How to Create a Time Object in Python (learningaboutelectronics.com)](http://www.learningaboutelectronics.com/Articles/How-to-create-a-time-object-in-Python.php)
        - [Python Create Date Object (w3schools.com)](https://www.w3schools.com/python/gloss_python_date_create.asp)
        - [datetime — Basic date and time types — Python 3.11.4 documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour)
        - [Get Previous, Current and Next-Day System Dates in Python – Data to Fish](https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/)
        - [Python timestamp to datetime and vice-versa (With Examples) (programiz.com)](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
    - dict
        - [Adding to Dict in Python – How to Append to a Dictionary (freecodecamp.org)](https://www.freecodecamp.org/news/add-to-dict-in-python/)
        - [python字典遍历的几种方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/33033288)
        - [Python 按键(key)或值(value)对字典进行排序 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html)
    - [[pyyaml]]
        - - [What is YAML?](https://www.redhat.com/en/topics/automation/what-is-yaml)
        - [opml · PyPI](https://pypi.org/project/opml/)
    - [[feedparser]]
        - [Introduction — feedparser 6.0.10 documentation](https://feedparser.readthedocs.io/en/latest/introduction.html)
        - [python - AttributeError: module 'feedparser' has no attribute 'FeedParserDict' - Stack Overflow](https://stackoverflow.com/questions/46829474/attributeerror-module-feedparser-has-no-attribute-feedparserdict)
    - [[requests]]
    - [[feedgen]]
        - [lkiesow/python-feedgen: Python module to generate ATOM feeds, RSS feeds and Podcasts. (github.com)](https://github.com/lkiesow/python-feedgen)
        - ["ValueError: Required fields not set" when generating Atom feed · Issue #39 · lkiesow/python-feedgen --- 生成 Atom feed 时出现“ValueError：未设置必填字段” · 问题 #39 · lkiesow/python-feedgen (github.com)](https://github.com/lkiesow/python-feedgen/issues/39)
    - pytz
    - others
        - [python - How to raise an AttributeError? - Stack Overflow](https://stackoverflow.com/questions/73853413/how-to-raise-an-attributeerror)
        - [为什么产生 __pycache__ - Google Search](https://www.google.com/search?q=%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BA%A7%E7%94%9F+__pycache__)
        - [python函数如何传递多个参数_python传入多个参数_LLY_A_的博客-CSDN博客](https://blog.csdn.net/LLY_A_/article/details/119968335)
        - [Python传入参数的几种方法-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1567332)
        - [import - Python FileNotFoundError : - Stack Overflow](https://stackoverflow.com/questions/74953823/python-filenotfounderror)
        - [python - How do I create a directory, and any missing parent directories? - Stack Overflow](https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories)
        - [File Handling in Python – How to Create, Read, and Write to a File (freecodecamp.org)](https://www.freecodecamp.org/news/file-handling-in-python/#:~:text=In%20Python%2C%20you%20use%20the,it%20will%20return%20an%20error.)
        - [python - Write a file to a directory that doesn't exist - Stack Overflow](https://stackoverflow.com/questions/23793987/write-a-file-to-a-directory-that-doesnt-exist)
        - [python - Converting dictionary to JSON - Stack Overflow](https://stackoverflow.com/questions/26745519/converting-dictionary-to-json)
        - [python - How to make a datetime object aware (not naive) - Stack Overflow](https://stackoverflow.com/questions/7065164/how-to-make-a-datetime-object-aware-not-naive)
        - [python - Is there a list of Pytz Timezones? - Stack Overflow](https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones)
- [[tailwindcss]]
    - [Tailwind CSS Tooltip - Free Examples & Tutorial (tailwind-elements.com)](https://tailwind-elements.com/docs/standard/components/tooltip/)
- [[html]] [[pages/css|css]]
    - [七种CSS方式让一个容器水平垂直居中_css相对容器居中_](https://blog.csdn.net/u013063153/article/details/52572489) [link](https://app.todoist.com/app/task/8852805381)
    - [How do I create an HTML button that acts like a link? - Stack Overflow](https://stackoverflow.com/questions/2906582/how-do-i-create-an-html-button-that-acts-like-a-link)
    - [A Complete Guide to Flexbox | CSS-Tricks - CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [[javascript]]
    - [javascript - Expanding all details tags - Stack Overflow](https://stackoverflow.com/questions/43008609/expanding-all-details-tags)
    - [javascript - Open closest Details element onclick - Stack Overflow](https://stackoverflow.com/questions/66076836/open-closest-details-element-onclick)
    - > `window.location.href` — [Get the current URL with JavaScript? - Stack Overflow](https://stackoverflow.com/questions/1034621/get-the-current-url-with-javascript)
- Git
    - [git - How do I create a new GitHub repo from a branch in an existing repo? - Stack Overflow](https://stackoverflow.com/questions/9527999/how-do-i-create-a-new-github-repo-from-a-branch-in-an-existing-repo)
- Others
    - Can't open the tabnine setting panel
        - > FWIW I was able to install 3.2.8 without issue.
            — [Tabnine Extension was unable to download its dependencies. · Issue #447 · codota/tabnine-vscode --- Tabnine Extension 无法下载其依赖项。 · 问题 #447 · codota/tabnine-vscode](https://github.com/codota/tabnine-vscode/issues/447)

        - 降级到 3.2.8 #wsl
        - [can't open the setting panel · Issue #741 · codota/tabnine-vscode --- 无法打开设置面板 · Issue #741 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/741)
        - [command 'TabNine.statusBar' not found · Issue #426 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/426)
        - [hub not loading · Issue #643 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/643)
        - [WSL2 Issue with TabNine:config · Issue #386 · codota/TabNine (github.com)](https://github.com/codota/TabNine/issues/386)
        - [visual studio code - Tabnine Extension was unable to download its dependencies - Stack Overflow](https://stackoverflow.com/questions/70565623/tabnine-extension-was-unable-to-download-its-dependencies)

### PY 开始提醒强制使用 VENV

```
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

#### Solution

Pycharm 开启虚拟环境：

`Settings > Project: > Python Interpreter > Add Interpreter > Select Virtualenv`, via: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env

---
aliases:
  - Google
created: 2024-07-30T00:00:00
description:
modified: 2025-08-03T21:24:37
title: Google
---

# Google

## Google Analyse

- https://tagassistant.google.com/

## Google Mobile Service

> 2018 年 7 月, 欧盟在对 Google 相关问题进行调查之后, 欧盟对谷歌处以创纪录规模的反垄断罚款, 金额将高达 43 亿欧元 (50 亿美元). 欧盟指责谷歌通过滥用其 Android 市场的主导地位, 而将自家的搜索引擎和 Chrome 应用程序捆绑到操作系统中. Google 可不吃这亏, 羊毛出在羊身上, Google 进行了反制. 2019 年 2 月 1 日开始, 对欧盟手机厂商进行收费, 安装 GMS 的每台设备收 40 美元的授权费. via: https://www.sohu.com/a/315171197_114986

GMS, Google 应用程序和 [API](https://developers.google.com/android/guides/overview) 的集合. via: https://zhuanlan.zhihu.com/p/66478028 一般的用途有:

GMS 为 Android 上 Google 公司的系列应用程序提供支持

  - GMail.
  - Earth.
  - Play.

Android 系统的基础框架. **虽然 Android 开源, 但 GMS 仍须取得谷歌的授权**. GMS 包括 Google Map、Gmail、YouTube 等应用, 以及应用商店 Google Play, 要使用就必须获得谷歌的同意与授权, 而且不得随意修改.

### SMS, EMS, MMS

- SMS: Short Messaging Service, 短消息服务, 最多达 160 个字节, 与大约 1 秒钟的语音呼叫所占用的空间相当. 消息的传输总是由处于 GSM 外部的 SMSC(Short Messaging Service Center, 短消息服务中心) 进行中继, 与电子邮件类似, SMS 短信只与用户终端和 SMSC 有关. 大家熟知的 GSM 及以后的网络都对 SMS 提供了支持.
- EMS: Enhanced Message Service, 增强短信业务, SMS 的增强版本, 除文本外, 可发简单的图像、声音和动画等信息. 当时已有的 MMS 需要 GPRS 网络或 CDMA 2000 1X(2.5G 网络) 普及的限制, SMS 是作为一个从 SMS 到 MMS 过渡的版本而设计. EMS 在 GSM 网络就可以发送, 应该说是在 2G 网络向 2.5G 网络过渡的一项不错的技术. 对 EMS 的支持需改动最大的是运营商的计费系统, 因为图像、声音和动画等所占用的字数可能相差很大, 运营商需要仔细衡量.
- MMS: Multimedia Messaging Service, 多媒体短信业务, 这项业务是根据 3GPP 和 WAP 论坛的标准制定的. 用术语讲多媒体短信业务是在 GPRS 网络或 cdma2000 1X 网络的支持下, 以 WAP 无线应用协议为载体传送视频片段、图片、声音和文字. 支持语音、因特网浏览、电子邮件、会议电视等多种高速数据业务, 实现即时的手机端到端、手机终端到互联网或互联网到手机终端的多媒体信息传送. 这种业务的出现可以替代部分电子邮件的功能, 可以作为明信片的电子版, 提供的服务内容极为丰富. 这种业务发展的最大障碍是目前 2.5G 网络速度的限制, 网络速度慢直接导致了资费过高, 虽然价格已经下降很多, 但仍然是大多数用户不能承受的.
via: https://zhidao.baidu.com/question/21473984

## Google Search

2014 年 12 月版 部分参考：《利用搜索引擎检索现有技术》魏保志 201203 版

| Char        | Meanings                                                                  | Case                            |
| ----------- | ------------------------------------------------------------------------- | ------------------------------- |
| AND/空格      | " 与 " 关系                                                                  | 云计算 分布式计算                       |
| OR/(竖线)     | " 或 " 关系                                                                  | 图片 \ 写真                         |
| -           | " 非 " 关系                                                                  | 神雕侠侣 - 游戏                       |
| ()          | 括号里的运算将优先进行                                                               | 电子商务 AND (云计算 - 分布式计算)          |
| ""          | 括号中的内容作为一个整体被搜索; 精确匹配搜索                                                   | “智能天线”                          |
| *           | 通配符 *, 代表完整的字词; A * B、A * * B 这两个是有区别的                                    | Flower * pots /Flower * * pots  |
| +           | 强制搜索一般会被自动忽略的搜索关键词，如：who、the、of、am                                        | +B                              |
| ~           | 同义符; 在搜索词前使用，表示会和同时搜索相近词义的词; 示例中会同搜元素 Si                                  | ~ silicon                       |
| ..          | 搜索数字范围限定                                                                  | 手机 价格 2000..5000                |
| filetype:   | 把搜索范围限定在特定文件类型中; .pdf/.doc/.docx/.ppt/.pptx/.xls/.xlsx/.rtf/.txt/.swf/.ps | 霍金 黑洞 filetype:pdf              |
| site：       | 在特定站点、某一站点特定频道、特定域名后缀中搜索                                                  | 科技 site:news.163.com            |
| inurl:      | 在 url 链接中搜索                                                               | inurl:jiqiao photoshop          |
| allinurl:   | 在 url 链接中搜索, 只不过其后所有关键词均要在 url 链接中出现                                      | allinurl:jiqiao photoshop       |
| intitle     | 把搜索范围限定在网页标题中                                                             | 商业 intitle: 超级女声                |
| allintitle: | 把搜索范围限定在网页标题中; 只不过其后所有关键词均要在网页标题中出现                                       | allintitle: 超级女声 张靓颖            |
| intext:     | 把搜索范围限定在网页正文中; 忽略超链接文本、URL 以及题目等                                          |                                 |
| inanchor:   | 把搜索范围限定在链接锚文本文字中                                                          | inanchor: 吴清源                   |
| anchor:     | 检索某一作者/发明人的论著; 只在 Google Scholar 中可用                                      | anchor:/作者:                     |
| link：       | 检索所有链接到某个特定 URL 网址的网页; 只能单独使用                                             | link:163.com                    |
| cache:      | Google 网页快照                                                               |                                 |
| related：    | 检索与某特定网页类似的网页                                                             | related:www.163.com/index.shtml |
| info:       | 用来显示与某链接相关的一系列搜索; 提供 cache、similar-pages、link、related 等连接                 | info:www.sina.com.cn            |
| Index of    | 可以帮助你寻找网络和 FTP 目录                                                         | index of mp3                    |
| daterange:  | 查找在一定的日期或者一定的日期范围内; 只关注被 Google 收录的时间                                     |                                 |
| location:   | 指定地区区域内查询关键词相关的网页                                                         | wow gold location:France        |
| weather:    | 查询该地区或城市当前的天气状况                                                           | weather: 北京                     |
| stocks:     | 查询股票信息; 一般源于专业财经网站                                                        | stocks: 比亚迪                     |
| mark: :     | 返回包含查询关键词定义的网面                                                            | mark: : 暗网                      |

- Advanced Search: https://www.google.com/advanced_search
- Help: https://support.google.com/websearch/?hl=zh-Hans
- Directory: http://directory.google.com/

## [[google-voice|Google Voice]]

---
titile: Privacy
aliases:
  - 隐私
created: 2023-08-06T07:58:30
created-link: "[[20230806]]"
modified: 2025-01-17T09:57:10
description: 隐私一旦和政治挂钩，那么就不再是一种可有可无的东西，其事关 Everything
tags:
  - politics
  - privacy
type:
---

## Why

即使生活在远离网络世界的 [社会](china) 中，也有无处不在的监控、人脸识别和探针，即使这里隐私的洼地，也是这片入地的常态，但这不应成为我们习以为常的共识。

### 埋点

实际上，无论是 Web 应用，还是手机 APP，甚至是小程序，都充满了跟踪器，业内我们一般称之为「埋点」，即「数据采集」。

我是从 2024 年才开始真正重视起这个方面的，但其实没有任何办法，你总不能不用那些应用程序，我司用的是 [神策埋点](https://www.sensorsdata.cn/)，单日采集量在 2000W 左右，被公司用来做行为分析来用。如果这是匿名的，那无可厚非，但我司在采集过程中，每一条数据都是关联用户的。

这些不合规的行为用户不可能知道，也永远不会知道，你会被这个黑箱欺骗，用你最宝贵的时间，化为别人服务器上的商业数据。

Apple 曾发布过一篇隐私科普 PDF —— 《[记父女公园一日游](https://web.archive.org/web/20230322171610/https://www.apple.com.cn/privacy/docs/A_Day_in_the_Life_of_Your_Data.pdf)》讲述整个过程。非常讽刺，也令人伤心的是，Apple 为了更多的利润，也开始定向投入更多广告，这篇文章也在 2023 年之后，被删除了。

### 数据是自然界的「石油」

没有生命力的石油是可以随便出口的，哪怕是敌对的国家，也不在意两国互换石油。但是数据不一样，数据的生命力让数据的迁移和人口的迁移没有什么两样。如果人类到某国需要签证，那么数据也需要签证。

https://www.solidot.org/story?sid=65706

## Virtual SIM 虚拟手机号

### Google Voice

> [!note]
> 我今天尝试研究了一下用 api 识别 gv 号码的可行性。发现如果这些软件想给 gv 号码清理门户的话，实在是太简单了。携号转网是可以。转网之后记录也会更新。
>
> https://www.twilio.com/lookup
>
> Gv 号码显示的是 Google bwi bandwidth.com 如果转成 project fi 就变成 T-Mobile 了。 我有两个号，只有个位数不一样。一个是 gv 一个是 fi，结果很明显，他们不是靠号段判断运营商的。
>
> — https://www.v2ex.com/t/384812

#### 保号

IFTTT 的定时拨号服务御用号码，是机器人

```
+1（415）787-4253
```

亚马逊免费客服电话

```
+1（888）280-4331 
```

> Google may reclaim your Google Voice number (if you have one) if you do not appear to be making use of the service as it was intended, such as placing calls or sending text messages for a period of 3 months. We advise checking your email for notifications regarding any such number reclamation based on account inactivity.
> via: https://support.google.com/voice/answer/9230450

> You will lose your Google voice number after 30 days of inactivity. Google reassigns unused numbers after 30. To keep your number active need to **make at least 1 call or text per month**.
> via: https://www.mga.edu/telework/docs/Google_Voice_Handbook.pdf

#### Support status
- [x] https://www.douban.com
- [x] https://telegram.org
- [x] https://www.wechat.com
- [x] https://x.com
- [x] https://www.bilibili.com
- [x] https://www.zhihu.com
- [x] https://leetcode.cn
- [ ] https://store.steampowered.com
    - VOIP 不符合安全策略，via: https://help.steampowered.com/zh-cn/faqs/view/7EFD-3CAE-64D3-1C31

### eSIM

Skinny 现在基本买不到了，每次都是 `eSIMs are currently out of stock.` 所以我买了 giffgaff：

|                   | 🇺🇸美国 Ultra Mobile    | 🇬🇧英国 giffgaff | 🇳🇿新西兰 Skinny                                             |
| ----------------- | ---------------------- | --------------- | ---------------------------------------------------------- |
| **月租**            | 3 美元                   | 免费              | 免费                                                         |
| **收短信**           | 0.1 美元/条               | 免费              | 免费                                                         |
| **发短信**           | 0.5 美元/条               | 0.3 英镑/条        | 0.8 新元/条                                                   |
| **接电话**           | 3.59 美元/分钟             | 1 英镑/分钟         | 1.15 新元/分钟                                                 |
| **打电话**           | 3.59 美元/分钟             | 1 英镑/分钟         | 2.3 新元/分钟                                                  |
| **流量**            | 美国 0.2 美元/MB           | 0.2 英镑/MB       | [官网套餐](https://www.skinny.co.nz/pricing/overseas-roaming/) |
| **充值**            | 官网或 App                | 官网或 App         | 官网或 App                                                    |
| **保号**            | 交月租                    | 每半年发一条短信        | 每年发一条短信                                                    |
| **eSIM**          | 支持                     | 支持              | 暂不支持                                                       |
| **Wi-Fi Calling** | 每月免费 100 分钟电话和 100 条短信 | 暂不支持            | 支持                                                         |
| **实名**            | 非实名                    | 非实名             | 非实名                                                        |

#### 英国 Giff Gaff

## Email

> [!tip]
> 其实很多社区不会验证你的邮箱的正确性, 所以如果你不 care 未来的话, 几秒就可以拿到一个账号..

注册之前，可以去 https://github.com/jdm-contrib/jdm 了解下账号是否可以注销，

### Online
- https://temp-mail.org/zh/

### Outlook

Outlook 支持别名 [^alias-outlook]，。

这样还有另一个好处，你可以同时注册无数个小号，却只用了同一个邮箱 [^sepreate-email]，比如我叫 `hx`，那么我就可以注册：

```shell
hx@outlook.com   # PRIMARY
hxcn@outlook.com # 🇨🇳
hxtw@outlook.com # 🇹🇼
hxus@outlook.com # 🇺🇸
hxjp@outlook.com # 🇯🇵
```

当然，如果添加别名的次数过多，那么就会触发如下警告：

> [!warning]
> 我們會限制將別名新增至您帳戶的頻率。請稍後再試一次。We limit how frequently you can add aliases to your account. Please try again later

## Nickname

你可以取一个烂大街的名字，来掩盖自己的账号，如张三、李四等等，每个平台的名字最好不要重合。

```

ㅤ
ً
god
1024
2048
4096

cpp
java
py / python

su
sudo

int
bool
true
false
float
double

if
else
while

user
usr

foo
bar

张三
法外张三

91X 先生

Administrator
google
twiter
tumblr
```

## Delete Account

截止目前，我注销了如下服务：

- [x] 20210101：[QQ Zone](https://qzone.qq.com/)
    - [Delete Page](http://imgcache.qq.com/qzone/web/qzone_submit_close.html).
    - Backup Using [chrome extension](https://chrome.google.com/webstore/detail/aofadimegphfgllgjblddapiaojbglhf?hl=zh-CN).
- [x] 20210211：Xunlei + Ximalaya + Weibo + FB ~~+ IG~~
- [x] 20210301 抖音 + 最右
- [x] ~~20210313：拼多多分号~~
- [x] 20210319：Amap, Kugou.
- [x] 20210322：[京东白条](https://jr.jd.com/)
    - via: [终于把京东白条网贷给注销了! - V2EX](https://www.v2ex.com/t/442257)
- [x] ~~20210415：QQ, Wecha, Meiturn, Pindodo, Ele, Taobao to VMOS Pro~~.
- [x] 20210727：~~WeiBo +~~ 扇贝编程
- [x] 20210823：[csdn](http://csdn.com/)
- [x] 20210823：[vivo](https://www.vivo.com/)
- [x] 20210923：[Gitee](http://gitee.com/)
    - QQ support
- [x] 20210927：[DouBan](https://douban.com/)
    - Backup Using [doufen-org/tofu](https://github.com/doufen-org/tofu)
- [x] 20221002：[Netease Music](https://music.163.com/)
- [x] 20211123：[Youdao Dict](http://www.youdao.com/)
    - Write Letter.
- [x] 20220201：[Teamviver](https://www.teamviewer.com/)
- [x] 20220501：[GitBook](https://www.gitbook.com/)
- [x] 20220504：[Taptap](https://www.taptap.com/)
    - QQ support
- [x] 20220513：[Disqus](http://disqus.com/)
- [x] 20220525：[MuBu, 幕布](https://mubu.com/)
      - [work order, 申请工单](http://t.cn/A6vmvEdU).
- [x] 20220905：[Authy](https://authy.com/)
    - [Authy vs 2FAS - I need help : Bitwarden](https://www.reddit.com/r/Bitwarden/comments/sexzww/authy_vs_2fas_i_need_help/)
- [x] 20220910：[Trello](https://trello.com/)
- [x] 20221011：[QQ Music (+Wechat)](http://music.qq.com/)
- [x] 20221012：[Dribbble](https://dribbble.com/)
- [x] 20221031：[StackShare](https://stackshare.io/bgzocg); [GitKraken Account](https://app.gitkraken.com/goodbye);
- [x] 20221102：[Zotero | Your personal research assistant](https://www.zotero.org/);
- [x] 20221210：[Autodesk | 3D Design, Engineering & Construction Software](https://www.autodesk.com/); [ArtStation - Explore](https://www.artstation.com);
- [x] 20221219：[宝塔面板](https://www.bt.cn/)
- [x] [其乐社区](https://keylol.com/suid-1205865)
    - 假注销, 绑定了 MjEwNA@qq.com, 来年换一个邮箱...
    - 发帖申请注销还需要绑定手机号, 简直魔幻...
- [ ] 阿里小号注册下一堆招聘网站
- [ ] 网易严选
- [ ] 咕咪音乐
- [ ] 百度
- [ ] 京东
- [ ] 七牛云
- [ ] 米哈游
- [ ] osu
- [ ] utools
- [ ] 华为云会议 130

## Phone

手机是最容易泄漏个人信息的，建议传感器一类非必要不开启

```
Developer Options\Quick settings developer tiles\Sensors off
```

## [Browser](browser) search enginee

内置的 Google 引擎往往携带了非常多厂商定义的参数，比如 Edge 就是这样，如果你搜索 `test`，URL 会变得非常丑 [^search-params]：

```
https://www.google.com/search?q=test&oq=test&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYQTIGCAgQRRhB0gEIMTA4OGowajGoAgCwAgA&sourceid=chrome&ie=UTF-8
```

请直接替换：

```
https://google.com/search?q=%s&ie=UTF-8
```

## ​Good habits

- [ ] WiFi 随机 MAC 地址，via: https://www.v2ex.com/t/799831
- [ ] 查看公司口碑，是否符合 GDRP；
- [ ] 在电梯里，地铁里，咖啡厅等公开地方，输入密码会注意头上有没有摄像头；
- [ ] 电子产品离开视野，必定手动锁定；
- [ ] 每个账号绑定的邮箱都是独立的，采用随机 UUDI 的形式，哪里泄漏马上就知道；
- [ ] 定期商业投毒；

> 想做个针对监听隐私的投毒软件
> 随机播放一堆文字给智能音箱
> 随机访问淘宝污染用户画像
> 随机访问网页，污染历史记录
> 随机刷定位等等
> 随机抖音搜视屏污染用户画像
> 你听归你听，听的真不真又是另外一码事，感觉这软件商业收费应该也有人用。
> 和爬虫中的投毒机制差不多
> https://www.v2ex.com/t/796421

> 你死了，但是你的数据载体永生。那么，既然无法注销，那么应对？我选择给他们投毒。就像用不重复的大文件占用某些云盘的空间一样（百度云），既然我不喜欢你，你还拼命膈应我，那么我就只能“以彼之道还施彼身”了。怎么投毒呢？比如微信，既然不让注销，那么我拼命发朋友圈，所有内容都是毫不相干但是又看起来像是广告的，**总之干扰腾讯他们的数据分析，模糊你原来的数据，就行了
> https://www.v2ex.com/t/799827

## Links

- ~~[9 块钱申请一个新西兰手机号，最少可用 2 年](https://github.com/CY-Christin/CY-Christin-Blog/blob/master/9 块钱申请一个新西兰手机号.md)~~
- [可能是目前最全面的 giffgaff 使用指南 - V2EX](https://v2ex.com/t/987901)
- [Google Voice简介及使用&保号 - Newlearnerの小站](https://www.newlearner.site/2019/06/15/google-voice.html)
- [Google voice拨打电话自动挂断的原因及解决办法 – Google Voice中文网](https://www.googlevoice.cn/wifi-calling-auto-offline)
- [台湾苹果id怎么注册？台湾id的注册教程！(组图) | Tokyo Blog](http://www.hellokvm.com/?p=11069)
- https://www.v2ex.com/t/771550
- [  - Zero Width Space: U+200B - Unicode Character Table](https://unicode-table.com/en/200B/)
- [微信如何设置空白昵称？ - 知乎](https://www.zhihu.com/question/54624230)
- [微信, QQ, 微博, 淘宝, 支付宝, 京东, 百度, 网易 注销指南](https://sspai.com/post/43381),
- [网名生成器、姓名生成器、名字在线生成器](https://www.qmsjmfb.com/)

[^alias-outlook]: https://support.microsoft.com/en-us/office/add-or-remove-an-email-alias-in-outlook-com-459b1989-356d-40fa-a689-8f285b13f1f2
[^sepreate-email]: 比如你可以每年都换一个新的邮箱名，到了第二年可以直接把去年的地址删除，这样商家就联系不到你了。也可以区分 [[pages/git|git]] 提交记录，机器人提交的就不计入自己的热力图，这也是个好办法；
[^search-params]: The `gs_lcrp` could be found on [Git at Google](https://chromium.googlesource.com/chromium/src.git/+/e2ad407421b119f069f44fa4d8f9a01ee2d3ee73), which meaning is `Google Search Link Click Rank Position`. ==That's used to record which link users click on the search result page and transmits the link's ranking position to Google when users click on it, allowing Google to track user behavior and the effectiveness of search results==. The most funny thing is the `sourceid` is set to `chrome` ) via: https://webapps.stackexchange.com/questions/116105/what-are-the-different-parameters-used-in-google-search

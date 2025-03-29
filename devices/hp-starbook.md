---
title: HP 星Book 14 2024
aliases:
  - HP 星Book 14 2024
cover: 
created: 2024-07-14T14:09:13
modified: 2025-03-22T14:57:33
description: 硬盘是后换的，800
cpu: R7-7840H
gpu: 780M
ram: 32G
ssd: 2T
price: 5986
tags: 
- consume/give-for-free
type: 3c
wikipedia:
---

跟大多数人一样，高考之后，手机和电脑都是人生第一次真正拥有，此前回顾都是捡长辈不用的垃圾当宝。加上平日辗转各大补习班的功夫，虽然曾经暗自下了好几次决心要精通电脑，但都一直都没能静下心来贯彻到底。那个时候只是匆匆地比较了一下 CPU，挑了一张入门显卡，第二天电脑就到手了。想来已经过去四年，内存和硬盘在过去的日子不断加码，总是感觉焦虑，双双翻了四倍，

现在我毕业了，第一次把手里的 Windows11 Insider Version 抹掉，换了 Archlinux，虽然不及 Ubuntu，但好在初见良好，但剧烈的阵痛还是把我拉回了 Windows，我已经不能再能忍受我手上这台笔记本和 Linux 不相容的驱动。浪费在这些层面的每分每秒都让我无比想念 Win 的开箱即用，这简直是在谋财害命。傻瓜式的开箱即用，很难不说是一件美事。尤其是重装系统的时候，Winodws Update 好像真的很好用。

最大的推动力是对 Mac 的失望，以及家里老旧 PC 的淘汰。自打之前对 Mac 的去魅，真的对 Mac 有了天然的抵抗性，一天的体验使用下来，真的和 Linux 别无二致。嗯，我坚信他不值两万，或者说，两万的笔记本，很难不是这个样子的，甚至应该比他更好，但是很少有两万的轻薄本。老旧的 PC 似乎迫使我选择一台能战未来的机器，在能接受的价位挑了又挑，最后，我想，为什么不能是我手上这台笔记本呢？这台笔电我足够了解，也许才是更好的选择。

距离回家的火车出发还有 4 天，我已经不再允许自己有什么大笔的消费，如果时隔春节快递停运，错过了退货的时机的话，那就得不偿失了。

我有一个朋友，我在他那里见过任何一台刚发售的手机，见过 Switch、Xbox、MR、iPadPro 等这些不寻常的玩意，今天，我又在朋友圈里看到他考研过后新攒的海景房，兴许是已经上岸，只得暗自恭喜。回过头来想想自己，和他比起来，我总不好意思说自己是一个发烧友。我想，如果没能成为一个合格的消费者，好想连这样自证的标签都羞于贴在身。

只是，我怀疑，这是消费主义的陷阱，或是打小被培养的画地为牢。我对大笔的消费总是很敏感。如果一下子要让我闭着眼睛掏出全部的积蓄，或许只剩下信仰了吧？但是自打染指阴谋论的腔调之后，我谁都不信，国家、民族、尊严这种形而上的东西只是文化的一种套牢。我相信地球、星河与宇宙，这些我看得见，摸得着的东西，让我无尽沉迷。但我总要有东西来写下这种感动，享受这种灵魂上的冲击，所以我喜欢电子产品。

碍于家境贫寒，人生中第二台电脑承载了我太多幻想，这幻想是如此沉重，我几乎看遍了 2024 年发售的所有机器，却只想静静地当一位座上宾，静静等待能让我为之动心，闭眼交上所有积蓄的机器。至少不会是苹果。

### [[windows]] 调教

- [x] [[~为什么 windows 是用 c 语言编写的，却默认对文件大小写不敏感]]
- [x] #gtd/todo [Windows 开启 Hibernate](https://zhuanlan.zhihu.com/p/527318720)
    - 今天去银行柜台休息区，终于遇到 7840H 睡死的 BUG，所以还是很后悔着急买了这个中国特供芯片的笔记本。看起来短时间不能让他休眠了，Hibernate 会更加合适一些。
    - 睡死的 BUG 的原因？

- [ ] 优化 [[firefox]] 浏览器占用
  - http://zenki2001cn.github.io/Wiki/Debian/Firefox%E5%86%85%E5%AD%98%E5%8D%A0%E7%94%A8%E9%AB%98%E7%9A%84%E4%BC%98%E5%8C%96%E6%96%B9%E6%B3%95.html
- [ ] Reset Apple MagicTrackPad
    - https://devicechecker.org/blog/how-to-reset-a-magic-trackpad/
    - https://discussions.apple.com/thread/2720347?sortBy=best

## ==HP StarBook Pink Color==

收到电脑，跳过联网登录，检验完外观、硬盘、屏幕，解锁硬盘 BitLocker，就用 PE 开始迁移系统，随后拆机，拔电池，放静电，换固态，上电测试，没问题后合上卡扣。

不得不说，惠普的卡扣机真难拆，我的上台惠普游戏本也是卡扣，早不如当初的紧致，缝隙变得松松垮垮，很难让人喜欢。况且今天是第一次拆，就已经掰断两个卡扣...

没有电池上电测试的时候一切正常，但是扣上电池，电脑就开始反复重启，虽然最后可以进入系统，但是需要等待的时间实在太长，约莫一分钟。

随后重置了一下设备，一切恢复正常，进入系统，联网激活，算是安全下车。

因为使用较多的安装包已经提前下载，所以迁移起来还是相对轻松的。点点点就完了。

随后出现的问题就是专业版激活的问题，当年在软购商城购买了一份 Windows10 专业版的激活码，现在将激活码键入后虽依旧识别，成功进入转换的状态。

随后就是代码数据的迁移了，这个比较费劲，如果是大文件用共享文件夹其实效果不错，但是如果太多的小文件还不如直接用硬盘去拷，也不如打成压缩包一次传输。

浏览器选择的时候，才发现自己又把上个电脑的数据弄丢了，从去年 3 月，到今年 2 月的全部历史，又因为重装 Linux 的缘故，丢失了。实在是一件憾事。像是丢了过去的自己，很难受。

尤其是 Chromium with google 不再支持 https://github.com/NeverDecaf/chromium-web-store/releases, 怎么也找不到方法，最后还是换回了火狐，虽然性能、稳定性不及 Chrome，但是我更愿意拥抱最近两年火狐拥抱用户的决策，包括开放拓展等等。

所以现在最大的问题就是拓展 API 和市场的差异，包括 Unlimited History 等我非常喜欢的拓展。

## AMD rather then INTEL

1. 没有用过 AMD 所以想试试
2. AMD 价格更加便宜
3. AMD 巡航上要好于 INTEL
4. R7 7840HS 听说是神 U

> 买 7000 系 AMD 续航挺好，Intel 还在用 10nn ，AMD 旗舰台积电 4nm ，能效强一大截
  — [最近想从 Macbook 切换到 Windows 笔记本，有啥坑吗 - V2EX](https://v2ex.com/t/947911)

> 然后要买 7840hs 或者 7940hs 的迷你主机，不要买 7840h ，这个中国特供的，驱动并不友好。
  https://www.v2ex.com/t/991646

## Why
### Macbook

苹果的高价变相拉长了产品的生命周期，这也意味着，生产商能为了保准利润和价格，不必参与到其他厂商的低价促销中去。就算旧机器压在仓库也没有关系，消费浪潮褪去后，投给三方渠道去销售即可。

半个月前，在实际摸过机器之后，才发现之前对苹果的种种幻想，已经对 [[macbook-pro-m2pro-16inch|Macbook Pro 祛魅]]，如：

- 融合内存架构干翻传统内存
- 无缝运行 iOS 应用

但拿到手才发现有种种限制，因为苹果就是这样：不会基于用户太多自由。

![https://www.v2ex.com/t/989322#reply22](https://i.imgur.com/ESD1uke.jpg)

- [m1pro 还值得买吗 - V2EX](https://www.v2ex.com/t/1000503): 已经畸形的定价
- Apple Silicon M1 机器学习性能简单测试 - 知乎 https://zhuanlan.zhihu.com/p/350955566
- MacBook Pro (14-inch, 2021) Benchmarks - Geekbench https://browser.geekbench.com/macs/macbook-pro-14-inch-2021-apple-m1-pro-10-core-cpu
- 来说说你买的 MacBook Pro 官翻机硬盘、电池和屏幕状况 - V2EX https://www.v2ex.com/t/906513
- Macbook Pro M3Max 36 + 1T (丐版): 现在还没有 22000 现金流
    - 看了这个帖子（[m1pro 还值得买吗 - V2EX](https://v2ex.com/t/1000503#reply20)）后，下定决定退掉 M1Pro，多攒 4000 块入手 M3Max

> 交过几次苹果税，发现苹果不按 CPU 分级，是因为存储与内存，最让『高端用户』不舒服，不得不掏钱。
>
> 其实男孩子很简单的，你不用骗他，男孩子他会自己骗自己的
>
> https://cn.v2ex.com/t/909637

> 又是老生常谈，高配 mac 应该由公司出钱购买，哪里有自己出钱给资本家购买设备的道理
> [m2 air 还是 14 寸 pro? Java 后端 - V2EX](https://v2ex.com/t/871690)

### 联想

1. 黑胶
2. 低温锡
    1. [联想哪些型号的笔记本使用了低温锡技术，这个事件有什么瓜可以吃？_游戏本_什么值得买 (smzdm.com)](https://post.smzdm.com/p/a0q3vkwz/)
    2. [【健哥说】聊聊联想小新低温锡 (youtube.com)](https://www.youtube.com/watch?v=TU8LsGcjTtE)
    3. https://zhuanlan.zhihu.com/p/351879268
3. 控评

> [!NOTE]
> 显卡吧不让说联想的坏话

### Yoga

偏贵

![[p53Hd-fK6Kw-YOGA-Pro14s轻盈版R7-7840HS#Source]]

- [联想yoga14s 翻车指北 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/351879268)

### 小新

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1N64y1E7nE&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1N64y1E7nE' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1N64y1E7nE</a></center>
线下买不到的 Air14，也没必要单独看

<iframe src="https://www.youtube.com/embed/FoFiCMeNYDc" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=FoFiCMeNYDc' target='_blank' class='external-link'>https://www.youtube.com/watch?v=FoFiCMeNYDc</a></center>

小新，溢价高，模具和拓展性也不怎么样；

- [入了联想小新 14pro 7840hs，想退货了 - V2EX](https://www.v2ex.com/t/963772)
- [新买联想笔记本，如何防止厂商流氓？ - V2EX](https://www.v2ex.com/t/846379)

### 戴尔

#### XPS Ultra 9 二合一 INTEL

前一代，性能保守护暂不考虑 https://item.jd.com/10059055970873.html

### XPS Plus 定价

看了 DELL 支持 64GB 的电脑，还是选 Macbook 更有性价比

https://www.dell.com/zh-cn/shop/%E7%AC%94%E8%AE%B0%E6%9C%AC/sr/laptops/64-gb?appliedRefinements=37698

### 华硕灵耀

看了这个视频，直接快递都没有拆，直接退回去了，太容易撞功耗墙，U5 足够，U7 浪费；

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1kc41127GY&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1kc41127GY' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1kc41127GY</a></center>

  - [ ] #gtd/canceled #性能 保守 Zenbook Ultra 7 32 + 1T
    - [华硕灵耀 14Pro 2023 入手一周使用体验 - V2EX](https://www.v2ex.com/t/939893)
    - Intel Core i9-13900H vs Intel Core Ultra 7 165H Benchmark, comparison and differences
      https://www.cpu-monkey.com/en/compare_cpu-intel_core_i9_13900h-vs-intel_core_ultra_7_165h

### 华硕幻 14

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1YP411q7rL&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1YP411q7rL' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1YP411q7rL</a></center>

真的受不了华硕家祖传的叠叠乐；

### 微星绝影

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV1kK411b75u&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV1kK411b75u' target='_blank' class='external-link'>https://www.bilibili.com/video/BV1kK411b75u</a></center>

> [!NOTE]
> 不是每个人上图吧的，买二线的都是钱少的
> ![[~BV1N64y1E7nE-中正评测-3999元-小新Air14-R7-7840U-笔记本电脑推荐2024-装机-笔记本-电脑#Source]]

### 机械革命

> 我以前以为这种品牌到手没问题就算上车成功，没想到实际是只要在手上，就是在车上，车况稳不稳全看命，为了一个电子产品，每次开机会提心吊胆的生怕点不亮。
> https://v2ex.com/t/990112

### 火影众颜

火影售后得去木叶 via https://www.coolapk.com/feed/52590148?shareKey=Nzk3MjAxNjQxNzE5NjViNjBmY2M~

### 吾空

内存 DDR5，硬盘垃圾；

https://www.youtube.com/watch?v=CdzctCUxnTE&t=6s

### 无界

板载 16G，不支持拓展；

### SD X Elite for PC

Is there a version for android? I really cannot leave away android, such as tachiyomi, termux and a lot of emulators.

> 这就是高通提前大半年画的大饼……这春秋比法，单核和 m2 比也就算了，多核也拿 m2 比？ 12 个大核 80 瓦的功耗和不到 20 瓦 4 大核的 m2 比多核性能？真的让人叹为观止。刚好 m3 的一些初步跑分出来了，简单加了上去，关键是 m3 立马就能买到，而高通的大饼要明年中才陆续上市，而再过 3 个月 m4 又出来了～
>
> [来来来，我来补充一下高通 X Elite 的 ppt](https://v2ex.com/t/987831)

## 主机？

好想配台式机啊，但是损坏率太高，移动太不方便了啊

- https://www.v2ex.com/t/848733
- https://zhuanlan.zhihu.com/p/103493966
- https://www.v2ex.com/t/653417

## References

- [2024 年想换台笔记本，老哥们有什么推荐？ - V2EX](https://www.v2ex.com/t/1012374#reply60)
- [求帮忙推荐一款适合装 Linux 的笔记本电脑 - V2EX](https://v2ex.com/t/1013900#reply6)
- 海洋的另一边的评价 https://forum.gamer.com.tw/C.php?bsn=60030&snA=629141
- 说实话，不怎么看好 ROG Air 的性能释放，但是好像也没得选？
- [CES 2024现场报道：我看了哪些新鲜科技？ - YouTube](https://www.youtube.com/watch?v=3b1iDuEj0RA)
- [够薄才够爽！ROG 2024探索沙龙探展，全新幻Air系列全网最详细解读 - YouTube](https://www.youtube.com/watch?v=Q-gj0uDq_9w&t=43s)
- [猪王帶你看看今年CES上有哪些好玩的新電腦！| 笔吧评测室 - YouTube](https://www.youtube.com/watch?v=OclJXq1SVLI)
- ultra5 65w vs r77840hs 65w
- [ROG枪神7plus，i9-13980HX、RTX4060 - YouTube](https://www.youtube.com/watch?v=cpwFDeaRVrY&t=181s)
- [ROG幻16，i9-13900H、RTX4060 - YouTube](https://www.youtube.com/watch?v=HJWFjXoARDA)
- [電競掌機 大亂鬥時代開啟 🕹️ Steam掌機 開始繁殖增生?｜ 遊戲新聞/偷閒加油站 - YouTube](https://www.youtube.com/watch?v=Q8qYwGA8KgQ&t=667s)
- [核显63帧畅玩《赛博朋克2077》！AMD重磅发布锐龙8000G处理器：已成为2024年最强核显APU - YouTube](https://www.youtube.com/watch?v=oKbhdHEbM9c)
- [相信我，今年就應該買筆記本 | 筆吧評測室 - YouTube](https://www.youtube.com/watch?v=J0Hp5w5NigU&t=696s)
- [RTX4080&4090移动版游戏表现：2K、4K游戏提升巨大！ | 笔吧评测室 - YouTube](https://www.youtube.com/watch?v=A6qiQ_JglA0&t=9s)
- [“满血显卡”的时代结束了？RTX4050/4060/4070游戏本显卡深度分析 | 笔吧评测室 - YouTube](https://www.youtube.com/watch?v=towiutdXG2k&t=631s)
- 最拥有生产力的 Linux 发行版本推荐 https://www.v2ex.com/#reply33
- [r7-7840h ==休眠睡死==的 bug 修复了吗？ - V2EX](https://www.v2ex.com/t/972937)

> 这话说的就是找茬，换手机要多少成本？大多数人都换得起。换国家要多少成本？
> —— [看了《2023 年了，我觉得 iPhone 比安卓难用很多》之后，想问各位用 iPhone 并且觉得体验很好的朋友说一下为什么 - V2EX](https://www.v2ex.com/t/939521)

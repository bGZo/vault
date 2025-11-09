---
draft: true
aliases:
  - Apple
created: 2025-03-02T20:37:37
modified: 2025-08-30T10:36:06
title: Apple
---
# Apple

> 乔布斯：“我从来不做用户调研。如果亨利·福特在发明汽车之前去做市场调研，他得到的答案一定是消费者希望得到一辆更快的马车。”
> https://t.me/zaihuanews/31366

## Account

中国日用，美国翻墙，台湾动画疯。

### Sign up

因为 Apple ID 被风控的不确定性，而且风控之后的后果相当严重，如：

1. iCloud 无法访问，未下载到设备上的 iCloud 数据将永久丢失，包括相片或者文件之类。
2. 通过这个 Apple 账户购买的软件/订阅服务都会失效不可恢复，Apple 也不会退款给你。
3. 所有绑定在这个 ID 上的 Apple 硬件将是毁灭性打击，包括但不限于：
    1. iPhone/iPad/Mac 无法登出，无法关闭查找，盲目强制 Reset 则直接变成激活锁设备
    2. AirPods 无法从账户中删除，无法完全转移 AirPods 到其他 iPhone 使用（会一直弹窗）
    3. AirTag 无法删除，无法二次使用

iPhone/iPad 之类还可以提交最原始的购买证明（如果你还找得到），尝试官方解开激活锁，其他 Apple 设备则几乎没有办法。 并且苹果也不会给你这些设备负责，包括退款，如果你的设备本身就是某鱼某宝之类第三方平台二手购入的，那直接宣判死亡。[^apple-ban-id]

因此，我排斥对 Apple Store 的付费，能避免就尽量避免。

### Fake Profile

Using https://www.bestrandoms.com/random-address

```shell
John Smith (first name(given name), last name)
via: https://www.zhihu.com/question/19864402
---
(406) 443-4577
10 Alta St
Helena, Montana(MT), 59601
---
电话
道路地址
市名, 州名(缩写), 邮编
```

注册好了就不用挂代理了, 兑换, 购买, 下载全部可以在国内网络进行.

### Gift card

美区 Apple ID 用非人哉借记卡购买失败，日区有人成功过，via: https://bgm.tv/group/topic/372135

我个人猜测是发行终止了和美区的交易, 这位也是 2020 年用美区非人哉借记卡突然被封. via:https://www.v2ex.com/t/720736

#### `PockytShop`

> 支付宝 -> 左上角切换城市 /选择洛杉矶
>   -> 搜索「PockytShop」小程序 -> 输入购买金额 -> 直接买
>   -> 搜索「由我付」小程序 -> 绑定美国手机号 -> 绑定实名身份 -> 直接买
> https://shop.pockyt.io/pc/home
> https://www.v2ex.com/t/1052316

#### 其他三方渠道

### 转区

- [中国区的Apple ID转地区到美国区会出现什么问题吗？ - 知乎](https://www.zhihu.com/question/31841333)

## Develop

> #only-apple-can-do
> 非常反直觉的一个条款
> https://www.reddit.com/r/iOSProgramming/comments/13jhfh1/can_i_have_my_app_for_personal_use_without_paying/

### Reading list

这两天一直在用 safari 的 reading list，不用考虑多端同步真是太节省时间了，也许就是我懒，但有这些 hook，真的能让我专注于本应该做的事情。这还是挺重要的。

### iCloud 无法同步 `.git`：每个机器不一致

https://stackoverflow.com/questions/35853139/can-git-and-icloud-drive-be-effectively-used-together

Apple 的风格就是这样，当你面向中上产做产品的时候，你会丢掉非常多烦恼，用户群本身的高学历、高资产就像是拥有丰富羊毛的羊群，讨好商客，就能换来开发者，换来良好的生态。

## Fuck [[pages/apple-music]]

### 音乐库是会受审查的

因为你无法找到下面的歌手 / 歌曲，您可以试试：

```diff
  - 童话镇 - 陈一发儿
  - 关于郑州的基于 - 李志
  - 差不多先生 - hotdog
```

### 非会员和狗不得入内

是的，你没有权利访问你的歌单，除非开会员

- 这对迁移数据的用户是恼人的，所以就算我开着 AM 的会员，我依然不会创建自己的歌单；
  - 我知道就算创建了，他也不属于我，而是库克 😅

### 安卓直连网络很卡

不如 iOS，总是卡卡的，现象在登录之后会好转；

### 跨国家分享是不可能的

或者说，折腾成本是非常高的；

- https://discussionschinese.apple.com/thread/140136779
- https://zhuanlan.zhihu.com/p/377114774

### iTunes 锁区

## Fuck apple tv

### 为什么要嵌入 Safari 呢？

为什么不呢？

浏览器能做的事情，远远大于电视盒子吧？

- 用户隐私、财产安全是一个问题，官方当然可以用协议撇开责任；
- 生态破坏，讨好用户的话，只会打击商家做苹果生态的信心，是对生态的降维打击；
- 交互的不好做，这是另一个操作系统；

当然你可以用 `ayiVideo`，但依据苹果傲慢的态度，将永远不予上架，并且你还得用交每年 99 刀的保护费，所以为什么要做呢？

<iframe src="https://www.youtube.com/embed/n49lVxMM4YA" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=n49lVxMM4YA' target='_blank' class='external-link'>https://www.youtube.com/watch?v=n49lVxMM4YA</a></center>

[^apple-ban-id]: 为什么不能登录 iCloud? 听说一旦登陆就会封号? https://www.v2ex.com/t/645534, https://www.v2ex.com/t/650137, https://v2ex.com/t/739530, https://www.v2ex.com/t/981649, https://www.v2ex.com/t/1013730, https://www.v2ex.com/t/1058796, https://v2ex.com/t/1105001

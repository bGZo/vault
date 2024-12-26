---
created: 2023-09-23T12:00:00
modified: 2024-12-26T08:48:25
status:
  - writing/draft
---

今天下午，EMS 取走了武汉寄过来的快递，寄去了北京。Apple 退货算是告一段落，这让我不禁开始重新想一个问题：**我真正的需求到底是什么**？

## 真正需求

即使后来也一遍一遍地在内心劝过自己，想要用 Pencil 去画画，去涂鸦，去记笔记，但至少，身为一个写代码、看漫画的人来说，但是还是觉得这是一个谎言。在这个广告宣传盖过实际产品的环境，广告是一点都不能信的。那些从产品发布会主持人嘴中吹出来的牛逼，跑出来的火车，也许就是一种诈骗。

$$性能 > 便携 > 续航$$

但是，我忽略了最重要的一件事情：生态。

## 放弃心路：反复幻灭

首先，是 Everything Paid 的味道。尤其是我最主要的内容消费平台，Safari 浏览器，Safari 相比于 [kiwibrowser/src](https://github.com/kiwibrowser/src) 只能说是一个残废。我必须短时间内改变自己多年来使用 Chromium 养成的大量操作习惯。这相当不适应，或者我就只能买 App Store 第三方开发出来的插件，当然这些事情都还好。最重要的是 Tampermonkey 的缺失（即使有 [quoid/userscripts](https://github.com/quoid/userscripts)），因为 Safari 不提供 Chrome API，油猴的大多数脚本也无法无感迁移，这让我有了第一个想退掉它的冲动。

其次，是 Apple 的闭源傲慢侧载政策。基于第一点不适，我只能开始寻求开源的替代品，但就 AltStore 这样临时的解决方案来说相当失望。因为 Apple 还有这样的限制（只支持同时 Sideload 三个应用，每周 10 个 App IDs）：

> You can sideload as many apps as you want with AltStore, but due to Apple's restrictions **only 3 sideloaded apps can be active at a time**. If you try to activate more than 3 apps, you will be prompted to "deactivate" a sideloaded app first. Deactivating an app will make AltStore back up all its data before removing it from your iPhone or iPad, freeing up a slot for you to then sideload another app. Alternatively, you can manually deactivate an app at any time by long-pressing it in the My Apps tab and pressing "Deactivate".
— [Activating Apps - AltStore](https://faq.altstore.io/how-to-use-altstore/activating-apps)

> Every app you sideload with AltStore requires a certain number of "App IDs" to be registered with your Apple ID, which depends on the number of app extensions each app contains. **You can only register up to 10 App IDs at a time**, but each App ID expires after one week. If you want to sideload an app that requires more App IDs than you have available, you'll have to wait for enough App IDs to expire.
— [App IDs - AltStore](https://faq.altstore.io/how-to-use-altstore/app-ids)

所以你只能拿到 2 个侧载 App 的资格（AltStore 自己要占一个）。总的来说，就算我已经花了 $799（￥6399）买它，但我还是需要为它的软件政策每年付 $99 给 Apple? 真的有人愿意坚守这样的平台吗？[无法分配内存、也无法创建子进程，即使是本人，也无法独立 Build 应用程序 (必须花钱去签名)的平台？](https://developer.apple.com/forums/thread/128859)

What A Fucking Joke?

然后，是续航，官方标称的 10 个小时简直让人控诉诈骗。因为我的体感最多也就是 5 个小时，已经掉到了 20% 以下，这还没有接键盘，也没有上蜂窝（带笔）。就如同这个 [视频](https://www.youtube.com/watch?v=VtYL0Ye1vP8) 结尾测试数据一样，高强度 Safari 一个小时掉电 20% 是稀松平常的事情。和 Mac 上十多个小时的续航相形见绌。

最后一点是，当我想到自己手中这台鸡肋的设备其实等于 2 个 Steam Deck(Arch Linux) 的时候，我彻底的放弃了。

Okey, It's not worth any more.

> 我不在信任苹果制造产品的出发点是为了更好的用户体验，赤裸裸的用所谓商业策略来对消费者行使心理操纵以保证他们的利润。2022 年了跨不过的还是 64g ，60hz ，这俩坎。
—  [iPad Pro M2 版本已经发布 - V2EX](https://www.v2ex.com/t/887936)[^1]

Apple, you fool your customer.

[^1]: 关于此类话题的更多讨论，可见：[iPad Pro 算是好产品么？ - V2EX](https://v2ex.com/t/954360)、[放弃 iPad Pro 的原因、AI 继续驱动应用创新、Android 14 新特性](https://iois.me/archives/15061.html) ；

---
aliases:
  - deep-linking/mobile
  - URL Scheme
created: 2022-11-28T00:00:00
modified: 2025-07-17T21:56:00
title: URL Scheme
wikipedia: https://en.wikipedia.org/wiki/List_of_URI_schemes
---

# URL Scheme

Link to a specific location within a mobile app rather than simply launching the app.

## Why

## How

## What

The format of the URI used to trigger or deep link an app is often different depending on the mobile operating system.

- [[android|Android]] devices work through **intents**
	- https://developer.android.com/guide/components/intents-filters
- BlackBerry 10 devices work through BB10's invocation framework
- **Firefox OS** devices work through **Web Activities**
- [[ios|iOS]] devices work through the **openUrl application** method
	- https://developer.apple.com/documentation/uikit/uiapplication#jumpTo_37
- **Windows Phone 8 devices** work through the **UriMapper class**

## References

### [[telegramdesktop-tdesktop|telegram]]

```shell
tg://resolve?domain=<bot_username>
```

[Deep links](https://core.telegram.org/api/links)

### Ali Scanner

```shell
alipayqr://platformapi/startapp?saId=10000007
```

### Alipan

```shell
smartdrive://share/browse?shareId=EDgMfoP5XbA
```

### Pinduoduo

- `pinduoduo://com.xunmeng.pinduoduo/search_result.html?search_key=%s`
- `pinduoduo://goods2.html?goods_id=270513197618`
- `https://mobile.yangkeduo.com/goods2.html?goods_id=270513197618`

### Eudic

- `eudic://dict/%s`

### 电商

```shell
<string>taobao</string><!-- 淘宝  -->
<string>tmall</string><!-- 天猫  -->
<string>jdlogin</string><!-- 京东  -->
<string>pinduoduo</string> <!-- 拼多多  -->
<string>kaola</string> <!-- 网易考拉  -->
<string>yanxuan</string> <!-- 网易严选  -->
<string>vipshop</string> <!-- 唯品会  -->
<string>suning</string> <!-- 苏宁  -->
<string>mishopv1</string> <!-- 小米商城 -->
<string>wireless1688</string> <!-- 阿里巴巴 -->
```

### 社交、社区

```shell
<string>weibo</string><!-- 微博 -->
<string>zhihu</string><!-- 知乎 -->
<string>xhsdiscover</string><!-- 小红书 -->
<string>momochat</string><!-- 陌陌 -->
<string>blued</string><!-- blued -->
<string>mqzone</string><!-- QQ空间 -->
<string>mqq</string><!-- QQ -->
<string>tantanapp</string><!-- 探探 -->
<string>huputiyu</string><!-- 虎扑 -->
<string>com.baidu.tieba</string> <!-- 贴吧  -->
<string>tianya</string> <!-- 天涯社区  -->
<string>douban</string> <!-- 豆瓣 -->
<string>jike</string> <!-- 即刻 -->
```

### 短视频

```shell
<string>snssdk1128</string> <!-- 抖音 -->
<string>snssdk1112</string> <!-- 火山 -->
<string>snssdk32</string> <!-- 西瓜视频 -->
<string>gifshow</string> <!-- 快手 -->
```

### 视频/直播

```shell
<string>tenvideo</string> <!-- 腾讯视频  -->
<string>youku</string> <!-- 优酷  -->
<string>bilibili</string> <!-- B站  -->
<string>imgotv</string> <!-- 芒果TV  -->
<string>qiyi-iphone</string> <!-- 爱奇艺  -->
<string>hanju</string> <!-- 韩剧TV  -->
<string>douyutv</string> <!-- 斗鱼  -->
<string>yykiwi</string> <!-- 虎牙  -->
```

### 图片处理

```shell
<string>mtxx.open</string> <!-- 美图秀秀  -->
<string>faceu</string> <!-- faceu国内  -->
<string>ulike</string> <!-- 轻颜国内 -->
```

### 资讯

```shell
<string>snssdk141</string> <!-- 今日头条  -->
<string>newsapp</string> <!-- 网易新闻  -->
<string>qqnews</string> <!-- 腾讯新闻  -->
<string>iting</string> <!-- 喜马拉雅 -->
<string>weread</string> <!-- 微信读书 -->
<string>jianshu</string> <!-- 简书 -->
<string>igetApp</string> <!-- 得到 -->
<string>kuaikan</string> <!-- 快看漫画 -->
```

### 财经

```shell
<string>sinanews</string> <!-- 新浪财经  -->
<string>amihexin</string> <!-- 同花顺炒股 -->
```

### 音乐

```shell
<string>orpheus</string> <!-- 网易云音乐  -->
<string>qqmusic</string> <!-- qq音乐  -->
<string>kugouURL</string> <!-- 酷狗  -->
<string>qmkege</string> <!-- 全民K歌 -->
<string>changba</string> <!-- 唱吧  -->
```

### 工具

```shell
<string>iosamap</string> <!-- 高德地图  -->
<string>baidumap</string> <!-- 百度地图   -->
<string>baiduyun</string> <!-- 百度网盘  -->
<string>rm434209233MojiWeather</string> <!-- 墨迹天气  -->
```

### 办公

```shell
<string>wxwork</string> <!-- 企业微信  -->
<string>dingtalk</string> <!-- 钉钉 -->
```

### 生活

```shell
<string>imeituan</string> <!-- 美团  -->
<string>dianping</string> <!-- 点评  -->
<string>cainiao</string> <!-- 菜鸟裹裹  -->
<string>wbmain</string> <!--  58同城 -->
<string>mihome</string> <!--  米家 -->
```

### 美食佳饮

```shell
<string>xcfapp</string> <!-- 下厨房  -->
<string>sbuxcn</string> <!-- 星巴克中国  -->
<string>meituanwaimai</string> <!-- 美团外卖  -->
```

### 运动健康

```shell
<string>fb370547106731052</string> <!-- 小米运动  -->
<string>meetyou.linggan</string> <!-- 美柚  -->
<string>babytree</string> <!-- 宝宝树  -->
<string>keep</string> <!-- keep  -->
```

### 旅行

```shell
<string>CtripWireless</string> <!-- 携程  -->
<string>diditaxi</string> <!-- 滴滴  -->
<string>taobaotravel</string> <!-- 飞猪  -->
<string>travelguide</string> <!-- 马蜂窝  -->
```

### 游戏

```shell
<string>tencent1104466820</string> <!-- 王者荣耀  -->
<string>tencent100689805</string> <!-- 天天爱消除  -->
<string>tencent382</string> <!-- QQ斗地主  -->---
```

### App Store

```shell
{
xiaomi: {
    reg: /\(.*Android.*(MI|Mi|Redmi).*\)/,
    scheme: "mimarket://details?id=com.xx.xx"
},
samsung: {
    reg: /\(.*Android.*(SAMSUNG|SM-).*\)/,
    scheme: "samsungapps://ProductDetail/com.xx.xx"
},
huawei: {
    reg: /\(.*Android.*(HUAWEI|HONOR).*\)/i,
    scheme: "appmarket://details?id=com.xx.xx"
},
oppo: {
    reg: /\(.*Android.*OPPO.*\)/,
    scheme: "oppomarket://details?packagename=com.xx.xx",
    downloadFirst: !0
},
vivo: {
    reg: /\(.*Android.*(vivo|VIVO).*\)/,
    scheme: "vivomarket://details?id=com.xx.xx"
}
```

## References

- [应用列表 | 捷径社区](https://sharecuts.cn/apps)
- [常见App Scheme整理](https://zhuanlan.zhihu.com/p/47837970)
- [求调用安卓各大应用市场的url scheme - SegmentFault 思否](https://segmentfault.com/q/1010000005116145)

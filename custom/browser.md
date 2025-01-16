---
aliases:
  - safari
  - firefox
  - kiwi
  - chrome
  - 浏览器
  - chromium
titile: 
created: 2024-07-28T12:00:00
created-link: "[[20240728]]"
modified: 2025-01-15T09:14:03
description: 
tags:
  - tool
type: tool
---

## Firefox

### Profile

```
.
├── AlternateServices.txt
├── ClientAuthRememberList.txt
├── SecurityPreloadState.txt
├── SiteSecurityServiceState.txt
├── Telemetry.FailedProfileLocks.txt
├── addonStartup.json.lz4
├── addons.json
├── autofill-profiles.json
├── blocklist.xml
├── bookmarkbackups # This folder stores bookmark backup files,
|                   # which can be used to restore your bookmarks.
├── broadcast-listeners.json
├── browser-extension-data
├── cert9.db        # all your security certificate settings and
|                   # any SSL certificates you have imported into
|                   # Firefox.
├── cert_override.txt
├── compatibility.ini
├── containers.json # the details of containers used by the Container
|                   # Tabs feature, including those created by extensions
|                   # such as Facebook Container.
├── content-prefs.sqlite # Site-specific preferences:
├── cookies.sqlite       # a bit of information stored on your computer
|                        # by a website you’ve visited
├── crashes
├── datareporting
├── enumerate_devices.txt
├── extension-preferences.json
├── extension-settings.json
├── extensions           # stores files for any extensions you have installed
├── extensions.json
├── favicons.sqlite      # all of the favicons for your Firefox bookmarks.
├── features
├── formhistory.sqlite   # This file remembers what you have searched
|                        # for in the Firefox search bar and what
|                        # information you’ve entered into forms on websites.
├── gmp
├── gmp-gmpopenh264
├── gmp-widevinecdm
├── handlers.json        # preferences that tell Firefox what to do when
|                        # it comes across a particular type of file.
├── key4.db              # Passwords
├── logins-backup.json
├── logins.json          # Passwords
├── mediacapabilities
├── memory-report.json.gz
├── minidumps
├── notificationstore.json
├── parent.lock
├── permissions.sqlite   # Site-specific preferences
├── pkcs11.txt           # security module configuration.
├── places.sqlite        # This file contains all your Firefox bookmarks
|                        # and lists of all the files you've downloaded
|                        # and websites you’ve visited.
├── pluginreg.dat
├── prefs.js             # customized user preference settings, such as
|                        # changes you make in Firefox Settings dialogs.
|                        # The optional user.js file, if one exists,
|                        # will override any modified preferences.
├── protections.sqlite
├── saved-telemetry-pings
├── search.json.mozlz4   # This file stores user-installed search engines
├── security_state
├── serviceworker.txt
├── sessionCheckpoints.json
├── sessionstore-backups
├── sessionstore.jsonlz4  # the currently open tabs and windows
├── shader-cache
├── shield-preference-experiments.json
├── signedInUser.json
├── storage
├── storage-sync-v2.sqlite
├── storage-sync-v2.sqlite-shm
├── storage-sync-v2.sqlite-wal
├── storage-sync.sqlite
├── storage.sqlite
├── times.json
├── weave
├── webappsstore.sqlite   # DOM storage,  provide a larger, more secure,
|                         # and easier-to-use alternative to storing
|                         # information in cookies.
└── xulstore.json         # toolbar and window size/position settings
```

#### Windows

default location is `%APPDATA%\Mozilla\Firefox\Profiles\`[^windows-profile]

### Custom Config

#### Limit memory using

```yaml
browser.cache.memory.capacity: 8192000
```

#### History max to be keep

https://superuser.com/questions/1269516/what-exactly-does-the-number-listed-under-places-history-expiration-transient-c

```yaml
places.history.expiration.transient_current_max_pages
# https://support.mozilla.org/en-US/questions/1039372

browser.migrate.chrome.history.limit
browser.migrate.chrome.history.maxAgeInDays
# https://superuser.com/questions/1635171/firefox-doesnt-import-all-history-from-chrome

places.history.expiration.max_pages
# https://www.reddit.com/r/firefox/comments/u417w8/how_long_does_firefox_keep_history_for/
```

### User Agent (UA)

Go `about:config` to create a String named ` general.useragent.override` [^create-custom-ua]

Value could be an iPad:

```
Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10
```

Or an iPhone:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1
```

Or a Mac:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15
```

Check your current on https://www.whatsmyua.info/

More UA check via: https://www.whatismybrowser.com/guides/the-latest-user-agent/ios

## Safari

### Youtube 画中画

在 YouTube 菜单仍在屏幕上的情况下，再次右键单击以打开 Safari 的上下文菜单，就会出现 `Picture in Picture`，via: https://zhuanlan.zhihu.com/p/350035245

### Waiting features
- Put Inactive tabs to sleep
    - No way now. via: https://www.reddit.com/r/apple/comments/zvvy9k/put_inactive_safari_tabs_to_sleep_solving_the_ram/
- Keyword search
    - such as typing `wiki+%s`, could search wikipedia. via: http://www.macosxtips.co.uk/extensions/#anysearch
- Set RAM limit
    - https://discussions.apple.com/thread/1510907?sortBy=rank

## (Ungoogled) Chromium

### Install

- https://github.com/ungoogled-software/ungoogled-chromium
- https://github.com/Hibbiki/chromium-win64

### Chrome Extensions 无法使用
1. `chrome://flags/#extension-mime-request-handling` -> **Always prompt for ins**
2. Download Crx [NeverDecaf/chromium-web-store: Allows adding extensions from chrome web store on ungoogled-chromium. Also adds semi-automatic extension updating.](https://github.com/NeverDecaf/chromium-web-store) ![](https://img.shields.io/github/stars/NeverDecaf/chromium-web-store)

via: [How to Manually Install Extensions (Ungoogled Chromium) | avoidthehack!](https://avoidthehack.com/manually-install-extensions-ungoogled-chromium)

### New tab setting
- `chrome://flags/#custom-ntp`
- `chrome://new-tab-page`
- `chrome://newtab`

I really love Brave's homepage with RSS, so I found some alternatives:

- https://github.com/deepjyoti30/startpage
- https://chrome.google.com/webstore/detail/manganum-1-new-tab-for-ch/jbfeongihppeenfnaofmdeikahaefljd?hl=en-US
- https://github.com/deepjyoti30/startpage
    - ==这个拓展的配置文件不会刷新, 因为他的配置没有写在 Manifest 里面, 默认他是需要在页面内进行配置的, 也很合理==

### wontfix: playback of protected content

[spotify doesn't work · Issue #1849 · ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/issues/1849)

### wontfix: notifications
1. Native windows notifications
2. Web push application offline
    - depend on Google Cloud Message / Firebase Cloud Messaging

> Push Notifications used GCM service for client notification.For example user get unique ID for future notifications. In chrome/browser/push_messaging is located Push notifications implementation. Impossible to have client Push API notification without cloud services by Google (or Mozilla in case of Firefox browser)
> By the way, currently they migrate to FCM.
> https://github.com/ungoogled-software/ungoogled-chromium/issues/589

> Rather than use Mozilla servers, [roll your own](https://github.com/mozilla-services/autopush). I don't know if anyone has audited the source for connections to other Mozilla services.
> https://github.com/ungoogled-software/ungoogled-chromium/issues/1020

You can test notification using https://web-push-book.gauntface.com/demos/notification-examples, go `User Data\Default\Platform Notifications` to cat log for them. [^noti-log]

### Value path

- `User Data/Default`
    - Cache 大头
        - `Service Worker\CacheStorage`
        - `Cache`
        - `Code Cache`
        - `IndexedDB`
        - ...
    - `History`
    - `Bookmarks`

### Cookie manage #deprecated
##### Always

```html
[*.]leetcode.cn
[*.]bilibili.com
[*.]discord.com
[*.]duolingo.com
[*.]github.com
[*.]gmgard.com
[*.]google.com
[*.]inoreader.com
[*.]leetcode.com
[*.]live.com
[*.]logseq.com
[*.]nowcoder.com
[*.]openai.com
[*.]spotify.com
[*.]steampowered.com
[*.]v2ex.com
[*.]youtube.com
[*.]player.fm
[*.]steamdb.info
[*.]raindrop.io
[*.]gmgard.moe
[*.]anki.net
[*.]pixiv.net
[*.]south-plus.net
[*.]mastodon.social
[*.]zodgame.xyz
```

##### Never

```
[*.]twitter.com
[*.]mastodon.social
[*.]bgm.tv
```

##### Garbage

```
[*.]jp
[*.]csdn.net
[*.]weibo.com
[*.]zhihu.com
[*.]youdao.com
[*.]toutiao.com
[*.]qq.com
[*.]douban.com
[*.]baidu.com
[*.]aliyundrive.com
[*.]alipay.com
[*.]51cto.com
[*.]163.com
[*.]sina.com.cn
```

## Chromium: Brave #deprecated

除了设计得好一点, 没有一点用处, 在 Chromium 的基础上绑定了 Brave Coins 的全套插件, 然后打包释出, 可以说真正的技术点就仅仅是表面套壳的几个插件罢了, 对比 `User Data` 下产生的数据, 多出来的目录屈指可数

```shell
/mnt/c/Users/15517/Desktop/browser/diff > tree -L 3
.
├── BraveWallet
│   └── 1.0.20
│       ├── README.md
│       ├── chainlist.json
│       ├── contract-map.json
│       ├── evm-contract-map.json
│       ├── images
│       ├── manifest.fingerprint
│       ├── manifest.json
│       └── solana-contract-map.json
├── BrowserMetrics-spare.pma
├── Default
│   ├── Google Profile.ico
│   ├── Rewards.log
│   ├── ads_service
│   │   ├── client.json
│   │   ├── confirmations.json
│   │   ├── database.sqlite
│   │   └── database.sqlite-journal
│   └── publisher_info_db
├── Greaselion
│   └── Temp
├── Module Info Cache
├── SODA
├── SODALanguagePacks
│   └── en-US
├── Webstore Downloads
├── afalakplffnnnlkncjhbmahjfjhmlkal
│   └── 1.0.216
│       ├── 1
│       ├── manifest.fingerprint
│       └── manifest.json
├── aoojcmojmmcbpfgoecoadbdpnagfchel
│   └── 1.0.7
│       ├── manifest.fingerprint
│       ├── manifest.json
│       └── photo.json
├── cffkpbalmllkdoenhmdmpbkajipdjfam
│   └── 1.0.1521
│       ├── manifest.fingerprint
│       ├── manifest.json
│       ├── regional_catalog.json
│       ├── resources.json
│       └── rs-ABPFilterParserData.dat
├── gccbbckogglekeggclmmekihdgdpdgoe
│   └── 1.0.1026
│       ├── 21062e05-6c2c-495a-bccb-b681e8bdfea2.jpeg
│       ├── 3217128b-2500-4a44-857e-4340488fafd8.png
│       ├── 3c255ec1-6fad-420f-b02c-779c874615d1.png
│       ├── 51f1a8be-a766-46e9-beca-044cc10109e0.jpeg
│       ├── manifest.fingerprint
│       ├── manifest.json
│       └── photo.json
├── iblokdlgekdjophgeonmanpnjihcjkjj
│   └── 1.0.71
│       ├── dnryisldmaqljgwaxeqbuuhuvrbboqlf
│       ├── kkjipiepeooghlclkedllogndmohhnhi
│       ├── manifest.fingerprint
│       ├── manifest.json
│       └── resources.json
├── lfgnenkkneohplacnfabidofpgcdpofm
│   └── 1.0.897
│       ├── manifest.fingerprint
│       ├── manifest.json
│       ├── resources.json
│       └── rs-AC023D22-AE88-4060-A978-4FEEEC4221693.dat
├── ocilmpijebaopmdifcomolmpigakocmo
│   └── 1.0.53
│       ├── bvkgcaxyaitmhkbbqnqnqugrjeqzspxv
│       ├── emgmepnebbddgnkhfmhdhmjifkglkamo
│       ├── manifest.fingerprint
│       ├── manifest.json
│       └── resources.json
└── oofiananboodjbbmdelgdommihjbkfag
  └── 1.0.120
      ├── 6.0
      ├── manifest.fingerprint
      └── manifest.json
29 directories, 49 files
```

可以看出多出来的只是 `Brave (Rewards)Wallet + Brave Ads + Ad Block`, 所以感觉 Meaningless. 之前看过的软文 ([How To Enable Or Disable Notifications On The Brave Web Browser | PC | *2022* 👍 - YouTube](https://www.youtube.com/watch?v=86xEqFtENB8) & [Brave浏览器看广告赚取BAT Token | 完美支持MetaMask钱包 | 比谷歌浏览器快3倍，高度保护用户隐私 - YouTube](https://www.youtube.com/watch?v=QGFJ_LbUFpM)), 号称打着边挖矿边保护隐私方面, 还把 Brendan Eich 的名号搬出来, 可笑可笑

Notification not for GCM/FCM, via: [Notification problem for some web sites - Browser Support / Desktop Support - Brave Community](https://community.brave.com/t/notification-problem-for-some-web-sites/223966/17)

## Chromium: Kiwi (Android)

### Fullscreen

```js
(function() {
  var elem = document.documentElement;
  var rfs =
         elem.requestFullscreen
      || elem.webkitRequestFullScreen
      || elem.mozRequestFullScreen
      || elem.msRequestFullScreen;
  rfs.call(elem);
})();
```

via: https://github1s.com/xieby1/fullscreen/blob/HEAD/fullscreen.js#L1-L9, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call

## Chromium: Chrome #deprecated

### Privacy Problem

### Extension Version

- [3 月 15 日谷歌就要停止第三方 chrome 浏览器的同步功能了，我该怎么办？ - V2EX](https://www.v2ex.com/t/761099)
- [Will my organization's Chrome extensions with manifest v2 run after Jan 2023? - Chrome Enterprise Community](https://support.google.com/chrome/a/thread/175260822/will-my-organization-s-chrome-extensions-with-manifest-v2-run-after-jan-2023?hl=en)
- [巨坑：chrome extensions绝对不要升级到V3 - 掘金](https://juejin.cn/post/7094545901967900686)

## Chrome: Edge

[^windows-profile]: via: [MZHistoryView: View the list of visited web sites in Firefox / Mozilla browsers](http://www.nirsoft.net/utils/mozilla_history_view.html) & https://support.mozilla.org/bm/questions/754699
[^create-custom-ua]: [Is there any way to change user agent string on Firefox 80.1.3 for Android? : r/firefox](https://www.reddit.com/r/firefox/comments/it7jqx/is_there_any_way_to_change_user_agent_string_on/)
[^noti-log]:https://superuser.com/questions/1035042/is-there-any-way-to-view-chrome-browser-notifications-history

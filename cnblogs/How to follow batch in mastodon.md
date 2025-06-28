## Import `csv` from setting

> [!Warning]
> 存在超時的問題，並且無法得知是哪些賬戶，雖然我的導入大部分是成功的，但現在一直顯示導入中。可能的原因是關注的賬戶存在「加鎖」問題，有些賬戶並不希望被大量的不認識的人關注，所以需要在主人同意之後才能關注。

I have some address from rss feed like this:

```xml
<outline text="Social / mastodon.social" title="Social / mastodon.social">
<outline text="@Gargron (Eugen Rochko)" title="@Gargron (Eugen Rochko)" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@Gargron" xmlUrl="https://openrss.org/mastodon.social/@Gargron"/>
<outline text="草莓醬🍓 :verified:" title="草莓醬🍓 :verified:" description="" type="rss" version="RSS" htmlUrl="https://m.cmx.im/@strawberry" xmlUrl="https://m.cmx.im/@strawberry.rss"/>
<outline text="層疊 - The Cascading (@cascading@misskey.io)" title="層疊 - The Cascading (@cascading@misskey.io)" description="" type="rss" version="RSS" htmlUrl="https://misskey.io/@cascading" xmlUrl="https://misskey.io/@cascading.rss"/>
<outline text="獨孤求敗" title="獨孤求敗" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@no1guangming" xmlUrl="https://o3o.ca/@no1guangming.rss"/>
<outline text="改過自新的閃啵" title="改過自新的閃啵" description="" type="rss" version="RSS" htmlUrl="https://slashine.onl/@shinybot" xmlUrl="https://slashine.onl/@shinybot.rss"/>
<outline text="國家地理每日精選" title="國家地理每日精選" description="" type="rss" version="RSS" htmlUrl="https://acg.mn/@yourshot" xmlUrl="https://acg.mn/@yourshot.rss"/>
<outline text="漢語圈聯邦宇宙" title="漢語圈聯邦宇宙" description="" type="rss" version="RSS" htmlUrl="https://mstdn.social/@fediverse" xmlUrl="https://mstdn.social/@fediverse.rss"/>
<outline text="黑客手記" title="黑客手記" description="" type="rss" version="RSS" htmlUrl="http://danielhu.software/" xmlUrl="http://danielhu.software/?feed=rss2"/>
<outline text="老兄 (@laoxong@m.moec.top)" title="老兄 (@laoxong@m.moec.top)" description="" type="rss" version="RSS" htmlUrl="https://m.moec.top/@laoxong" xmlUrl="https://m.moec.top/@laoxong.rss"/>
<outline text="盧昌海" title="盧昌海" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@Changhai" xmlUrl="https://mastodon.social/@Changhai.rss"/>
<outline text="貓貓咪咪糊糊" title="貓貓咪咪糊糊" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@BeObjectiveAlways" xmlUrl="https://o3o.ca/@BeObjectiveAlways.rss"/>
<outline text="毛茸茸生長 :trans_flag:" title="毛茸茸生長 :trans_flag:" description="" type="rss" version="RSS" htmlUrl="https://bgme.me/@bgme" xmlUrl="https://bgme.me/@bgme.rss"/>
<outline text="沒關係Bot" title="沒關係Bot" description="" type="rss" version="RSS" htmlUrl="https://toot.mantyke.icu/@dontworry" xmlUrl="https://toot.mantyke.icu/@dontworry.rss"/>
<outline text="蜜瓜級輕巡洋艦二番艦@五月病 :ff14_kaihua:" title="蜜瓜級輕巡洋艦二番艦@五月病 :ff14_kaihua:" description="" type="rss" version="RSS" htmlUrl="https://douban.city/@everpcpc" xmlUrl="https://douban.city/@everpcpc.rss"/>
<outline text="三聯生活週刊（鏡像）" title="三聯生活週刊（鏡像）" description="" type="rss" version="RSS" htmlUrl="https://pullopen.xyz/@lifeweek" xmlUrl="https://pullopen.xyz/@lifeweek.rss"/>
<outline text="獸獸 :verify: 🔞" title="獸獸 :verify: 🔞" description="" type="rss" version="RSS" htmlUrl="https://acg.mn/@Showfom" xmlUrl="https://acg.mn/@Showfom.rss"/>
<outline text="王小美" title="王小美" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@mashiro" xmlUrl="https://hello.2heng.xin/@mashiro.rss"/>
<outline text="西卡卡 :vip7: :verified_neko:" title="西卡卡 :vip7: :verified_neko:" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@jess" xmlUrl="https://o3o.ca/@jess.rss"/>
<outline text="小鳥文學" title="小鳥文學" description="" type="rss" version="RSS" htmlUrl="https://m.cmx.im/@aves" xmlUrl="https://m.cmx.im/@aves.rss"/>
<outline text="小衆軟件" title="小衆軟件" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@appinn" xmlUrl="https://mastodon.social/@appinn.rss"/>
<outline text="雲五" title="雲五" description="" type="rss" version="RSS" htmlUrl="https://go5.dev/@yun5s" xmlUrl="https://go5.dev/@yun5s.rss"/>
<outline text="雜食型蓑白（賽里斯地區的形態）" title="雜食型蓑白（賽里斯地區的形態）" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@hiromst" xmlUrl="https://mastodon.social/@hiromst.rss"/>
<outline text="長毛象導航" title="長毛象導航" description="" type="rss" version="RSS" htmlUrl="https://mstdn.one/@list" xmlUrl="https://mstdn.one/@list.rss"/>
<outline text="中文毛象宇宙觀察" title="中文毛象宇宙觀察" description="" type="rss" version="RSS" htmlUrl="https://social.datalabour.com/@mastdonbot" xmlUrl="https://social.datalabour.com/@mastdonbot.rss"/>
<outline text="alan w. smith :ablobfoxbongo:" title="alan w. smith :ablobfoxbongo:" description="" type="rss" version="RSS" htmlUrl="https://hachyderm.io/@TheIdOfAlan" xmlUrl="https://hachyderm.io/@TheIdOfAlan.rss"/>
<outline text="Animoe" title="Animoe" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@rsv" xmlUrl="https://hello.2heng.xin/@rsv.rss"/>
<outline text="Aqua" title="Aqua" description="" type="rss" version="RSS" htmlUrl="https://mstdn.moe/@aqua" xmlUrl="https://mstdn.moe/@aqua.rss"/>
<outline text="CodePen.IO :verify:" title="CodePen.IO :verify:" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@CodePen" xmlUrl="https://hello.2heng.xin/@CodePen.rss"/>
<outline text="Command Line Magic" title="Command Line Magic" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@climagic" xmlUrl="https://mastodon.social/@climagic.rss"/>
<outline text="CUF 校長室 (@admin@social.edu.ci)" title="CUF 校長室 (@admin@social.edu.ci)" description="" type="rss" version="RSS" htmlUrl="https://social.edu.ci/@admin" xmlUrl="https://social.edu.ci/@admin.rss"/>
<outline text="𝕕𝕚𝕞𝕝𝕒𝕦" title="𝕕𝕚𝕞𝕝𝕒𝕦" description="" type="rss" version="RSS" htmlUrl="https://tzcafe.com/@dimlau" xmlUrl="https://tzcafe.com/@dimlau.rss"/>
<outline text="Eugen Rochko" title="Eugen Rochko" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@Gargron" xmlUrl="https://mastodon.social/@Gargron.rss"/>
<outline text="Everyday One Cat" title="Everyday One Cat" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@eveonecat" xmlUrl="https://hello.2heng.xin/@eveonecat.rss"/>
<outline text="feeeed" title="feeeed" description="" type="rss" version="RSS" htmlUrl="https://indieapps.space/@feeeed" xmlUrl="https://indieapps.space/@feeeed.rss"/>
<outline text="Genius🌟小乖 side B" title="Genius🌟小乖 side B" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@wattlebird" xmlUrl="https://mastodon.social/@wattlebird.rss"/>
<outline text="georgianachow" title="georgianachow" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@georgianachow" xmlUrl="https://o3o.ca/@georgianachow.rss"/>
<outline text="GitHub" title="GitHub" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@github" xmlUrl="https://hello.2heng.xin/@github.rss"/>
<outline text="GoodLinks" title="GoodLinks" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@goodlinks" xmlUrl="https://mastodon.social/@goodlinks.rss"/>
<outline text="Hailong" title="Hailong" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@haohailong" xmlUrl="https://mastodon.social/@haohailong.rss"/>
<outline text="Hanchin Hsieh (@yuchanns@dvd.chat)" title="Hanchin Hsieh (@yuchanns@dvd.chat)" description="" type="rss" version="RSS" htmlUrl="https://dvd.chat/@yuchanns" xmlUrl="https://dvd.chat/@yuchanns.rss"/>
<outline text="Leeing" title="Leeing" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@Leeing" xmlUrl="https://mastodon.social/@Leeing.rss"/>
<outline text="Mariotaku" title="Mariotaku" description="" type="rss" version="RSS" htmlUrl="https://m.cmx.im/@mariotaku" xmlUrl="https://m.cmx.im/@mariotaku.rss"/>
<outline text="Mastodon" title="Mastodon" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@Mastodon" xmlUrl="https://mastodon.social/@Mastodon.rss"/>
<outline text="Mat" title="Mat" description="" type="rss" version="RSS" htmlUrl="https://wandering.shop/@matmoore" xmlUrl="https://wandering.shop/@matmoore.rss"/>
<outline text="Medium" title="Medium" description="" type="rss" version="RSS" htmlUrl="https://me.dm/@medium" xmlUrl="https://me.dm/@medium.rss"/>
<outline text="nedis (@nedis@nya.one)" title="nedis (@nedis@nya.one)" description="" type="rss" version="RSS" htmlUrl="https://nya.one/@nedis" xmlUrl="https://nya.one/@nedis.rss"/>
<outline text="NeoDB 聯邦宇宙書影音播客遊戲標註平臺🔖" title="NeoDB 聯邦宇宙書影音播客遊戲標註平臺🔖" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@neodb" xmlUrl="https://mastodon.social/@neodb.rss"/>
<outline text="Nine-Lie" title="Nine-Lie" description="" type="rss" version="RSS" htmlUrl="https://nine-lie.com/" xmlUrl="https://nine-lie.com/feed/"/>
<outline text="O3O.Foundation" title="O3O.Foundation" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@o3o_bulletin" xmlUrl="https://o3o.ca/@o3o_bulletin.rss"/>
<outline text="OldPanda" title="OldPanda" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@oldpanda" xmlUrl="https://mastodon.social/@oldpanda.rss"/>
<outline text="Open Science ✅" title="Open Science ✅" description="" type="rss" version="RSS" htmlUrl="https://mastodon.social/@openscience" xmlUrl="https://mastodon.social/@openscience.rss"/>
<outline text="Paul Graham" title="Paul Graham" description="" type="rss" version="RSS" htmlUrl="https://mas.to/@paulg" xmlUrl="https://mas.to/@paulg.rss"/>
<outline text="ruanyf" title="ruanyf" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@ruanyf" xmlUrl="https://hello.2heng.xin/@ruanyf.rss"/>
<outline text="Salt :saltamoto001:" title="Salt :saltamoto001:" description="" type="rss" version="RSS" htmlUrl="https://o3o.ca/@salt" xmlUrl="https://o3o.ca/@salt.rss"/>
<outline text="Su • 最後一代 🏴‍☠️" title="Su • 最後一代 🏴‍☠️" description="" type="rss" version="RSS" htmlUrl="https://mastodon.0ne.day/@su" xmlUrl="https://mastodon.0ne.day/@su.rss"/>
<outline text="Visual Studio Code :verify:" title="Visual Studio Code :verify:" description="" type="rss" version="RSS" htmlUrl="https://hello.2heng.xin/@code" xmlUrl="https://hello.2heng.xin/@code.rss"/>
<outline text="walfie" title="walfie" description="" type="rss" version="RSS" htmlUrl="https://kirakiratter.com/@walfie" xmlUrl="https://kirakiratter.com/@walfie.rss"/>
<outline text="Wikimedia Foundation" title="Wikimedia Foundation" description="" type="rss" version="RSS" htmlUrl="https://wikimedia.social/@wikimediafoundation" xmlUrl="https://wikimedia.social/@wikimediafoundation.rss"/>
<outline text="Xidorn Quan" title="Xidorn Quan" description="" type="rss" version="RSS" htmlUrl="https://pawoo.net/@upsuper" xmlUrl="https://pawoo.net/@upsuper.rss"/>
<outline text="Year Progress" title="Year Progress" description="" type="rss" version="RSS" htmlUrl="https://techhub.social/@year_progress" xmlUrl="https://techhub.social/@year_progress.rss"/>
<outline text="zeocy" title="zeocy" description="" type="rss" version="RSS" htmlUrl="https://m.cmx.im/@zeocy" xmlUrl="https://m.cmx.im/@zeocy.rss"/>
```

Then I use regex to replace it with `.*htmlUrl="(.*?)" xmlUrl=.*`:

```shell
https://mastodon.social/@Gargron
https://m.cmx.im/@strawberry
https://misskey.io/@cascading
https://o3o.ca/@no1guangming
https://slashine.onl/@shinybot
https://acg.mn/@yourshot
https://mstdn.social/@fediverse
http://danielhu.software/
https://m.moec.top/@laoxong
https://mastodon.social/@Changhai
https://o3o.ca/@BeObjectiveAlways
https://bgme.me/@bgme
https://toot.mantyke.icu/@dontworry
https://douban.city/@everpcpc
https://pullopen.xyz/@lifeweek
https://acg.mn/@Showfom
https://hello.2heng.xin/@mashiro
https://o3o.ca/@jess
https://m.cmx.im/@aves
https://mastodon.social/@appinn
https://go5.dev/@yun5s
https://mastodon.social/@hiromst
https://mstdn.one/@list
https://social.datalabour.com/@mastdonbot
https://hachyderm.io/@TheIdOfAlan
https://hello.2heng.xin/@rsv
https://mstdn.moe/@aqua
https://hello.2heng.xin/@CodePen
https://mastodon.social/@climagic
https://social.edu.ci/@admin
https://tzcafe.com/@dimlau
https://mastodon.social/@Gargron
https://hello.2heng.xin/@eveonecat
https://indieapps.space/@feeeed
https://mastodon.social/@wattlebird
https://o3o.ca/@georgianachow
https://hello.2heng.xin/@github
https://mastodon.social/@goodlinks
https://mastodon.social/@haohailong
https://dvd.chat/@yuchanns
https://mastodon.social/@Leeing
https://m.cmx.im/@mariotaku
https://mastodon.social/@Mastodon
https://wandering.shop/@matmoore
https://me.dm/@medium
https://nya.one/@nedis
https://mastodon.social/@neodb
https://nine-lie.com/
https://o3o.ca/@o3o_bulletin
https://mastodon.social/@oldpanda
https://mastodon.social/@openscience
https://mas.to/@paulg
https://hello.2heng.xin/@ruanyf
https://o3o.ca/@salt
https://mastodon.0ne.day/@su
https://hello.2heng.xin/@code
https://kirakiratter.com/@walfie
https://wikimedia.social/@wikimediafoundation
https://pawoo.net/@upsuper
https://techhub.social/@year_progress
https://m.cmx.im/@zeocy
```

Then you could use `https://(.*)/@(.*)\n` to format again:

```
Gargron@mastodon.social,true,false,
strawberry@m.cmx.im,true,false,
cascading@misskey.io,true,false,
no1guangming@o3o.ca,true,false,
shinybot@slashine.onl,true,false,
yourshot@acg.mn,true,false,
fediverse@mstdn.social,true,false,
laoxong@m.moec.top,true,false,
Changhai@mastodon.social,true,false,
BeObjectiveAlways@o3o.ca,true,false,
bgme@bgme.me,true,false,
dontworry@toot.mantyke.icu,true,false,
everpcpc@douban.city,true,false,
lifeweek@pullopen.xyz,true,false,
Showfom@acg.mn,true,false,
mashiro@hello.2heng.xin,true,false,
jess@o3o.ca,true,false,
aves@m.cmx.im,true,false,
appinn@mastodon.social,true,false,
yun5s@go5.dev,true,false,
hiromst@mastodon.social,true,false,
list@mstdn.one,true,false,
mastdonbot@social.datalabour.com,true,false,
TheIdOfAlan@hachyderm.io,true,false,
rsv@hello.2heng.xin,true,false,
aqua@mstdn.moe,true,false,
CodePen@hello.2heng.xin,true,false,
climagic@mastodon.social,true,false,
admin@social.edu.ci,true,false,
dimlau@tzcafe.com,true,false,
Gargron@mastodon.social,true,false,
eveonecat@hello.2heng.xin,true,false,
feeeed@indieapps.space,true,false,
wattlebird@mastodon.social,true,false,
georgianachow@o3o.ca,true,false,
github@hello.2heng.xin,true,false,
goodlinks@mastodon.social,true,false,
haohailong@mastodon.social,true,false,
yuchanns@dvd.chat,true,false,
Leeing@mastodon.social,true,false,
mariotaku@m.cmx.im,true,false,
Mastodon@mastodon.social,true,false,
matmoore@wandering.shop,true,false,
medium@me.dm,true,false,
nedis@nya.one,true,false,
neodb@mastodon.social,true,false,
o3o_bulletin@o3o.ca,true,false,
oldpanda@mastodon.social,true,false,
openscience@mastodon.social,true,false,
paulg@mas.to,true,false,
ruanyf@hello.2heng.xin,true,false,
salt@o3o.ca,true,false,
su@mastodon.0ne.day,true,false,
code@hello.2heng.xin,true,false,
walfie@kirakiratter.com,true,false,
wikimediafoundation@wikimedia.social,true,false,
upsuper@pawoo.net,true,false,
year_progress@techhub.social,true,false,
zeocy@m.cmx.im,true,false,
```

Congratulations, you get the import csv files. Just add the following head, so you could import it.

```
Account address,Show boosts,Notify on new posts,Languages
```

## Script using third SDK with official API #gtd/wait

難點：有點麻煩，不想搞

## Userscripts to jump specific site #gtd/wait

難點：無法知道這個站點是不是 Mastodon，按鈕顯示是個問題

## References

1. https://mguhlin.org/2022/11/09/tootorial-importing-followinglist-members-for-mastodon/
2. https://github.com/seanthegeek/mastodon-lists

Source via: https://note.bgzo.cc/
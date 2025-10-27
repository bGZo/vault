---
aliases:
  - Ximalaya Voice Download
  - ximalaya-download
created: 2025-04-04T16:38:20
deadline: 2025-04-04T16:38:20
modified: 2025-07-02T21:35:40
title: Ximalaya Voice Download
type: project
tags:
  - gtd/doing
---

# Ximalaya Voice Download

## Why

承诺了一年更新，但是道长常常放鸽子，一年会变成一年半，说实话有点难熬，因为常常会有人直接微信找到我。

## How

### 获得播客列表更新

地址如：

```shell
https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=80989111&pageNum=1&pageSize=30
```

获得内容：

```json
{  
  "ret": 200,  
  "data": {  
    "currentUid": 504634873,  
    "albumId": 80989111,  
    "trackTotalCount": 102,  
    "sort": 1,  
    "tracks": [  
      {  
        "index": 102,  
        "trackId": 830328394,  
        "isPaid": true,  
        "tag": 0,  
        "title": "58. 为什么缅甸政府罕见接受援助？",  
        "playCount": 16583,  
        "showLikeBtn": true,  
        "isLike": false,  
        "showShareBtn": true,  
        "showCommentBtn": true,  
        "showForwardBtn": false,  
        "createDateFormat": "1天前",  
        "url": "/sound/830328394",  
        "duration": 5734,  
        "isVideo": false,  
        "isVipFirst": false,  
        "breakSecond": 0,  
        "length": 5734,  
        "albumId": 80989111,  
        "albumTitle": "八分半",  
        "albumCoverPath": "storages/56cf-audiofreehighqps/92/7C/GKwRIRwJ2bIrAAtMawK-AecT.jpeg",  
        "anchorId": 327331799,  
        "anchorName": "梁文道",  
        "ximiVipFreeType": 0,  
        "joinXimi": false  
      }],  
    "pageNum": 1,  
    "pageSize": 30,  
    "superior": [],  
    "lastPlayTrackId": 823490447  
  }  
}
```

请求单集接口：

```shell
https://www.ximalaya.com/mobile-playpage/track/v3/baseInfo/1743755436814?device=www2&trackId=830328394&trackQualityLevel=1
```

返回的具体信息是：

```json
{
  "ret": 0,
  "extendInfo": {
    "isDownHimalayaApp": false,
    "currentPositionFrom": 0,
    "pageStyle": "old",
    "currentUid": 504634873,
    "interval": 10679706136
  },
  "trackInfo": {
    "trackId": 830328394,
    "title": "58. 为什么缅甸政府罕见接受援助？",
    "type": 0,
    "categoryId": 1002,
    "intro": "【东京鸽友会】开办提醒 本周日（4月6日）就是我们东京鸽友会的日子了，再次提醒各位朋友提前安排好您的旅行行程。 鸽友会的举办时间是东京当地时间，即2025年4月6日 14:00-16:00（东京时间）。记得调整好时差&amp;闹钟。 届时入场凭电子票二维码及节目订阅页面核验。请大家提前准备好电子票二维码（报名平台或收到的短信信息内可找到）。 临时无法参加的鸽友，麻烦去报名平台取消一下报名（进入“活动行”可自行取消），以便我们统计活动人数（活动场地位置有限，切勿空降，感谢理解）。 再次感谢鸽友们的支持和理解。如有任何问题，欢迎随时联系我们。期待这个春天相见。     收听提示 1、愚人节有哪些经典的恶搞？ 2、缅甸7.9级地震有多严重？ 3、为什么缅甸政府罕见接受援助？ 4、回应一些听友留言。  本集相关 缅甸突发地震 3月28日，缅甸发生7.9级地震，震中距曼德勒市约17.2公里。初次地震发生后约12分钟，该地区再次发生6.4级余震。地震已致数千人死伤。此次地震波及范围广泛，中国境内多地震感明显。   夏绿蒂现象  指的是耳石没有退化而具有超导体磁性，一旦有地震，就会感应电磁波预测地震的传说。 此现象由美国俄勒冈州的夏绿蒂·金所发现，该女子发现自己在七...",
    "headSkip": 0,
    "tailSkip": 0,
    "paidType": 0,
    "processState": 2,
    "createdAt": 1743595200000,
    "coverSmall": "http://imagev2.xmcdn.com/storages/56cf-audiofreehighqps/92/7C/GKwRIRwJ2bIrAAtMawK-AecT.jpeg!op_type=3&columns=100&rows=100",
    "coverMiddle": "http://imagev2.xmcdn.com/storages/56cf-audiofreehighqps/92/7C/GKwRIRwJ2bIrAAtMawK-AecT.jpeg!op_type=3&columns=180&rows=180",
    "coverLarge": "http://imagev2.xmcdn.com/storages/56cf-audiofreehighqps/92/7C/GKwRIRwJ2bIrAAtMawK-AecT.jpeg!op_type=3&columns=1000&rows=1000",
    "videoCover": "",
    "uid": 327331799,
    "nickname": "梁文道",
    "isLike": false,
    "isPublic": true,
    "likes": 64,
    "comments": 64,
    "shares": 19,
    "userSource": 1,
    "status": 1,
    "duration": 5734,
    "sampleDuration": 0,
    "isPaid": true,
    "isFree": false,
    "isAuthorized": true,
    "authorizedType": 0,
    "isVipFree": false,
    "isVideo": false,
    "isDraft": false,
    "isRichAudio": false,
    "isAntiLeech": true,
    "vipFirstStatus": 0,
    "ximiFirstStatus": 0,
    "hqNeedVip": true,
    "permissionSource": "201",
    "playUrlList": [
      {
        "huaweiSound": false,
        "type": "M4A_64",
        "fileSize": 34953925,
        "sampleSize": 1625179,
        "url": "u2dBYKx3ACOhex4YYR4uJsML27C9siqZmzAARDHjc1ogi9MxkkDAvqEtUtf0xIhlbRuPqHI308XAghWZR-0tCbqd5jFTzCYj6zNSCFC4NlC6Ds0AIZ9BKQiLeUq9PGIfKxMdESjyPlkqdJ7dDncYYGhENSEM3C2S6jUwDPpd2FkHMDMVv_JeYhAUHvaCsfTlF3WqqfiEyAwxXQzUweirzwNnFNpTFzJiKkbzFd6xjQEaRDUhqMa3cPbVGO3Xv6F0rZfTwf3MjZGfUSAVYEB2r7eHEIgzovAATj-LJt26pA",
        "qualityLevel": 1,
        "uploadId": 33177732590,
        "width": 0,
        "height": 0,
        "version": 1
      },
      {
        "huaweiSound": false,
        "type": "MP3_64",
        "fileSize": 45878587,
        "sampleSize": 1440331,
        "url": "nmH1XmuUlgKhex4YYa5ujqYKdizKgoH9mzAARDE9Var_HPkmzA4yK6EtUtf0QCvW8oYlVi_bkRHAgljxjc4IZ-IVWiZSwPQCs2JS10i7IpDiJfEGsn1bO43BeTjv5Dj6Q1aAzRbUdqG-Rp7dDssCWbVEh-1pJmLoJnZYCyYT3hweCM8-k-8ct44tuzUc4kzWd-iIhtb2_qkxXQzUwSGUScRh-6VSZcBBKkbzFd4DP8dpwg82adXr4_bVGO3XtIiXHpT5DufAGBmfUSAVYMTHqLyOS0vc_-MATj-LJt5nPA",
        "qualityLevel": 1,
        "uploadId": 33177732590,
        "width": 0,
        "height": 0,
        "version": 1
      },
      {
        "huaweiSound": false,
        "type": "M4A_24",
        "fileSize": 17748904,
        "sampleSize": 1085086,
        "url": "3fclOwFtEHehex4YYR4e-QgvyNolunGImzAARDHjeY0Bs_q9r07Ro6EtUtf0xLLsKDf1l2xklzHAgiYT5DYs2z4_Fb2LX_d39cRSdt24fGk-K3fQGKF6GPqWeQGlYeNFnMyDbAWffuAqdJ7dDncaW5dr--Ux88ExLiY-CxU7eduCPz5CCBeRgFsU8yaviaO3R1Jz6un_HBwxXQzUwehEnQ_3WLCL8uYaKkbzFd6xB7mqOVkOKB1Y3fbVGO3X7VbVZ4r6NpRfKzqfUSAVYEDgD2ADKPo9Ys8ATj-LJt1TKA",
        "qualityLevel": 0,
        "uploadId": 33177732590,
        "width": 0,
        "height": 0,
        "version": 1
      },
      {
        "huaweiSound": false,
        "type": "MP3_32",
        "fileSize": 22939420,
        "sampleSize": 720292,
        "url": "VC2gk2gz1Gihex4YYa7_bhIgJxJXal_6mzAARDE9ddsJ5stf3Me_4qEtUtf0QJgZoedy7qASk93Ago0720TFjX65bV8dkdBo9RRSKN27Emh-vqVZ--BOwRUoeTL62_oTObjZLSJakrG-Rp7dDss6tu67NmqJfsaUWCgmdT4TE3Z0QSLDd1rhkCt0HfTBujfrtldTt9i3uAAxXQzUwSEn9pUtmMQdRlbyKkbzFd4DgCtRaV0C4tiQMfbVGO3X4Qwu_lrLV7WRvcSfUSAVYMTGz3OgvwURzN4ATj-LJt4NJg",
        "qualityLevel": 0,
        "uploadId": 33177732590,
        "width": 0,
        "height": 0,
        "version": 1
      }
    ],
    "childAlbumInWhiteList": false,
    "isEnjoying": false,
    "offlineVisibleType": 0,
    "permissionExpireTime": 253402271999000,
    "hasShqAuthorized": false,
    "isXimiUhqTrack": false,
    "isXimiUhqAuthorized": false,
    "visibleCrowdType": 0,
    "playtimes": 16596
  },
  "albumInfo": {
    "albumId": 80989111,
    "title": "八分半",
    "coverLarge": "http://imagev2.xmcdn.com/storages/56cf-audiofreehighqps/92/7C/GKwRIRwJ2bIrAAtMawK-AecT.jpeg!op_type=3&columns=290&rows=290&magick=png",
    "saleScope": 0,
    "ageLevel": 1,
    "freeListenStatus": 0,
    "albumType": 0,
    "status": 1,
    "offlineType": 0,
    "isPaid": true,
    "isPodcastAlbum": false,
    "isAutoBuy": false
  },
  "version": 0,
  "hasAlbumRealFinished": false
}
```

实际的播放地址是：

```shell
https://audiopay.cos.tx.xmcdn.com/download/1.0.0/storages/568c-audiopay/2F/7E/GKwRINsHU_BLABBvTwHS2vzW-aacv2-48K.m4a?sign=cdc12894ea6fecba04b0875559bfa74a&buy_key=FM&timestamp=1743755152731000&token=6774&duration=132
```

没看懂是怎么算出来这个地址的

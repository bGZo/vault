---
created: 2025-04-04T23:33:28
modified: 2025-04-10T20:24:10
---

## 入手原因
### iOS Android 双持

### 家人守护

### 相机拍摄
## 担忧

### 屏幕品控

一加 12 的屏幕品次真是仅次于小米 11 烧 CPU 的大问题： https://www.coolapk.com/feed/63671089?shareKey=ZDRiZThlNzdlOTJiNjdlZTMwOTY~&shareUid=2988517&shareFrom=com.coolapk.app_15.2

### 碎屏险只保两年

![300](https://raw.githack.com/bGZo/assets/dev/2025/1000000280_origin_Screenshot_2025-04-09-14-34-54-96.jpg)

## Magisk ROOT

<iframe src='https://player.bilibili.com/player.html?isOutside=true&bvid=BV19Bf5YJEDD&p=1&autoplay=false' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://www.bilibili.com/video/BV19Bf5YJEDD' target='_blank' class='external-link'>https://www.bilibili.com/video/BV19Bf5YJEDD</a></center>

首先解锁：

```shell
adb reboot bootloader
fastboot flashing unlock
```

去大侠阿木， https://yun.daxiaamu.com/OnePlus_Roms/ ， 下载全量包，因为源站不再提供直链下载，你会得到一个百度网盘的链接。

下载对应版本的全量包，然后随便找个提取器，提取器提取 `boot.img`， 如 https://github.com/ssut/payload-dumper-go

拿到对应的 `boot.img`，去 `Magisk` 修复引导文件，然后进入 `bootloader` 重新刷入引导，你就成功拿到了用户级别的 ROOT。

```
# 检测是否存在已连接的设备  
fastboot devices
# 刷入  
fastboot flash boot [magisk_patched-xxx.img 文件路径]  
# 终端输出 Finished 表示成功  
# 重启  
fastboot reboot
```

> [!NOTE]
> 在刷机的过程中，我这边多次出现了进 fastboot 后不识别设备，输入命令然后就进入了等待模式，显示 `<Waiting for Device>`，我的解决办法就是多试一试，

或者你可以去 https://magiskcn.com/pixel-boot.html 拿到别人打好的包

## 应用安装
### ADB 无线调试

开发者模式打开无线调试

```shell
adb connect 192.168.46.1:5555
```

重新连接

```shell
adb kill-server
```

## References

- 一加未来可能全面降级： https://www.coolapk.com/feed/63756148?shareKey=NjY2YmNkZmY1NWI4NjdlZDQxNzI~&shareUid=2988517&shareFrom=com.coolapk.app_15.2
- https://oplus.icu/

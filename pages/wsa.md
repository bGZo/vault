---
draft: true
aliases:
  - Windows Subsystem for Android
  - Wsa
  - WSA
created: 2023-05-20T00:00:00
modified: 2025-07-16T21:16:24
tags:
  - android
  - samsung-dex
  - Windows
title: WSA
---
# WSA

## Why

Run android app on [[windows|Windows]]

## How

  > [!note]
  > The most of issues here is about [[adb]] problem.

### How to use [[proxy]]

```shell
adb connect 127.0.0.1:58526 && adb shell "settings put global http_proxy ``ip route list match 0 table all scope global | cut -F3``:7890"
```

- https://github.com/WSA-Community/WSAGAScript/issues/131
- [Windows Android 子系统 WSA 代理设置方法教程 — 秋风于渭水 (tjsky.net)](https://www.tjsky.net/tutorial/391)
- [Android device: set Wifi Proxy with ADB command | by Andres Sandoval | Medium](https://andresand.medium.com/android-device-set-wifi-proxy-with-adb-command-7a2f8cf4c434)
- [Win11 安卓子系统VirtWifi无法访问网络_virtwifi已连接,但无法访问互联网_被闲置的鱼的博客-CSDN博客](https://blog.csdn.net/qq_14902731/article/details/124891739)

### How to Push Files

```shell
adb connect 127.0.0.1:58526
adb install application.apk
adb push file_path /storage/emulated/0/Download
```

via: [How to use adb command to push a file on device without sd card](https://stackoverflow.com/questions/20834241/how-to-use-adb-command-to-push-a-file-on-device-without-sd-card)

### How to install apk

```shell
.\adb install-multiple ..\Snipd_2.2.24\base.apk ..\Snipd_2.2.24\split_config.arm64_v8a.apk ..\Snipd_2.2.24\split_config.en.apk ..\Snipd_2.2.24\split_config.ja.apk ..\Snipd_2.2.24\split_config.xxhdpi.apk ..\Snipd_2.2.24\split_config.zh.apk
```

via: [How to install xapk, apks, or multiple-apks via adb?](https://android.stackexchange.com/questions/221204/how-to-install-xapk-apks-or-multiple-apks-via-adb)

### Install Failed

```shell
adb shell settings put global verifier_verify_adb_installs 0
adb shell settings put global package_verifier_enable 0
```

via: [APK installation failed: [INSTALL_FAILED_VERIFICATION_FAILURE]](https://stackoverflow.com/questions/15014519/apk-installation-failed-install-failed-verification-failure)

## What

### Alternatives for GPlay/Sudo Root care

- [[MustardChef-WSABuilds|WSABuilds]]

### Applications I used on WSA

- https://weread.qq.com
- [[mihonapp-mihon|mihon]]

## References

- [在 Windows 上运行 Andriod 应用：WSA 安装说明 - sysin](https://sysin.org/blog/wsa-install/)

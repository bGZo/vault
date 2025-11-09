---
draft: true
aliases:
  - React Native vs Flutter
created: 2024-08-15T00:00:00
modified: 2025-08-31T10:54:31
tags:
  - facebook/react-native
  - flutter
title: React Native vs Flutter
---
# React Native vs [[flutter|Flutter]]

## Reference

> React Native 和 Flutter 的思路很不一样。
> React Native 秉承 React + web 的理念，使用 React + JavaScript 运行时借助各平台原生组件呈现视图。
> React Native 的优势是：可以轻松使用系统原生视图、获得原生级的用户体验和动画流畅度，使用 js ，能够轻松热更新；
> React Native 的缺点是：在各个平台呈现的视图不一致；
> Flutter 使用自己的绘图引擎，在各个平台上自绘视图，运行机制更接近游戏引擎。
> Flutter 的优势是能够自制复杂的视图控，；在所有平台上获得一致的视图；
> Flutter 的缺点是：Flutter 的绘图引擎（ Skia 、Impeller ）比不过原生的动画流畅性和交互体验，这方面有太多的 issues 了：动画反馈会延迟 1~3 帧，无法使用 Android 12 的滚动回弹动画，滑动和翻页时有明显的掉帧，严重的着色器编译时卡顿 ( https://docs.flutter.dev/perf/shader ) ；难以在 Flutter 视图内嵌入原生组件
> 另外近些年前端的开发理念一直比较领先，React 虽然稍微落后 vue3 、solidjs 、qwik ，但比起 Flutter 还是领先一个大版本的。Flutter 使用嵌套地狱写视图，React 有 jsx ； React 状态管理的 zustand 、jotai 、valti 一个比一个简单易用，Flutter 连 hook 都没有。
> 对于不需要复杂的绘图操作的 APP ，也就是普通 新闻、聊天 APP 的话，应该首选 RN + expo ；如果你要开发具有复杂视图的 APP ，比如游戏、谷歌地球、高德地图、Wonderous ，应该首选 Flutter 。
> 具体到楼主的 记账 APP ，肯定首先 React Native 。
> 建议体验一下 V2EX 的 Flutter 客户端和 React Native 客户端，Flutter 版本滑动、翻页的时候存在明显卡顿，RN 的体验明显好得多。
> https://github.com/guozhigq/flutter_v2ex
> https://github.com/liaoliao666/v2ex
> https://www.v2ex.com/t/1065065

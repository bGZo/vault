---
aliases:
  - "# 调研"
  - "## 调研"
  - 项目
  - Telegram Index bot
created: 2023-06-23T12:00:00
modified: 2025-08-17T18:16:46
tags:
  - gtd/todo
title: Telegram Index bot
type: project
---

# Telegram Index bot

any undertaking, carried out individually or collaboratively and possibly involving research or design, that is carefully planned to achieve a particular goal.

## Why

Telegram 频道消息是用数字命名的，所以只要知道最新一条消息的 ID1，以及上次消息的 ID2，两者 ID2-ID1 就是这段时间更新的消息，只需要将消息输出到聊天窗口，利用 Preview 功能即可实现 All in One 的设计。

而这个问题去年就有人提出了：

<iframe src='https://stackoverflow.com/questions/75516182/how-to-get-last-message-id-from-telegram-channel' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://stackoverflow.com/questions/75516182/how-to-get-last-message-id-from-telegram-channel' target='_blank' class='external-link'>https://stackoverflow.com/questions/75516182/how-to-get-last-message-id-from-telegram-channel</a></center>

实际上，以目前机器人有的 API，除非添加机器人为管理员，否则无法自由访问频道信息。

- https://core.telegram.org/bots/api
- https://core.telegram.org/bots/api#message
- https://core.telegram.org/bots/samples
- https://core.telegram.org/bots/tutorial
- https://telegram.org/tour/channels

## 覆盖范围

<iframe src='https://github.com/bGZo/playground/blob/2025/08/telegram-index-bot-python/config/channels.yaml' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://github.com/bGZo/playground/blob/2025/08/telegram-index-bot-python/config/channels.yaml' target='_blank' class='external-link'>https://github.com/bGZo/playground/blob/2025/08/telegram-index-bot-python/config/channels.yaml</a></center>


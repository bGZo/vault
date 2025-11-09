---
draft: true
created: 2023-06-25
description: 提交和管理用户的需要周期性执行的任务 | Job scheduler on Unix-like operating systems | 定期运行的作业
type: command/linux
wikipedia: https://en.wikipedia.org/wiki/Cron
---
<iframe src='https://wangchujiang.com/linux-command/c/crontab.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/crontab.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/crontab.html</a></center>


### [Cron - ArchWiki](https://wiki.archlinux.org/title/cron)
- base system uses [systemd/Timers](https://wiki.archlinux.org/title/Systemd/Timers) instead by default.
```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │             7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * <command to execute>
```
```shell
crontab -l
# 显示你的作业
crontab -e
# 编辑已有的 Cron 作业
# 设定编辑器 EDITOR=nano crontab -e
```
- Cases
    - 每 12 小时运行来自 `/Users/flavio/test.sh` 的脚本
```shell
* */12 * * * /Users/flavio/test.sh >/dev/null 2>&1
```

## Reference
- [crontab (opengroup.org)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07)
- [Crontab Generator - Generate crontab syntax](https://crontab-generator.org/)
- [Crontab.guru - The cron schedule expression editor](https://crontab.guru/)
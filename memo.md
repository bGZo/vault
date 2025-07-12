---
created: 2025-06-03T22:13:00
modified: 2025-06-22T11:25:49
---

## Sync with [[telegram-message-sync-bot|telegram-message-sync-bot]]

```shell
rsync -avz --progress --delete bgzo@192.168.31.20:/home/bgzo/workspaces/telegram-message-sync/archives/channel/ "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/clippers/telegram/"
```

```shell
rsync -avz --progress --delete bgzo@192.168.31.20:/home/bgzo/workspaces/telegram-message-sync/archives/person/ "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/clippers/telegram/person/"
```

### Mini PC

```shell
rsync -avz --progress --delete bgzo@192.168.31.238:"/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/clippers/telegram/person/" /home/bgzo/workspaces/telegram-message-sync/archives/person/
```

## Push Vault

```shell
cd clippers && git push origin main && cd - && git push origin main && cd .obsidian && git push origin main && cd -
```
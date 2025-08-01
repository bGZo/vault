---
aliases: [How to activate jetbrains, How to install develop environment]
created: 2024-12-08T09:26:21
modified: 2025-07-01T21:23:13
title: How to install develop environment
---

# How to install develop environment

## Environment

### [C++](cpp.md)

```shell
# Windows
scoop install mingw
# Linux
scoop install gcc
```

Directly download via:

- https://www.mingw-w64.org
- (windows) https://winlibs.com

### [Java](java.md)

Manage with [Home \| SDKMAN! the Software Development Kit Manager](https://sdkman.io)

```shell
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# install specific version
sdk install java 21.0.2-open
```

### [NodeJS](nodejs) Using NVM

Manage with https://github.com/nvm-sh/nvm

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# install specific version
nvm install --lts
```

Go https://nodejs.org/en/download to get the specific version you want and download / install it.

### [Python](python.md)

### [Golang](golang.md)

```shell
# macos
brew install go
# windows
scoop install go
```

Download portable version via: https://go.dev/dl/

### [Ruby](ruby)

on ubuntu:

Running following[^ruby]

```shell
sudo apt-get install ruby-full build-essential zlib1g-dev
```

Configure and source `.bashrc`:

```shell
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
```

Windows need install MSYS2, so not recommand

Mac please use [[rvm-rvm|rvm]], running following:

```shell
curl -sSL https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer | bash -s stable
source ~/.rvm/scripts/rvm
rvm install ruby@latest
```

## [[jetbrains|Jetbrains]]

### Activate using `ja-netfilter`

Go https://3.jetbra.in download the `ja-netfilter.zip`.

Unzip file to the specific location. Append the following config to `config-jetbrains/url.conf` if on China:

```shell
# https://zhile.io/2024/09/05/jetbrains-2024-2-region.html
[URL]
PREFIX,https://account.jetbrains.com.cn/lservice/rpc/validateKey.action
```

Run `script/install.sh` on unix, or `install-current-user.vbs` on windows.[^core-jetbra]

Copy code and paste on IDE. Enjoy!

[^ruby]:via: https://jekyllrb.com/docs/installation/ubuntu, https://jekyllrb.com/docs/installation/other-linux/, https://jekyllrb.com/docs/installation/ubuntu/
[^core-jetbra]: 在环境变量中添加 JAR，启动的时候加载破解补丁 via: https://www.exception.site/essay/idea-reset-eval

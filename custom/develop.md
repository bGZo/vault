---
created: 2024-12-08T09:26:21
created-link: "[[20241208]]"
modified: 2025-01-06T09:58:29
---

## Environment

### [[java]]

Manage with [Home \| SDKMAN! the Software Development Kit Manager](https://sdkman.io)

```shell
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

#### install specific version

```shell
sdk install java 21.0.2-open
```

#### manually

### [[nodejs]] using NVM

Manage with [GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions](https://github.com/nvm-sh/nvm)

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

```shell
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

#### install specific version

```
nvm install --lts
```

#### manually

### [[python]]

### [[golang]]

```shell
#macos
brew install go
#windows
scoop install go
```

Download portable version via: https://go.dev/dl/

### [[ruby]]

[Installing Ruby](https://www.ruby-lang.org/en/documentation/installation/#installers)

#### jekyll

- https://jekyllrb.com/docs/installation/other-linux/
- https://jekyllrb.com/docs/installation/ubuntu/

## Jetbrains

### Activated using `ja-netfilter`

Go https://3.jetbra.in download the `ja-netfilter.zip`.

Unzip file to the specific location. Append the following config if on China:

```shell
# https://zhile.io/2024/09/05/jetbrains-2024-2-region.html
[URL]
PREFIX,https://account.jetbrains.com.cn/lservice/rpc/validateKey.action
```

 Run `script/install.sh` on unix, or `install-current-user.vbs` on windows.

Copy code and paste on IDE. Enjoy!

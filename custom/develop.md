---
created: 2024-12-08T09:26:21
created-link: "[[20241208]]"
modified: 2024-12-22T02:20:19
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

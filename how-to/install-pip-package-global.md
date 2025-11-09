---
draft: false
aliases:
  - How to install pip package
  - How to install pip package globally
  - Install-pip-package-global
created: 2025-07-26T22:52:33
modified: 2025-07-26T22:56:41
title: How to install pip package
---
# How to install pip package

## [[pypa-pipx|Pipx]]

如果你用 Homebrew / Python >= 3.11 / pip >= 23.0，在全局安装 PIP 包，会遇到如下错误：

```shell
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

可以用 PIPX 实现全局安装并且对环境依赖无污染

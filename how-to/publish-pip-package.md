---
aliases:
  - How to publish pip package
  - Publish-pip-package
created: 2025-07-26T23:07:16
modified: 2025-07-26T23:15:32
title: How to publish pip package
---

# How to publish pip package

## [[python-poetry-poetry|poetry]]

Firstly, register an account via: https://pypi.org

Then get **account publish token** in account setting, and config it:

```shell
poetry config pypi-token.pypi <your-token>
```

Then you could publish it.

```shell
poetry publish --build
```

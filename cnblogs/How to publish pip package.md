
## poetry

Firstly, register an account via: https://pypi.org

Then get **account publish token** in account setting, and config it:

```shell
poetry config pypi-token.pypi <your-token>
```

Then you could publish it.

```shell
poetry publish --build
```

Source via: https://note.bgzo.cc/how-to/publish-pip-package
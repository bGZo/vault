---
created: 2023-07-28T12:00:00
created-link: "[[20230728]]"
description: 版本管理
document: 
status: tool/star
tags: 
type: tool
modified: 2025-01-11T04:01:04
---

## Alternatives

1. https://learnxinyminutes.com/docs/zh-cn/git-cn/
2. https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

## Config

### [[ssh]]: username & email & key

```shell
git config --global user.name 'HX'
git config --global user.email 'im@bgzo.cc'
ssh-keygen -t rsa -C 'im@bgzo.cc'

# Check connect to github
ssh -Tv git@github.com

# Paste following to github setting
cat ~/.ssh/id_rsa.pub
```

### Case sensitive

```shell
git config core.ignorecase false
```

via: https://juejin.cn/post/7135422871735631902

## Commit
### Init

```shell
git init
```

### Clone

```shell
git clone ssh://user@domain.com/repo.git
git clone -b main --single-branch ssh://user@domain.com/repo.git
```

### Status

```shell
git status
git diff # Changes to tracked files
```

### Add

```shell
git add .
```

### Commit

```shell
git commit
git commit -m "feat(xxx): xxx"
```

> [!NOTE] 3 种 Git 规范
> 1. `Add / Fix / ....` 首选动词，并且首字母大写，尽量简洁描述自己的内容，比较简陋；
> 2. `fix: xxx / feat: xxx / docs: xxx` 每次都需要选一个类似这样的 tag 打上去，方便后面检索；
> 3. `:tada: xxx / :books: xxx / bug: xxx` 利用 Github 实现的 Emoji 作为 tag，类似 2，并且可以在 Github 上显示更好？
>
> via: https://stackoverflow.com/questions/9742073/graphics-in-github-commit-messages

### History

```shell
git log
git log --oneline
git blame <file>
```

### Push & Pull

```shell
git pull <remote> <branch>
git push <remote> <branch>

git remote -v # List all currently configured remotes
git remote show <remote> # Show information about a remote
git remote add <shortname> <url> # Add new remote repository, named <remote>
# git submodule add <url>/<ssh>
git fetch <remote> # Download all changes from <remote>

git branch -dr <remote/branch> # Delete a branch on the remote
git push --tags # Publish your tags
```

`git fetch` + `git merge` == `git pull` via https://www.jianshu.com/p/a5c4d2f99807

![](https://raw.githack.com/bGZo/assets/dev/2024/image_1645371143990_0-or8.png)

```bash
git fetch origin master
git log -p master..origin/master
git merge origin/master
git fetch origin master:tmp
git diff tmp
git merge tmp
# via: https://blog.csdn.net/hudashi/article/details/7664457
```

## Rollback

> [!warning]
> 不要用 `git reset --hard (versionＨash)`, 修改会清空!

### add

```shell
git reset --mixed
# 保留修改, 退出暂存区, --mixed 为默认参数
git reset HEAD
# 撤销 add (绿字变红字)
git checkout -- (file)
# 撤销没 add 的修改 (红字变无)
```

### commit

```shell
git reset --soft HEAD^
# 不删除工作空间改动代码, 撤销 commit, 不撤销 git add
git commit --amend
# commit 注释写错了, 只想改一下注释
```

### `--hard`

恢复到了上一次的 commit 状态，删除工作空间改动代码，撤销 `commit`，撤销 `git add .`

### all things

```
git reflog
```

## Merge

### [[jetbrains]] gui tools

外部程序直接可以调用 IDEA 的 Git Merge 工具；

```shell
[diff]
	guitool = intellij
[difftool "intellij"]
	path = C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2023.3.2/bin/idea.bat
	cmd = \"C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2023.3.2/bin/idea.bat\" diff \"$LOCAL\" \"$REMOTE\"
[merge]
	guitool = intellij
[mergetool "intellij"]
	path = C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2023.3.2/bin/idea.bat
	cmd = \"C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2023.3.2/bin/idea.bat\" merge \"$LOCAL\" \"$REMOTE\" \"$BASE\" \"$MERGED\"
```

via: https://stackoverflow.com/questions/72018546/git-mergetool-with-intellij-ideas-community-edition-on-windows

> [!NOTE] 并非银弹
> via: https://www.xttblog.com/?p=5294
Untracked Files Prevent Checkout* Move or commit them before checkout

### command-line

```bash
git merge <branch>
git rebase <branch>
git rebase --abort
git rebase --continue
git mergetool
git add <resolved-file>
git rm <resolved-file>
```

`rebase` check https://juejin.cn/post/7038093620628422669

### Force reset merge other branch

```shell
git reset --hard dev/1197
```

via: https://stackoverflow.com/a/59238409

## Submodules

```shell
git submodule add https://github.com/yyy/xxx.git
git submodule status
git submodule deinit
git clone https://github.com/yyy/xxx.git --recursive #子模块也一起 clone, or using for
git submodule init && git submodule update # euqal following
git submodule update --init
git submodule update --init --recursive # 递归添加
```

via: https://knightyun.github.io/2021/03/21/git-submodule

## Brach

```shell
git branch -av
git checkout <branch> # Switch HEAD branch
git branch <new-branch> # Create a new branch based
git checkout --track <remote/branch> #Create a new tracking branch based on a remote branch
git branch -d <branch> # Delete a local branch
```

## Tag

```shell
git tag <tag-name>

git log 								# list all tags
git tag -l "v1.8.5*" 					# list with regex

git tag -a v1.4 -m "my version 1.4" 	# annotated 附注标签

git push origin v1.5 					# push sepecific
git push origin --tags			 	# push all
```

`tag`: 每一个正式发布的版本 merge 到 master 并且打一个 tag

用例：利用打 tag 自动部署一次应用

via: https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%89%93%E6%A0%87%E7%AD%BE

## History remove

Install https://github.com/newren/git-filter-repo

```shell
pip3 install --trusted-host pypi.tuna.tsinghua.edu.cn -i https://pypi.tuna.tsinghua.edu.cn/simple filter-repo
```

Remove folder

```shell
git filter-repo --path pdf --invert-paths
```

Remove file

```shell
git filter-repo --path readme.md --invert-paths --force
```

Force Push

```shell
git remote add "origin" git@github.com:xxx/xxx.git
git push origin dev --force
```

## Notes

### `revert` vs `checkout` vs `reset`

`revert` -> `commit level`, no `file level`

__safe operation__ for 'public undos' as it creates new history which can be shared remotely and doesn't overwrite history remote team members may be dependent on.

`checkout` -> `commit level` & `file level`

A checkout is an operation that moves the HEAD ref pointer to a specified commit

`reset`

A reset is an operation that __takes a specified commit and resets the "three trees" to match the state of the repository at that specified commit__.

`three trees` -> `working directory` & `stagged snapshot` & `commit History`

`three different modes`??

`checkout` and `reset` are generally used for making local or private 'undos'. They modify the history of a repository that can cause conflicts when pushing to remote shared repositories.

```bash
git reset --hard HEAD
git checkout HEAD <file> # Discard local changes in a specific file
git revert <commit> # Revert a commit   (by producing a new commit with contrary changes)
git reset --hard <commit> # Reset your HEAD pointer to a previous commit …and discard all changes since then
git reset <commit> # and preserve all changes as unstaged changes
git reset --keep <commit> # and preserve uncommitted local changes
```

via: https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting

### remote add origin vs remote set-url origin

below is used to add a new remote:

```bash
git remote add "origin" git@github.com:User/UserRepo.git
```

below is used to change the url of an existing remote repository:

```bash
git remote set-url "origin" git@github.com:User/UserRepo.git
```

below will push your code to the master branch of the remote repository defined with `"origin"` and `-u` let you point your current local branch to the remote master branch:

```bash
git push -u origin main
```

**[Documentation](https://git-scm.com/docs/git-remote)**
https://stackoverflow.com/questions/42830557/git-remote-add-origin-vs-remote-set-url-origin

## Emojis supported by [[pages/github]] [^github-emoji-refer]

| Commit type                | Emoji                                            |
| -------------------------- | ------------------------------------------------ |
| Initial commit             | 🎉 `:tada:`                                      |
| Version tag                | 🔖 `:bookmark:`                                  |
| New feature                | ✨ `:sparkles:`                                   |
| Bugfix                     | 🐛 `:bug:`                                       |
| Metadata                   | 📇 `:card_index:`                                |
| Documentation              | 📚 `:books:`                                     |
| Documenting source code    | 💡 `:bulb:`                                      |
| Performance                | 🐎 `:racehorse:`                                 |
| Cosmetic                   | 💄 `:lipstick:`                                  |
| Tests                      | 🚨 `:rotating_light:`                            |
| Adding a test              | ✅ `:white_check_mark:`                           |
| Make a test pass           | ✔️ `:heavy_check_mark:`                          |
| General update             | ⚡ `:zap:`                                        |
| Improve format/structure   | 🎨 `:art:`                                       |
| Refactor code              | 🔨 `:hammer:`                                    |
| Removing code/files        | 🔥 `:fire:`                                      |
| Continuous Integration     | 💚 `:green_heart:`                               |
| Security                   | 🔒 `:lock:`                                      |
| Upgrading dependencies     | ⬆️ `:arrow_up:`                                  |
| Downgrading dependencies   | ⬇️ `:arrow_down:`                                |
| Lint                       | 👕 `:shirt:`                                     |
| Translation                | 👽 `:alien:`                                     |
| Text                       | 📝 `:pencil:`                                    |
| Critical hotfix            | 🚑 `:ambulance:`                                 |
| Deploying stuff            | 🚀 `:rocket:`                                    |
| Fixing on MacOS            | 🍎 `:apple:`                                     |
| Fixing on Linux            | 🐧 `:penguin:`                                   |
| Fixing on Windows          | 🏁 `:checkered_flag:`                            |
| Work in progress           | 🚧 `:construction:`                              |
| Adding CI build system     | 👷 `:construction_worker:`                       |
| Analytics or tracking code | 📈 `:chart_with_upwards_trend:`                  |
| Removing a dependency      | ➖ `:heavy_minus_sign:`                           |
| Adding a dependency        | ➕ `:heavy_plus_sign:`                            |
| Docker                     | 🐳 `:whale:`                                     |
| Configuration files        | 🔧 `:wrench:`                                    |
| Package.json in JS         | 📦 `:package:`                                   |
| Merging branches           | 🔀 `:twisted_rightwards_arrows:`                 |
| Bad code / need improv.    | 💩 `:hankey:`                                    |
| Reverting changes          | ⏪ `:rewind:`                                     |
| Breaking changes           | 💥 `:boom:`                                      |
| Code review changes        | 👌 `:ok_hand:`                                   |
| Accessibility              | ♿ `:wheelchair:`                                 |
| Move/rename repository     | 🚚 `:truck:`                                     |
| Other                      | [Be creative](http://www.emoji-cheat-sheet.com/) |

## Links

![[git-cheatsheet.pdf]]

1. https://github.com/liangzr/github-run
2. https://github.com/sallar/github-contributions-canvas

[^github-emoji-refer]:https://gist.github.com/parmentf/035de27d6ed1dce0b36a, https://github.com/dannyfritz/commit-message-emoj, https://gitmoji.carloscuesta.me

---
draft: true
created: 2024-08-11
description: global regular expression print | 全局正则表达式打印 | 强大的文本搜索工具
type: command/linux
---
<iframe src='https://wangchujiang.com/linux-command/c/grep.html' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://wangchujiang.com/linux-command/c/grep.html' target='_blank' class='external-link'>https://wangchujiang.com/linux-command/c/grep.html</a></center>


## Reference

```shell
less index.md | grep -n document.getElementById
```
- Parms
```
-F, --fixed-strings
        将模式 PATTERN 视为一个固定的字符串的列表，用新行 (newlines) 分隔，只要匹配其中之一即可。
-f FILE, --file=FILE
        从文件 FILE 中获取模式，每行一个。空文件含有0个模式，因此不匹配任何东西。
-n, --line-number
        在输出的每行前面加上它所在的文件中它的行号。
-q, --quiet, --silent
        安静。不向标准输出写任何东西。如果找到任何匹配的内容就立即以状态值  0  退
        出，即使检测到了错误。 参见 -s 或 --no-messages 选项。
-R, -r, --recursive
        递归地读每一目录下的所有文件。这样做和 -d recurse 选项等价。
-s, --no-messages
        禁止输出关于文件不存在或不可读的错误信息。 对于可移植性需要注意：与 GNU grep 不同，传统的  grep  不遵守  POSIX.2  规范，因为传统的
        grep  缺少一个  -q 选项，而它的 -s 选项与 GNU grep 的 -q 选项行为相似。需要可移植到传统 grep 的 shell 脚本应当避免使用 -q 和 -s 选
        项，而应当将输出重定向到 /dev/null 。
-i, --ignore-case
        忽略模式 PATTERN 和输入文件中的大小写的分别。 (区分大小写)
-v, --invert-match
        改变匹配的意义，只选择不匹配的行。(翻转结果, 反向排除)
```
- TLDR
```shell
# Search for a pattern within a file:
grep "search_pattern" path/to/file
# Search for an exact string (disables regular expressions):
grep --fixed-strings "exact_string" path/to/file
grep -F "exact_string" path/to/file
# Search for a pattern in all files recursively in a directory, showing line numbers of matches, ignoring binary files:
grep --recursive --line-number --binary-files=without-match "search_pattern" path/to/directory
# Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:
grep --extended-regexp --ignore-case "search_pattern" path/to/file
# Print 3 lines of context around, before, or after each match:
grep --context|before-context|after-context=3 "search_pattern" path/to/file
# Print file name and line number for each match with color output:
grep --with-filename --line-number --color=always "search_pattern" path/to/file
# Search for lines matching a pattern, printing only the matched text:
grep --only-matching "search_pattern" path/to/file
# Search stdin for lines that do not match a pattern:
cat path/to/file | grep --invert-match "search_pattern"
```

- cases
    - 告诉 grep 在相应行的前后各输出 2 行，以提供更多的上下文

```shell
grep -nC 2 document.getElementById index.md
```
- `-C`
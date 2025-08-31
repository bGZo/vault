---
aliases:
  - 正则表达式
  - Regex
created: 2024-04-21T00:00:00
modified: 2025-08-30T23:38:30
title: 正则表达式
---

# 正则表达式

## Why

## How

### Match Object [[encoding]]

Emoji

```javascript
s = s.replaceAll("\\p{So}+", "");
```

### Question

```shell
# editor envir: https://rubular.com | a ruby regular expression editor
# title: regex notes
# author: bGZoCg
b.t # b as begining, t as end
loadScript.*lua # string begining with loadScript to lua.
loadScript.*?lua # string begining with loadScript fitstly to lua.
loadScript\((.*?),(.*?)\) # double groups
loadScript($1,id,$2) # add id
# (TO_DATE.*)(\d+-[a-z]+-\d+', ')DD(-MM-YY')
# INSERT INTO EMPLOYEES VALUES( '100','Steven','King','SKING', '515.123.4567' , TO_DATE('17-JUN-87', 'DD-MM-YY'), 'AD_PRES', '24000',NULL, NULL,'90') -->
[^ ] # Character class. any character contained between the square brackets(blank space).
[^ ]* # string interval with blank space(include `\n`)
[^ ]*?@[^ ]*?\.[^ ]* # email
[\w.]+@\w+\.(com|net|edu) #email
  \w vs [^ ]*: [^ ]* include `\n`, former not.
[\u4e00-\u9fa5] # Simplied Chinese
[^\x00-\xff] # Double Bytes
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*) # url
https?:/{2}\w.+$'# url
\(?\d{3}[-.)]\d{3}[-.]\d{4} # phone number
```

```shell
[*]+# https://stackoverflow.com/questions/42058748/what-does-mean-in-regex
^(^?)*\?(.*)$ # https://stackoverflow.com/questions/15205994/what-does-mean-in-this-regex
\[(?:[^][]|(?R))*\] # https://stackoverflow.com/questions/17845014/what-does-the-regex-mean
```

向前非贪婪匹配匹配: 全模拟也可以解决

```shell
[Rubular: a Ruby regular expression editor](https://rubular.com/)
[Regex Util download | SourceForge.net](https://sourceforge.net/projects/regex-util/)
[PowerGREP: Windows grep Software to Search (and Replace) through Files and Folders on Your PC and Network](https://www.powergrep.com/)
# Solution
1. while mo ni
2. ([0-9A-z-]*)/([0-9A-z-]*) \)$
3. TODO 从后贪婪匹配
```

## [[navigation|Navigation]]

- [Rubular: a Ruby regular expression editor](https://rubular.com/)
- [Regex Tester - Javascript, PCRE, PHP](https://www.regexpal.com/)
- [Regular Expression Tester](http://myregexp.com/)
- [Regular expression tool - regex.larsolavtorvik.com](http://regex.larsolavtorvik.com/)
- [Nregex v/0.1](http://nregex.com/)
- [jflap](https://www2.cs.duke.edu/csed/jflap/)
- [Regular Expressions Quick Start](https://www.regular-expressions.info/quickstart.html)
- [Regexper](https://regexper.com/)
- [RegexBuddy: Learn, Create, Understand, Test, Use and Save Regular Expression](https://www.regexbuddy.com/)
- [Expresso Regular Expression Tool](https://ultrapico.com/Expresso.htm)
- [PowerGREP: Windows grep Software to Search (and Replace) through Files and Folders on Your PC and Network](https://www.powergrep.com/)
- [Regular-Expressions.info - Regex Tutorial, Examples and Reference - Regexp Patterns](https://www.regular-expressions.info/)
- [Regular Expression Library](https://www.regexlib.com)
- [Regex Util download | SourceForge.net](https://sourceforge.net/projects/regex-util/)

## References

- [可能是最好的正则表达式的教程笔记了吧... - 掘金](https://juejin.cn/post/6844903648309297166)
- [正则表达式_w3cschool](https://www.w3cschool.cn/regexp/)
- [开发过程最全的正则表达式匹配中英文、字母和数字_正则表达式_脚本之家](https://www.jb51.net/article/161544.htm)
- [java - What is the regex to extract all the emojis from a string? - Stack Overflow](https://stackoverflow.com/questions/24840667/what-is-the-regex-to-extract-all-the-emojis-from-a-string)

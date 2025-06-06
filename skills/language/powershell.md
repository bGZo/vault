---
aliases:  
created: 2024-08-10T00:00:00
description:
tags: shell
type: lang/programming
modified: 2025-03-22T16:37:50
---

## Why

> Because-I-Believe-PowerShell-Commands-Are-Way-Too-Long-And-Unnecessarily-Verbose-That-I-Definitely-Hate-To-Type-Any-Of-Them-For-The-Sake-Of-My-Finger-Health-And-Keyboard-Durability
> —— [PowerShell 为什么使用的人很少？ - V2EX](https://www.v2ex.com/t/876580)

## How

### ps5 vs ps7

> PS7 renamed `powershell.exe` to `pwsh.exe`
> via: https://learn.microsoft.com/en-us/powershell/scripting/whats-new/differences-from-windows-powershell?view=powershell-7.4

migrating via: https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.4#using-powershell-7-side-by-side-with-windows-powershell-51

### get **version**

```shell
echo $PSVersionTable
```

### **output** with `echo` alias of `Write-Output` (cmdlet)

> [!note]
> 大部分 `cmdlet` 和函数都遵循 " 动词 - 名词 " 命名规则

```shell
echo Hello world!
echo 'Hello world!';
```

### **click run** with bat file on windows

```shell
Powershell.exe -executionpolicy remotesigned -File  C:\Users\SE\Desktop\ps.ps1
```

via: https://stackoverflow.com/questions/19335004

### base

``` powershell
Get-ExecutionPolicy -List
Set-ExecutionPolicy AllSigned
# Execution Policy 包含以下：
# - Restricted: 不会运行脚本。
# - RemoteSigned: 只会运行受信任的发行商下载的脚本。
# - AllSigned: 运行需要被信任发行商签名的脚本。
# - Unrestricted: 运行所有脚本
help about_Execution_Policies # 查看更多信息
# 当前 PowerShell 版本
$PSVersionTable
$host             # get-host | select version
# 查找命令
Get-Command about_* # 别名: gcm
Get-Command -Verb Add
Get-Alias ps
Get-Alias -Definition Get-Process
Get-Help ps | less # 别名: help
ps | Get-Member # 别名: gm
Show-Command Get-EventLog # GUI 填充参数
Update-Help # 管理员运行
```

```powershell
# 正如你看到的，每一行开头是 # 都是注释
# 简单的 Hello World 实例
echo Hello world!
# echo 是 Write-Output (cmdlet) 的别名
# 大部分 cmdlet 和函数都遵循 "动词-名词" 命名规则。
# 每个命令都从新的一行开始或者是一个分号
echo 'This is the first line'; echo 'This is the second line'
# 声明一个变量如下：
$aString="Some string"
# 或者像这样：
$aNumber = 5 -as [double]
$aList = 1,2,3,4,5
$anEmptyList = @()
$aString = $aList -join '--' # 也包含 join 方法
$aHashtable = @{name1='val1'; name2='val2'}
# 使用变量：
echo $aString
echo "Interpolation: $aString"
echo "$aString has length of $($aString.Length)"
echo '$aString'
echo @"
This is a Here-String
$aString
"@
# 注意 ' (单引号) 不是变量的一部分
# 在这里字符串也可以是单引号
# 内置变量:
# 下面是一些有用的内置变量，比如：
echo "Booleans: $TRUE and $FALSE"
echo "Empty value: $NULL"
echo "Last program's return value: $?"
echo "Exit code of last run Windows-based program: $LastExitCode"
echo "The last token in the last line received by the session: $$"
echo "The first token: $^"
echo "Script's PID: $PID"
echo "Full path of current script directory: $PSScriptRoot"
echo 'Full path of current script: ' + $MyInvocation.MyCommand.Path
echo "FUll path of current directory: $Pwd"
echo "Bound arguments in a function, script or code block: $PSBoundParameters"
echo "Unbound arguments: $($Args -join ', ')."
# 更多的内置类型: `help about_Automatic_Variables`
# 内联其他文件 (点操作符)
. .\otherScriptName.ps1
```

### 控制流

```powershell
# 下面是条件判断结构
if ($Age -is [string]) {
    echo 'But.. $Age cannot be a string!'
} elseif ($Age -lt 12 -and $Age -gt 0) {
    echo 'Child (Less than 12. Greater than 0)'
} else {
    echo 'Adult'
}
# Switch 语句比其他语言更强大
$val = "20"
switch($val) {
  { $_ -eq 42 }           { "The answer equals 42"; break }
  '20'                    { "Exactly 20"; break }
  { $_ -like 's*' }       { "Case insensitive"; break }
  { $_ -clike 's*'}       { "clike, ceq, cne for case sensitive"; break }
  { $_ -notmatch '^.*$'}  { "Regex matching. cnotmatch, cnotlike, ..."; break }
  { 'x' -contains 'x'}    { "FALSE! -contains is for lists!"; break }
  default                 { "Others" }
}
# 经典的 For 循环
for($i = 1; $i -le 10; $i++) {
  "Loop number $i"
}
# 或者可以更简洁
1..10 | % { "Loop number $_" }
# PowerShell 还提供其他循环方式
foreach ($var in 'val1','val2','val3') { echo $var }
# while () {}
# do {} while ()
# do {} until ()
# 异常处理
try {} catch {} finally {}
try {} catch [System.NullReferenceException] {
    echo $_.Exception | Format-List -Force
}
### Providers
# 列出当前目录下的文件和子目录
ls # 或者 `dir`
cd ~ # 回到主目录
Get-Alias ls # -> Get-ChildItem
# 这些 cmdlet 有更加通用的名称，因为它不仅仅只操作当前目录，这一点和其他脚本语言不同。
cd HKCU: # 跳转 HKEY_CURRENT_USER 注册表中的值
# 获取当前会话中的提供者
Get-PSProvider
```

### Providers

```powershell
# 列出当前目录下的文件和子目录
ls # 或者 `dir`
cd ~ # 回到主目录
Get-Alias ls # -> Get-ChildItem
# 这些 cmdlet 有更加通用的名称，因为它不仅仅只操作当前目录，这一点和其他脚本语言不同。
cd HKCU: # 跳转 HKEY_CURRENT_USER 注册表中的值
# 获取当前会话中的提供者
Get-PSProvider
```

### 管道

```powershell
# Cmdlets 中的参数用来控制它们的行为：
Get-ChildItem -Filter *.txt -Name # 获取所有 txt 文件名。
# 需要输入足够多的参数来确保没有歧义。
ls -fi *.txt -n # -f 是不可以的因为 -Force 同样存在。
# 使用 `Get-Help Get-ChildItem -Full` 来查看全部参数。
# 之前 cmdlet 获取的结果输出可以作为一下个输入。
# `$_` 指代当前管道处理的对象。
ls | Where-Object { $_.Name -match 'c' } | Export-CSV export.txt
ls | ? { $_.Name -match 'c' } | ConvertTo-HTML | Out-File export.html
# 如果对管道的对象感到疑惑，使用 `Get-Member` 来查看该对象的可使用的方法和属性。
ls | Get-Member
Get-Date | gm
# ` 是行连续标识符，或者在每一行结尾添加一个 |
Get-Process | Sort-Object ID -Descending | Select-Object -First 10 Name,ID,VM `
    | Stop-Process -WhatIf
Get-EventLog Application -After (Get-Date).AddHours(-2) | Format-List
# 使用 % 作为 ForEach-Object 的简称。
(a,b,c) | ForEach-Object `
    -Begin { "Starting"; $counter = 0 } `
    -Process { "Processing $_"; $counter++ } `
    -End { "Finishing: $counter" }
# Get-Process 返回包含三列的表
# 第三列是使用 2 位精度数值表示 VM 属性
# 计算出来的列也可以表示更多的信息:
# `@{name='lbl';expression={$_}`
ps | Format-Table ID,Name,@{n='VM(MB)';e={'{0:n2}' -f ($_.VM / 1MB)}} -autoSize
```

### 函数

```powershell
### 函数
# [string] 注记是可选的。
function foo([string]$name) {
    echo "Hey $name, have a function"
}
# 调用你的函数
foo "Say my name"
# 函数可以包含命名参数、参数的注记和可解析的文档
<#
.SYNOPSIS
Setup a new website
.DESCRIPTION
Creates everything your new website needs for much win
.PARAMETER siteName
The name for the new website
.EXAMPLE
New-Website -Name FancySite -Po 5000
New-Website SiteWithDefaultPort
New-Website siteName 2000 # ERROR! Port argument could not be validated
('name1','name2') | New-Website -Verbose
#>
function New-Website() {
    [CmdletBinding()]
    param (
        [Parameter(ValueFromPipeline=$true, Mandatory=$true)]
        [Alias('name')]
        [string]$siteName,
        [ValidateSet(3000,5000,8000)]
        [int]$port = 3000
    )
    BEGIN { Write-Verbose 'Creating new website(s)' }
    PROCESS { echo "name: $siteName, port: $port" }
    END { Write-Verbose 'Website(s) created' }
}
```

### 都是 .NET

```powershell

# PS 中的字符串事实上就是 .NET 的 System.String 类型
# 所有 .NET 方法和属性都可用
'string'.ToUpper().Replace('G', 'ggg')
# 或者更加 PowerShell 一点
'string'.ToUpper() -replace 'G', 'ggg'
# 不确定这样的话 .NET 方法如何调用
'string' | gm
# 调用静态 .NET 方法的语法：
[System.Reflection.Assembly]:LoadWithPartialName('Microsoft.VisualBasic')
# 注意 .NET 方法调用必须使用括号，然而 PS 函数调用不能使用括号；
# 如果你调用 cmdlet/PS 函数使用了括号，就相当于传递了参数列表。
$writer = New-Object System.IO.StreamWriter($path, $true)
$writer.Write([Environment]:NewLine)
$writer.Dispose()
```

### IO

```powershell
### IO
# 从输入读入一个值
$Name = Read-Host "What's your name?"
echo "Hello, $Name!"
[int]$Age = Read-Host "What's your age?"
# Test-Path, Split-Path, Join-Path, Resolve-Path
# Get-Content filename # 返回字符串数组 string[]
# Set-Content, Add-Content, Clear-Content
Get-Command ConvertTo-*,ConvertFrom-*
```

### 有用的东西

```powershell
# 更新 PATH
$env:PATH = [System.Environment]:GetEnvironmentVariable("Path", "Machine") +
    ";" + [System.Environment]:GetEnvironmentVariable("Path", "User")
# 找到 Python 的 PATH
$env:PATH.Split(";") | Where-Object { $_ -like "*python*"}
# 改变工作目录而不需要记住之前的路径
Push-Location c:\temp # 改变工作目录至 c:\temp
Pop-Location # 改变到之前的工作目录
# 别名: pushd 和 popd
# 在下载之后解除目录阻塞
Get-ChildItem -Recurse | Unblock-File
# Windows 资源管理器打开当前目录
ii .
# 按任意键退出
$host.UI.RawUI.ReadKey()
return
# 创建快捷方式
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($link)
$Shortcut.TargetPath = $file
$Shortcut.WorkingDirectory = Split-Path $file
$Shortcut.Save()
# $Profile 是文件 `Microsoft.PowerShell_profile.ps1` 完整路径
# 下面所有的代码都在 PS 会话开始的时候执行
if (-not (Test-Path $Profile)) {
    New-Item -Type file -Path $Profile -Force
    notepad $Profile
}
```

### Other
#### 回显

```powershell
Set-PSDebug -Trace 1
# 0: Turn script tracing off.
# 1: Trace script lines as they run.
# 2: Trace script lines, variable assignments, function calls, and scripts.
```

via: [debugging - PowerShell "echo on" - Stack Overflow](https://stackoverflow.com/questions/2063995/powershell-echo-on)

#### Output

```powershell
write-host xxx
write(-output) xxx
# output 为管道输出, 可以进行管道搭配
```

via: [windows - PowerShell difference between Write-Host and Write-Output? - Stack Overflow](https://stackoverflow.com/questions/19754069/powershell-difference-between-write-host-and-write-output)

#### 去重

```powershell
xxx | sort -Unique
```

#### `ConvertTo-Html`: 输出的内容转换为 HTML
#### `out-file`: 重定向输出到一个文件（file）或者到打印机
#### `Get-Process/Start-Process/Stop-Process/Wait-Process`: 操作进程
#### `write-EventLog`: 写入日志
#### `Get-Alias/New-Alias/Set-Alias/Import-Alias`: 别名
## What
### Encode Problem

> [!note]
> Low version(v5) used [UTF-16LE](https://wikipedia.org/wiki/UTF-16), and only support `UTF8`(with BOM);
via: [About Character Encoding - PowerShell | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding)

Higher version(v6) could solve this issue, they support `utf8NoBOM`, and can be changed using following command:

```ps
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'
$PSDefaultParameterValues['*:Encoding'] = 'utf8'
```

> [!note]
> By the way, `chcp 65001` not works, because it not change `utf-16le` by default.

> [!tip]
> So using the `pwsh` instead of `powershell` since

- [What is the difference between [pwsh] and [Powershell Integrated Console] on VS Code? - Stack Overflow](https://stackoverflow.com/questions/60124810/what-is-the-difference-between-pwsh-and-powershell-integrated-console-on-vs)
- [shell - How to force a Powershell Script to run a specific Version - Stack Overflow](https://stackoverflow.com/questions/61720842/how-to-force-a-powershell-script-to-run-a-specific-version)
- [about Pwsh - PowerShell | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.3)

> [!tip]
> Another way is that using UTF-16LE or UTF-8 with BOM by default as well.

- [php - cURL gets response with utf-8 BOM - Stack Overflow](https://stackoverflow.com/questions/12509855/curl-gets-response-with-utf-8-bom)

## References

- [powershell、cmd终端修改编码 - xututu6 - 博客园](https://www.cnblogs.com/xututu6/p/16574454.html)
- [Using PowerShell 7 in VS Code | rnelson0](https://rnelson0.com/2020/03/05/using-powershell-7-in-vs-code/) #vscode
- [Learn X in Y Minutes: Scenic Programming Language Tours](https://learnxinyminutes.com/docs/zh-cn/powershell-cn/)

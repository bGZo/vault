---
tags:
  - operating-system
created: 2024-09-22T09:26:22
modified: 2025-01-17T11:06:14
aliases:
  - Windows
---

## Prior to purchase

### Standard
- [ ] 力度触控板  
- [ ] 键盘按键的触发力度  
- [ ] 自动亮度调节  
- [ ] 风扇（性能）控制  
- [ ] 轻 (中) 度负载的噪音  
- [ ] 电池续航  
- [ ] 性能释放  
- [ ] 镜面屏  

There is no silver bullet for computer, via [[hp-starbook]]

### Bypass connect Wi-Fi

`shift + f12` 弹出命令行后，输入

```shell
oobe\bypassnro
```

重启进入系统即可跳过联网激活

## Install

- Get Windows ISO via
    - https://www.microsoft.com/en-us/software-download/windows11
    - https://msdn.sjjzm.com
    - https://msdn.itellyou.cn
    - https://www.hellowindows.cn
- Write it on U Disk via:
    - https://github.com/pbatard/rufus

## Activate

Thanks for https://github.com/massgravel/Microsoft-Activation-Scripts

```
irm https://massgrave.dev/get | iex
```

## Package management / Software recover

> [!IMPORTANT]
> `winget` is required by following command.
> Luckily, `winget` has supported for proxy, with unstable network..[^proxy_winget] So Choose one way to use proxy:

```bash
# Set Proxy for winget
$ sudo winget settings --enable ProxyCommandLineOptions
# Temporary
$ winget --proxy http://127.0.0.1:10800 install 
# Permanent
$ winget settings set DefaultProxy https://127.0.0.1:2345
# Cancel permanent
$ winget settings reset DefaultProxy
```

### Import `scoop`

Move scoop folder under `~` and then run as `install-scoop.ps1`

```powershell
$username = $env:USERNAME
$scoopPath = "C:\Users\$username\scoop"
$currentScoop = [Environment]::GetEnvironmentVariable("SCOOP", "User")
if ($currentScoop -eq $null) {
    [Environment]::SetEnvironmentVariable("SCOOP", $scoopPath, "User")
    Write-Output "SCOOP environment variable set to $scoopPath"
} else {
    Write-Output "SCOOP environment variable already exists with value: $currentScoop"
}


$currentUserPath = [Environment]::GetEnvironmentVariable("PATH", "User")
$newPathEntry = "%SCOOP%\shims"
if (-not $currentUserPath.Contains($newPathEntry)) {
    $updatedPath = "$currentUserPath;$newPathEntry"
    [Environment]::SetEnvironmentVariable("PATH", $updatedPath, "User")
    Write-Output "Path updated: $updatedPath"
} else {
    Write-Output "Path already contains $newPathEntry"
}
```

run following command with admin permissions

```bash
$ scoop reset *
# Set Proxy for scoop, via https://github.com/ScoopInstaller/Scoop/wiki/Using-Scoop-behind-a-proxy
$ scoop config proxy 127.0.0.1:10800
```

## Components build-in
### Remove: Ads

Run as `.ps1`:

```powershell
# 设置下载的目标目录
$distDir = "dist"

# 确保 dist 目录存在
if (-not (Test-Path -Path $distDir)) {
    # New-Item -Path $distDir -ItemType Directory
    mkdir $distDir
}

if (-not $distDir) {
    Write-Host "Error: \$distDir is null or empty!"
    exit
}

$fileUrl = "https://github.com/xM4ddy/OFGB/releases/download/v0.4/OFGB-Deps.exe"
$fileName = "OFGB-Deps.exe"
$destinationPath = Join-Path -Path $distDir -ChildPath $fileName

# 确保 dist 目录存在
if (-not (Test-Path -Path $distDir)) {
    New-Item -Path $distDir -ItemType Directory
}

# 默认代理地址
$defaultProxy = "http://127.0.0.1:7890"

# 询问用户是否使用代理
$useProxy = Read-Host "是否需要使用代理下载文件? (y/n)"

# 判断是否使用代理
if ($useProxy -eq "y") {
    # 询问用户是否使用默认代理地址
    $proxyAddress = Read-Host "是否使用默认代理地址 $defaultProxy? (y/n)"
    if ($proxyAddress -eq "y") {
        $proxy = $defaultProxy
    } else {
        # 用户提供自定义代理地址
        $proxy = Read-Host "请输入自定义代理地址"
    }

    # 设置代理并下载文件
    $webClient = New-Object System.Net.WebClient
    $webClient.Proxy = New-Object System.Net.WebProxy($proxy)
    $webClient.DownloadFile($fileUrl, $destinationPath)
    Write-Host "文件已通过代理下载到 $distDir 目录"
} else {
    # 直接下载文件，不使用代理
    Invoke-WebRequest -Uri $fileUrl -OutFile $destinationPath
    Write-Host "文件已下载到 $distDir 目录"
}
```

### Remove: Packages

Run following:[^uninstall-garbage]

```bash
$ winget uninstall "windows web experience pack"
$ winget uninstall "电脑管家"
$ winget uninstall "资讯"
```

### Replace: Powershell

```shell
#Powershell 7
$ winget install --id Microsoft.PowerShell
```

### Replace: Search

[GitHub - srwi/EverythingToolbar: Everything integration for the Windows taskbar.](https://github.com/srwi/EverythingToolbar) ![https://github.com/srwi/EverythingToolbar](https://img.shields.io/github/stars/srwi/EverythingToolbar)

```shell
# EverythingToolbar 
$ winget install stnkl.EverythingToolbar
```

### Disable: Services

Run following as `disable-services.ps1`:

```powershell
$servicesToDisable = @(
  "WSearch", 
  "DtsApo4Service"
)

foreach ($service in $servicesToDisable) {
    # 获取服务状态
    $svc = Get-Service -Name $service -ErrorAction SilentlyContinue
    
    if ($null -ne $svc) {
        # 停止服务
        if ($svc.Status -ne 'Stopped') {
            Write-Host "Stopping service: $service"
            Stop-Service -Name $service -Force
        }
        
        # 设置服务启动类型为禁用
        Write-Host "Disabling service: $service"
        Set-Service -Name $service -StartupType Disabled
    } else {
        Write-Host "Service $service not found!"
    }
}
```

### Disable: Firewall

Run as `disable-firewall.ps1`

```powershell
# Before
Get-NetFirewallProfile

Set-NetFirewallProfile -Profile Domain -Enabled False
Set-NetFirewallProfile -Profile Private -Enabled False
Set-NetFirewallProfile -Profile Public -Enabled False

# After
Get-NetFirewallProfile
```

### Disable: Windows Defender

use [`dControl`](https://www.sordum.org/9480/defender-control-v2-1/), but not open-source.

### Hide: Windows Security Notifications

Run as `disable-security-notifications.reg`[^wsn]

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications]
"DisableNotifications"=dword:00000001
```

### Disable: Windows Update

TODO

### Disable: Sticky keys

TODO

## Laptop Option

### Processor performance boost mode

Run <code>process-boost.bat</code>, then go `powercfg.cpl` to disable boost it. If you are using windows 11, you could use the `EnergyStar` meanwhile.[^overheat-laptop]

```bash
$ winget install 9NF7JTB3B17P
```

### Modern Standby (S0)

Check your laptop whether support S3 sleep mode:

```bash
powercfg -a
```

If shown only support S0, run following as `kill-s0-sleep.bat` to delete sleep mode.[^windows_modern_standby]

```bat
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Power]
"PlatformAoAcOverride"=dword:00000000
```

> [!NOTE]
> If you delete sleep mode, you should select your laptop to hibernate after closing lid.

```shell
powercfg /hibernate on
```

Recovery sleep mood run following as `reg`:

```bat
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Power]
"PlatformAoAcOverride"=-
```

## SubSystem

### WSL

Install WSL

```bash
$ sudo dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
$ wsl --set-default-version 2
$ wsl --install --no-distribution
```

> [!NOTE]
> If show `无法解析服务器的名称或地址`, just set system proxy, then retry.

Then import ubuntu[^import_export_wsl]

```bash
wsl --import ubuntu "C:\Users\bgzo\wsl\" "C:\Users\bgzo\Downloads\ubuntu.tar" --version 2
```

### WSA

TODO

## Customized

### Install Runtime Dependencies

```bash
# C++
$ winget install Microsoft.VCRedist.2010.x64
$ winget install Microsoft.VCRedist.2012.x64
$ winget install Microsoft.VCRedist.2013.x64
$ winget install Microsoft.VCRedist.2015+.x64
```

### Install Font

install under user permission, stored in `~\AppData\Local\Microsoft\Windows\Fonts`

```shell
$ scoop bucket add nerd-fonts

# https://github.com/lxgw/LxgwWenKai
$ scoop install LXGWWenKai
$ scoop install LXGWWenKaiMono

# https://github.com/JetBrains/JetBrainsMono
$ scoop install JetBrainsMono-NF
```

Recommend you install following fonts:

- Ping Fang Font
- Noble Scarlet

### Coding: Case Sensitive [^case-sensitive]

```shell
# Windows
$ fsutil.exe file setCaseSensitiveInfo ~\workspaces enable
# Git
$ git config core.ignorecase false 
```

### Chinese: Flypy Support

Run as `install-flypy.reg`

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS]
"UserDefinedDoublePinyinScheme0"="flypy*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt"
```

### Chinese: Font rendering

1. ClearType build-in windows.
2. Install [Noble Scarlet](https://github.com/fernvenue/microsoft-yahei)[^auto_replace_in_chinese_windows]
3. Replace with Apple PingFang using https://github.com/Tatsu-syo/noMeiryoUI

> [!NOTE]
> In 22H2 later versions, something would be wrong. via https://github.com/Tatsu-syo/noMeiryoUI/discussions/86

4. (Not recommend, cause *outdated*) MacType

````sh
$ winget install MacType.MacType
````

5. (Not recommend, cause *side effect*) Replace Fonts

### Proxy

See [[proxy]], then go https://github.com/bGZo/proxy

### Beautify

#### Like Mac

- BitDock: http://www.bitdock.cn/bbs/forum.php

## Waiting features

### Unlock windows hello without PIN

Impossible via: https://answers.microsoft.com/en-us/windows/forum/all/option-to-setup-fingerprint-without-pin-windows/10692b78-a60a-4208-9c97-b9ec27809cea

## Reference

### Shortcuts

#### Global

|Operation|Effects|
|:--------------:|:---------------:|
|Win+E|打开资源管理器|
|Win+t|循环切换任务栏|
|Win+Ctrl+D|创建虚拟 Desktop|
|Win+Q|搜索|
|Win+Ctrl+F4|关闭虚拟 Desktop|
|Win+R|对话框|
|Win+Ctrl+ 左/右|左右切换虚拟 Desktop|
|Win+X|“Windows 移动中心”设置面板|
|Win+F4|关闭窗口|
|Win+m|最小化窗口（全部窗口）|
|Win+Shift+M|还原窗口最小化（全部）|

#### Ctrl

|    Operation    |    Effects     |
| :-------------: | :------------: |
|     ctrl+w      | 关闭浏览器当前页（我的电脑） |
|     ctrl+t      |     打开新标签页     |
| ctrl+alt+delete |    打开任务管理器     |
|  ctrl+shift+t   |   恢复关闭的浏览器页面   |
|      ctrl+      |      放大页面      |
|      ctrl-      |      缩小页面      |

#### Alt

|Operation|Effects|
|:------------------:|:-----------------:|
|alt+F4|关闭窗口|
|alt+enter|查看选中文件属性|
|alt+ 前进/后退方向键|浏览器页面后退前进|
|alt+d|焦点固定到地址栏|
|alt+shief+numLock|用键盘控制鼠标|
|alt+space+n|单个窗口最小化（配合 Dock 使用）|

#### Fn

|Operation|Effects|
|:----------:|:--------:|
|F1|显示当前程序或者 windows 的帮助内容|
|F2|如果选中文件的话，进行重命名|
|F3|查找|
|F5|浏览器页面刷新|
|F6|使用浏览器时，地址栏获得焦点（即光标移到了地址栏）|
|F11|浏览器全屏|
|F12|浏览器审查元素/调试界面|
|prtsc|截屏|

### Changelog
#### 24H2

via: https://learn.microsoft.com/en-us/windows/whats-new/whats-new-windows-11-version-24h2#features-added-to-windows-11-since-version-23h2

- Features no longer under temporary enterprise control
- Checkpoint cumulative updates
- Features exclusive to Copilot+ PCs in 24H2
- Features added to Windows 11 since version 23H2
    - Server Message Block (SMB) protocol changes
        - SMB signing and encryption
        - SMB alternative client and server ports
        - SMB NTLM blocking exception list
        - SMB dialect management
        - SMB over QUIC
        - SMB firewall rule changes
    - Local Security Authority (LSA) protection enablement on upgrade
    - Remote Mailslot protocol disabled by default
    - Local Administrator Password Solution (LAPS) improvements
    - Rust in the Windows kernel
    - Personal Data Encryption (PDE) for folders
    - Windows protected print mode
    - SHA-3 support
    - App Control for Business
    - Wi-Fi 7 support
    - Bluetooth ® LE audio support for assistive devices
    - Windows location improvements
    - Sudo for Windows
    - Enable optional updates
    - Remote Desktop Connection improvements
    - Additional features
        - **File Explorer**
            - 7-zip and TAR archives support
        - **OOBE improvement**: when you need to connect to a network and there's no Wi-Fi drivers, you're given an *Install drivers* option to install drivers that are already downloaded
        - **Registry Editor**: The Registry Editor supports limiting a search to the currently selected key and its descendants
        - **Task Manager**: The Task Manager settings page has [Mica material](https://learn.microsoft.com/en-us/windows/apps/design/style/mica) and a redesigned icon
    - Developer APIs
- Features removed in Windows 11, version 24H2
    - WordPad
    - Alljoyn

#### 23H2

via: https://learn.microsoft.com/en-us/windows/whats-new/whats-new-windows-11-version-23h2

- Features no longer under temporary enterprise control
- Features added to Windows 11 since version 22H2
    - Passkeys in Windows
    - Windows passwordless experience
    - Web sign-in for Windows
    - Declared configuration protocol
    - Education themes
    - Temporary enterprise feature control
    - Multi-app kiosk
    - Copilot in Windows
    - Windows Hello for Business authentication improvement
    - LAPS native integration
    - Federated sign-in
    - Customize Windows 11 taskbar buttons
    - Braille displays
    - Dev Drive
    - Additional features
        - In-box apps

#### 22H2

via: https://learn.microsoft.com/en-us/windows/whats-new/whats-new-windows-11-version-22h2

- Microsoft Pluton
- Enhanced Phishing Protection
- Smart App Control
- Credential Guard
- Malicious and vulnerable driver blocking
- Security hardening and threat protection
- Personal Data Encryption
- WebAuthn APIs support ECC
- Stickers for Windows 11 SE, version 22H2
- Education themes
- Windows Update notifications
- Start menu layout
- Improvements to task manager
- Windows accessibility
- High Efficiency Video Coding (HEVC) support

## Close Function
  - Close 粘滞键
    - 设置 > 粘滞键 > 关闭所有触发方式
    - https://blog.csdn.net/xitongzhijia_abc/article/details/125505930

## References
[^china-office]: https://v2ex.com/t/1048191
[^turbo-boost]: https://www.youtube.com/watch?v=iWBVtXPfTB0
- Seem like some pc support edit on the bios
    - Settings --> AMD OverClocking --> Precision Boost Overdrive
    via: https://www.reddit.com/r/AMDHelp/comments/es0d4a/how_exactly_do_you_disable_pbo/

## TODO Remote Config
  - Reg editor

## TODO 备份 .m2 目录
-

[^proxy_winget]: https://github.com/microsoft/winget-cli/issues/190, https://github.com/microsoft/winget-cli/discussions/4428
[^uninstall-garbage]: https://superuser.com/questions/1684005/how-do-i-prevent-widgets-exe-from-getting-automatically-started-on-windows-11, https://answers.microsoft.com/en-us/windows/forum/all/how-to-permanently-stop-the-widgets-service-from/de082ed2-81db-4074-a334-0c9ca13f15c4, https://v2ex.com/t/1048191
[^wsn]:https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/windows-defender-security-center/wdsc-hide-notifications
[^overheat-laptop]: https://www.youtube.com/watch?v=iWBVtXPfTB0
[^windows_modern_standby]: via https://www.chiphell.com/thread-2460017-1-1.html to check abnormal power on count with ssd disk. more instructions you could via https://www.bilibili.com/video/BV1Pv4y1d7Ms/, solution via https://blog.csdn.net/sinat_30603081/article/details/130637807, https://www.timochan.cn/posts/any_pen/stupid_modern_standby
[^import_export_wsl]: https://blog.csdn.net/momodosky/article/details/108102146
[^case-sensitive]: case-sensitive via https://juejin.cn/post/7135422871735631902, https://www.zhihu.com/question/443835000/answer/1726902348↩
[^auto_replace_in_chinese_windows]: via: https://hermit.world/post/2022/01/17/refining-windows-font-rendering/, https://www.zhihu.com/question/67196637, https://v2ex.com/t/941786

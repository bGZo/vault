---
draft: true
aliases:
  - How to run program in background
  - Run-program-in-background
created: 2025-07-19T12:08:14
modified: 2025-07-19T12:09:09
title: How to run program in background
---
# How to run program in background

## [[windows|Windows]]

```powershell
Start-Process
Start Job { & C:\Full\Path\To\my.exe }
```

```cmd
start
```

## [[skills/devops/linux/index|index]]

- `tmux`
- `nohup`
- `bg`

## References

- [What's the nohup on Windows? - Stack Overflow](https://stackoverflow.com/questions/3382082/whats-the-nohup-on-windows)
- [What is the equivalent of 'nohup' in linux PowerShell? - Stack Overflow](https://stackoverflow.com/questions/64707869/what-is-the-equivalent-of-nohup-in-linux-powershell)
- [Start-Process (Microsoft.PowerShell.Management) - PowerShell | Microsoft Learn](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process)
- [What is the equivalent of 'nohup' in PowerShell? - Stack Overflow](https://stackoverflow.com/questions/19321903/what-is-the-equivalent-of-nohup-in-powershell)
- [Start-Job (Microsoft.PowerShell.Core) - PowerShell | Microsoft Learn](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/start-job)

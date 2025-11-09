---
draft: true
aliases:
  - 串流
  - moonlight
  - sunshine
created: 2023-05-31T11:12:34
modified: 2025-03-30T16:43:28
tags:
  - area/gaming
---
## Why

- In a correct place play something
- remote control pc.

## How

### [[windows|Windows]]
#### Pro self build-in
#### RDP Host Group Policies

- Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Connections
- Select RDP Transfer Protocols = **Enabled**
    - Set Transport Type to: "Use both UDP and TCP"
- Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Remote Session Enviorment
- Use hardware graphics adapters for all Remote Desktop Services Sessions = **Enabled**
- Prioritize H.264/AVC 444 graphics mode for Remote Desktop Connections = **Enabled**
- Configure H.264/AVC Hardware encoding for Remote Desktop Connections = **Enabled**
    - Set "Prefer AVC hardware encoding" to **"Always attempt"**
- Configure compression for Remote FX data = **Enabled**
    - Set RDP compression algorithem: **"Do not use an RDP compression algorithm"**
- Configure image quality for RemoteFX Adaptive Graphics = **Enabled**
    - Set Image Quality to "**High"** (lossless seemed too brutal over WAN connections.)
- Enable RemoteFX encoding for RemoteFX clients designed for Windows Server 2008R2 SP1 = **Enabled**.
- Computer Configuration > Policies > Administrative Template > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Remote Session Enviorment > Remote FX for Windows Server 2008R2
- Configure Remote FX = **Enabled**
- Optimize visual experience when using Remote FX = **Enabled**
    - Set Screen capture rate (frames per second) = **Highest (best quality)**
        - Set Screen Image Quality = **Highest (best quality)**
- Optimize visual experience for remote desktop sessions = **Enabled**
    - Set Visual Experience = **Rich Multimedia**

via: https://www.reddit.com/r/sysadmin/comments/fv7d12/pushing_remote_fx_to_its_limits

#### 60 FPS
- `regedit.msc`
    - `计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations`
        - 新建 `DWORD (32位)` 值，命名 `DWMFRAMEINTERVAL`
        [[streaming|Sunshine]]tps[[streaming]]net/csdn_life18/article/details/108250846

### Others: [[LizardByte-Sunshine|Sunshine]] + [[moonlight-stream-moonlight-qt|moonlight-qt]]

#### 物理虚拟显示器：显卡欺骗器
### 虚拟显示器

- [ ] #gtd/wait 期待效果，开机通过 systemctl 启动 on [[minisforum-um880pro|minisforum880pro]];

<iframe src='https://github.com/loki-47-6F-64/sunshine/issues/47' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://github.com/loki-47-6F-64/sunshine/issues/47' target='_blank' class='external-link'>https://github.com/loki-47-6F-64/sunshine/issues/47</a></center>

```bash
~ > systemctl cat sunshine@root
# /usr/lib/systemd/system/sunshine@.service
# via: https://www.reddit.com/r/linux_gaming/comments/17dd245/is_there_a_way_to_have_sunshine_launchbe/ 
#      https://github.com/LizardByte/Sunshine/issues/1533
[Unit]
Description=sunshine for %i.
After=graphical.target

[Service]
Type=simple
User=%i
Restart=on-abort
Environment=DISPLAY=:0
ExecStart=/home/bgzo/opt/sunshine.AppImage

[Install]
# WantedBy=multi-user.target
WantedBy=graphical-session.target
```

### Steam Link

- https://play.google.com/store/apps/details?id=com.valvesoftware.steamlink&hl=en_SG&gl=US

## FAQ

### Sunshine 服务器忘记密码

```
sunshine --creds admin adminadmin
```

via: [sunshine串流忘了用户名/密码，重置用户名/密码 - 哔哩哔哩](https://www.bilibili.com/opus/874155389577330696)

### Moonlight Cheatsheet

- document: https://ideas.moonlight-stream.org
- source: https://github.com/moonlight-stream/moonlight-qt

### Want to use screenshot in computer. Cannot mapping in the app.

> Moonlight seems to be designed with controllers in mind (obvious since its based on Nvidia game stream). If it does help, keep this in mind, so ce this is the way Game Stream is supposed to work
> via: [On screen keyboard · Issue #330 · moonlight-stream/moonlight-android](https://github.com/moonlight-stream/moonlight-android/issues/330)

https://github.com/moonlight-stream/moonlight-docs/wiki/Frequently-Asked-Questions

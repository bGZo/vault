---
aliases:
  - Xiaohongshu Exporter
  - xiaohongshu-exporter
created: 2025-07-27T10:06:42
deadline: 2025-07-27T10:06:42
modified: 2025-07-27T10:07:42
tags:
  - gtd/doing
title: Xiaohongshu Exporter
type: project
---

# Xiaohongshu Exporter

## Why

## How

### 前辈脚本：[小红书转发 - 源代码](https://greasyfork.org/zh-CN/scripts/464664-%E5%B0%8F%E7%BA%A2%E4%B9%A6%E8%BD%AC%E5%8F%91/code)

### Tampermonkey 隐私友好

### 包含范围

#### Xiaohongshu

![](https://raw.githack.com/bGZo/assets/dev/2025/202503231337389.png)

#### Twitter

DONE

#### Bilibili

TODO

## 试错历程（xiaohongshu 为例）

### 收集笔记

问题是点击两个按钮什么事情都没有发生。

```shell
// ==UserScript==
// @name         小红书本地导出
// @namespace    https://yournamespace.com
// @version      4.3
// @description  本地化导出小红书笔记为Markdown并打包下载
// @match        https://www.xiaohongshu.com/*
// @grant        unsafeWindow
// @grant        GM_addStyle
// @grant        GM.xmlHttpRequest
// @require      https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js
// @license      MIT
// @icon         https://www.xiaohongshu.com/favicon.ico
// ==/UserScript==

(function () {
  "use strict";
  console.log('[小红书导出] 脚本开始执行');

  // 修正后的样式
  GM_addStyle(`
    .export-panel {
      position: fixed;
      top: 200px;
      right: 20px;
      background: white !important;
      color: #333 !important;
      border: 1px solid #eee;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      z-index: 99999;
      width: 300px;
    }
    .export-btn {
      background: #056b00 !important;
      color: white !important;
      border: none;
      padding: 8px 15px;
      border-radius: 4px;
      cursor: pointer;
      margin: 5px;
    }
  `);

  let capturedNotes = [];
  let zip = new JSZip();

  // 创建导出面板
  function createExportPanel() {
    const panel = document.createElement('div');
    panel.className = 'export-panel';
    panel.innerHTML = `
      <h3>已捕获笔记：<span id="noteCount">0</span></h3>
      <button class="export-btn" id="exportMd">导出Markdown</button>
      <button class="export-btn" id="exportZip">打包下载</button>
    `;
    document.body.appendChild(panel);
  }

  function updateNoteCount() {
    document.getElementById('noteCount').textContent = capturedNotes.length;
  }

  // 新版接口处理逻辑
  function interceptRequests() {
    const originalOpen = XMLHttpRequest.prototype.open;
    const collectPattern = /\/api\/sns\/web\/v2\/note\/collect\/page/;
    const feedPattern = /\/api\/sns\/web\/v1\/feed/;

    const originalResponseText = Object.getOwnPropertyDescriptor(
      XMLHttpRequest.prototype,
      "responseText"
    );

    XMLHttpRequest.prototype.open = function (method, url) {
      originalOpen.apply(this, arguments);

      const xhr = this;
      const handleResponse = (response) => {
        try {
          const data = JSON.parse(response);
          console.log('[接口响应]', data);

          // 处理收藏接口
          if (collectPattern.test(url)) {
            console.log('[处理收藏接口]', data.data?.notes);
            data.data?.notes?.forEach(note => {
              const processed = processCollectNote(note);
              if (processed) {
                capturedNotes.push(processed);
                updateNoteCount();
              }
            });
          }
          // 处理动态流接口
          else if (feedPattern.test(url)) {
            console.log('[处理动态流接口]', data.data?.items);
            data.data?.items?.forEach(item => {
              if (item.note) {
                const processed = processNote(item.note);
                capturedNotes.push(processed);
                updateNoteCount();
              }
            });
          }
        } catch (e) {
          console.error('响应处理失败:', e);
        }
      };

      if (originalResponseText?.get) {
        Object.defineProperty(xhr, "responseText", {
          get: function () {
            const response = originalResponseText.get.call(this);
            if (collectPattern.test(url) || feedPattern.test(url)) {
              handleResponse(response);
            }
            return response;
          },
          configurable: true
        });
      }
    };
  }

  // 处理收藏接口的笔记结构
  function processCollectNote(rawNote) {
    try {
      return {
        id: rawNote.note_id,
        title: rawNote.display_title || '无标题',
        desc: '',
        time: Date.now(),
        user: {
          nickname: rawNote.user?.nickname || '匿名用户',
          userId: rawNote.user?.user_id || '未知用户'
        },
        images: [{
          url: rawNote.cover?.url_default || '',
          name: ''
        }],
        video: rawNote.type === 'video' ? {
          url: `https://sns-video-bd.xhscdn.com/${rawNote.video?.consumer?.originVideoKey}`,
          name: ''
        } : null
      };
    } catch (e) {
      console.error('收藏笔记处理失败:', e);
      return null;
    }
  }

  // 处理动态流笔记结构
  function processNote(rawNote) {
    return {
      id: rawNote.id,
      title: rawNote.title || '无标题',
      desc: rawNote.desc || '无描述',
      time: rawNote.time || Date.now(),
      user: {
        nickname: rawNote.user?.nickname || '匿名用户',
        userId: rawNote.user?.userId || '未知用户'
      },
      images: rawNote.imageList?.map(img => ({
        url: img.urlDefault || '',
        name: ''
      })) || [],
      video: rawNote.video ? {
        url: `https://sns-video-bd.xhscdn.com/${rawNote.video.consumer.originVideoKey}`,
        name: ''
      } : null
    };
  }

  // 生成Markdown
  function generateMarkdown(note) {
    return `# ${note.title}\n\n` +
      `**作者**: ${note.user.nickname} (ID: ${note.user.userId})\n\n` +
      `${note.desc}\n\n` +
      `${note.images.map(img => `![图片](${img.name})`).join('\n')}\n` +
      `${note.video ? `\n[视频](${note.video.name})` : ''}`;
  }

  // 初始化
  function init() {
    createExportPanel();
    interceptRequests();

    document.getElementById('exportMd').addEventListener('click', async () => {
      for (const note of capturedNotes) {
        const folder = zip.folder(note.id);

        // 下载图片
        for (const [index, img] of note.images.entries()) {
          if (img.url) {
            try {
              const response = await GM.xmlHttpRequest({
                method: "GET",
                url: img.url,
                responseType: "blob"
              });
              folder.file(`image_${index+1}.jpg`, response.response);
              img.name = `image_${index+1}.jpg`;
            } catch (error) {
              console.error('图片下载失败:', error);
            }
          }
        }

        // 下载视频
        if (note.video?.url) {
          try {
            const response = await GM.xmlHttpRequest({
              method: "GET",
              url: note.video.url,
              responseType: "blob"
            });
            folder.file(`video.mp4`, response.response);
            note.video.name = `video.mp4`;
          } catch (error) {
            console.error('视频下载失败:', error);
          }
        }

        folder.file('note.md', generateMarkdown(note));
      }
    });

    document.getElementById('exportZip').addEventListener('click', () => {
      zip.generateAsync({type:"blob"}).then(content => {
        saveAs(content, "xhs-notes.zip");
      });
    });
  }

  init();
})();

```

### 调整了监听器添加逻辑，调整了下载 Header

仍然没有用

```shell
// ==UserScript==
// @name         小红书本地导出
// @namespace    https://yournamespace.com
// @version      4.3
// @description  本地化导出小红书笔记为Markdown并打包下载
// @match        https://www.xiaohongshu.com/*
// @grant        unsafeWindow
// @grant        GM_addStyle
// @grant        GM.xmlHttpRequest
// @require      https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js
// @license      MIT
// @icon         https://www.xiaohongshu.com/favicon.ico
// ==/UserScript==

(function () {
  "use strict";
  console.log('[小红书导出] 脚本开始执行');


  // 调试标记
  let isGenerating = false;

  // 初始化检查
  console.log('JSZip可用性:', typeof JSZip !== 'undefined' ? '✅' : '❌');
  console.log('FileSaver可用性:', typeof saveAs !== 'undefined' ? '✅' : '❌');

  // 修正后的样式
  GM_addStyle(`
    .export-panel {
      position: fixed;
      top: 200px;
      right: 20px;
      background: white !important;
      color: #333 !important;
      border: 1px solid #eee;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      z-index: 99999;
      width: 300px;
    }
    .export-btn {
      background: #056b00 !important;
      color: white !important;
      border: none;
      padding: 8px 15px;
      border-radius: 4px;
      cursor: pointer;
      margin: 5px;
    }
  `);

  let capturedNotes = [];
  let zip = new JSZip();

  // 创建导出面板
  function createExportPanel() {
    const panel = document.createElement('div');
    panel.className = 'export-panel';
    panel.innerHTML = `
      <h3>已捕获笔记：<span id="noteCount">0</span></h3>
      <button class="export-btn" id="exportMd">导出Markdown</button>
      <button class="export-btn" id="exportZip">打包下载</button>
    `;
    document.body.appendChild(panel);


    // 添加事件监听（修复版）
    setTimeout(() => {
      document.getElementById('exportMd').addEventListener('click', handleExportMd);
      document.getElementById('exportZip').addEventListener('click', handleExportZip);
      console.log('按钮事件监听器已绑定');
    }, 1000);

  }

  function updateNoteCount() {
    document.getElementById('noteCount').textContent = capturedNotes.length;
  }

  // 新版接口处理逻辑
  function interceptRequests() {
    const originalOpen = XMLHttpRequest.prototype.open;
    const collectPattern = /\/api\/sns\/web\/v2\/note\/collect\/page/;
    const feedPattern = /\/api\/sns\/web\/v1\/feed/;

    const originalResponseText = Object.getOwnPropertyDescriptor(
      XMLHttpRequest.prototype,
      "responseText"
    );

    XMLHttpRequest.prototype.open = function (method, url) {
      originalOpen.apply(this, arguments);

      const xhr = this;
      const handleResponse = (response) => {
        try {
          const data = JSON.parse(response);
          console.log('[接口响应]', data);

          // 处理收藏接口
          if (collectPattern.test(url)) {
            console.log('[处理收藏接口]', data.data?.notes);
            data.data?.notes?.forEach(note => {
              const processed = processCollectNote(note);
              if (processed) {
                capturedNotes.push(processed);
                updateNoteCount();
              }
            });
          }
          // 处理动态流接口
          else if (feedPattern.test(url)) {
            console.log('[处理动态流接口]', data.data?.items);
            data.data?.items?.forEach(item => {
              if (item.note) {
                const processed = processNote(item.note);
                capturedNotes.push(processed);
                updateNoteCount();
              }
            });
          }
        } catch (e) {
          console.error('响应处理失败:', e);
        }
      };

      if (originalResponseText?.get) {
        Object.defineProperty(xhr, "responseText", {
          get: function () {
            const response = originalResponseText.get.call(this);
            if (collectPattern.test(url) || feedPattern.test(url)) {
              handleResponse(response);
            }
            return response;
          },
          configurable: true
        });
      }
    };
  }

  // 处理收藏接口的笔记结构
  function processCollectNote(rawNote) {
    try {
      return {
        id: rawNote.note_id,
        title: rawNote.display_title || '无标题',
        desc: '',
        time: Date.now(),
        user: {
          nickname: rawNote.user?.nickname || '匿名用户',
          userId: rawNote.user?.user_id || '未知用户'
        },
        images: [{
          url: rawNote.cover?.url_default || '',
          name: ''
        }],
        video: rawNote.type === 'video' ? {
          url: `https://sns-video-bd.xhscdn.com/${rawNote.video?.consumer?.originVideoKey}`,
          name: ''
        } : null
      };
    } catch (e) {
      console.error('收藏笔记处理失败:', e);
      return null;
    }
  }

  // 处理动态流笔记结构
  function processNote(rawNote) {
    return {
      id: rawNote.id,
      title: rawNote.title || '无标题',
      desc: rawNote.desc || '无描述',
      time: rawNote.time || Date.now(),
      user: {
        nickname: rawNote.user?.nickname || '匿名用户',
        userId: rawNote.user?.userId || '未知用户'
      },
      images: rawNote.imageList?.map(img => ({
        url: img.urlDefault || '',
        name: ''
      })) || [],
      video: rawNote.video ? {
        url: `https://sns-video-bd.xhscdn.com/${rawNote.video.consumer.originVideoKey}`,
        name: ''
      } : null
    };
  }

  // 生成Markdown
  function generateMarkdown(note) {
    const artile = `# ${note.title}\n\n` +
      `**作者**: ${note.user.nickname} (ID: ${note.user.userId})\n\n` +
      `${note.desc}\n\n` +
      `${note.images.map(img => `![图片](${img.name})`).join('\n')}\n` +
      `${note.video ? `\n[视频](${note.video.name})` : ''}`;
      console.log("按模板导出笔记：" + artile)
    return artile
  }

  // 初始化
  function init() {
    createExportPanel();
    interceptRequests();

    // document.getElementById('exportMd').addEventListener('click', async () => {
    //   console.log("检测到点击导出 Markdown");
    //   for (const note of capturedNotes) {
    //     const folder = zip.folder(note.id);

        // 下载图片
        // for (const [index, img] of note.images.entries()) {
        //   if (img.url) {
        //     try {
        //       const response = await GM.xmlHttpRequest({
        //         method: "GET",
        //         url: img.url,
        //         responseType: "blob"
        //       });
        //       folder.file(`image_${index+1}.jpg`, response.response);
        //       img.name = `image_${index+1}.jpg`;
        //     } catch (error) {
        //       console.error('图片下载失败:', error);
        //     }
        //   }
        // }

        // 下载视频
        // if (note.video?.url) {
        //   try {
        //     const response = await GM.xmlHttpRequest({
        //       method: "GET",
        //       url: note.video.url,
        //       responseType: "blob"
        //     });
        //     folder.file(`video.mp4`, response.response);
        //     note.video.name = `video.mp4`;
        //   } catch (error) {
        //     console.error('视频下载失败:', error);
        //   }
        // }

    //     folder.file('note.md', generateMarkdown(note));
    //   }
    // });

    // document.getElementById('exportZip').addEventListener('click', () => {
    //   console.log("检测到点击导出 ZIP");
    //   zip.generateAsync({type:"blob"}).then(content => {
    //     saveAs(content, "xhs-notes.zip");
    //   });
    // });
  }



  async function handleExportMd() {
    console.log('开始导出Markdown');
    if (capturedNotes.length === 0) {
      return alert('请先浏览内容确保捕获到笔记');
    }

    try {
      for (const note of capturedNotes) {
        const folder = zip.folder(note.id);
        // 添加媒体文件下载逻辑
        // await processMedia(note, folder);
        // 生成Markdown文件
        folder.file('note.md', generateMarkdown(note));
      }
      alert('Markdown准备完成，请点击打包下载');
    } catch (error) {
      console.error('导出失败:', error);
      alert('导出失败，请检查控制台日志');
    }
  }

  function handleExportZip() {
    console.log('开始生成ZIP');
    if (!zip.files || Object.keys(zip.files).length === 0) {
      return alert('请先点击导出Markdown');
    }

    zip.generateAsync({ type: 'blob' }).then(content => {
      const filename = `xhs-notes-${Date.now()}.zip`;
      const link = document.createElement('a');
      link.href = URL.createObjectURL(content);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(link.href);
      console.log('ZIP文件已生成:', filename);
    }).catch(error => {
      console.error('ZIP生成失败:', error);
      alert('打包失败，请检查控制台日志');
    });
  }


  // 在媒体下载部分修改GM.xmlHttpRequest调用
  async function downloadMedia(url, filename) {
    try {
      const response = await GM.xmlHttpRequest({
        method: "GET",
        url: url,
        headers: {
          'Referer': 'https://www.xiaohongshu.com/',
          'User-Agent': navigator.userAgent,
          'Origin': 'https://www.xiaohongshu.com',
          'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
          'Sec-Fetch-Dest': 'image',
          'Sec-Fetch-Mode': 'no-cors',
          'Sec-Fetch-Site': 'same-site'
        },
        responseType: "blob",
        anonymous: true // 重要：不发送cookie
      });

      if (response.status >= 200 && response.status < 300) {
        return response.response;
      }
      throw new Error(`HTTP ${response.status}`);
    } catch (error) {
      console.error('下载失败:', url, error);
      return null;
    }
  }

  // 修改后的处理函数
  async function processMedia(note) {
    const mediaFolder = zip.folder(note.id);

    // 处理图片
    for (const [index, img] of note.images.entries()) {
      if (img.url) {
        const blob = await downloadMedia(img.url);
        if (blob) {
          mediaFolder.file(`image_${index+1}.jpg`, blob);
          img.name = `image_${index+1}.jpg`;
        }
      }
    }

    // 处理视频
    if (note.video?.url) {
      const blob = await downloadMedia(note.video.url);
      if (blob) {
        mediaFolder.file(`video.mp4`, blob);
        note.video.name = `video.mp4`;
      }
    }
  }

  init();
})();
```

### 打包下载 ZIP

跟文件大小和数量没有关系

```js
// ==UserScript==
// @name         数据导出为 ZIP
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  捕获当前页面数据，生成 Markdown 文件并打包为 ZIP 下载
// @author       你
// @match        https://www.xiaohongshu.com/*
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js
// ==/UserScript==

(function() {
    'use strict';

    // 创建 ZIP 并下载
    function exportToZip() {
        const data = captureData();
        const zip = new JSZip();

        for(var i =0;i<10000;i++){
            zip.file(`meta-${i}.json`, JSON.stringify(data, null, 2));
        }
        
        zip.generateAsync({ type: 'blob' }).then(content => {
            saveAs(content, `${data.title.replace(/[\\/:*?"<>|]/g, '_')}.zip`);
        });
    }
    
    exportToZip()
})();
```

### 跑通 Demo

```js
// ==UserScript==
// @name         数据导出为 ZIP（修复版）
// @namespace    http://tampermonkey.net/
// @version      2.0
// @match        https://www.xiaohongshu.com/*
// @grant        unsafeWindow
// ==/UserScript==

(function() {
    'use strict';

    // 动态注入 JSZip 到页面环境
    const injectScript = (url, callback) => {
        const script = document.createElement('script');
        script.src = url;
        script.onload = callback;
        document.head.appendChild(script);
    };

    // 第一步：加载 JSZip
    injectScript('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js', () => {
        // 第二步：加载 FileSaver
        injectScript('https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js', () => {
            // 确保库已加载
            const { JSZip, saveAs } = unsafeWindow;

            // 创建 ZIP 实例
            const zip = new JSZip();

            // 添加示例文件
            for (let i = 0; i < 10; i++) {
                zip.file(`meta-${i}.json`, 'debug content');
            }

            // 生成并下载
            zip.generateAsync({ type: 'blob' }).then(content => {
                saveAs(content, 'xhs.zip');
            });
        });
    });
})();
```

另一种方式注入还是没有办法

```shell
// ==UserScript==
// @name         数据导出为 ZIP（修复版）
// @namespace    http://tampermonkey.net/
// @version      2.0
// @match        https://x.com/*
// @grant        unsafeWindow
// @grant        GM.xmlHttpRequest
// @grant        GM_addStyle
// ==/UserScript==

(function() {
    'use strict';

       // 1. 通过GM.xmlHttpRequest获取脚本内容
    const loadScript = (url, callback) => {
        GM.xmlHttpRequest({
            method: "GET",
            url: url,
            onload: (res) => {
                // 2. 创建Blob URL绕过CSP
                const blob = new Blob([res.response], { type: "text/javascript" });
                const url = URL.createObjectURL(blob);
                const script = document.createElement('script');
                script.src = url;
                script.onload = () => URL.revokeObjectURL(url);
                document.head.appendChild(script);
                callback();
            }
        });
    };

      // 3. 链式加载库
    loadScript('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js', () => {
        loadScript('https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js', () => {

            // 确保库已加载
            const { JSZip, saveAs } = unsafeWindow;

            // 创建 ZIP 实例
            const zip = new JSZip();

            // 添加示例文件
            for (let i = 0; i < 10; i++) {
                zip.file(`meta-${i}.json`, 'debug content');
            }

            // 生成并下载
            zip.generateAsync({ type: 'blob' }).then(content => {
                saveAs(content, 'xhs.zip');
            });

        });
    });



})();
```

## Problems

### xsec_token 过期，生成的未必是永久链接 #issue/wontfix

```shell
https://www.xiaohongshu.com/explore/66fa0075000000002c014d4c?xsec_token=AB1VctWn-DyPKogC3hpr1NlSKFmr1heOIW3HEn7naWRFU=
```

### 问题：`grant` #issue/closed

最后定位到是 的问题，只有在 `@grant none` 的时候，zip.generateAsync 才能生成文件成功

只要引入了 `unsafeWindow/GM_addStyle/GM.xmlHttpRequest` 或者删除 `@grant none` 都会失效。

相关的 ISSUE

- https://github.com/Stuk/jszip/issues/814
- https://github.com/Stuk/jszip/issues/934

### CSP (Content Security Policy) Limit

FF 上已经把 `Missing Content Security Policy enable/disable` 移除掉了

- https://www.reddit.com/r/firefox/comments/ubb8d4/how_to_disable_csp/
- https://support.mozilla.org/zu/questions/1374424

但是可以通过拓展临时禁用一下

- https://addons.mozilla.org/en-US/firefox/addon/disable-csp-for-a-minute/

## What

## Reference

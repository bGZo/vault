---
aliases:
  - 用 ASTRO 重新做网站这件事
created: 2025-10-12T00:39:37
modified: 2025-10-16T06:01:57
title: 用 ASTRO 重新做网站这件事
---

# 用 ASTRO 重新做网站这件事

受 [[ccbikai-BroadcastChannel|BroadcastChannel]] 和 https://www.pseudoyu.com 的启发，突然觉得 Astro 这个东西可以把自己过去好多玩具聚合：

- https://blog.bgzo.cc
- https://cast.bgzo.cc
- https://base64.bgzo.cc
- https://404.bgzo.cc
- https://where-is-my-web.vercel.app

能做出一个更酷的缝合怪出来，我猜 😇

## 架构选型

- Tool
	- Astro
	- Bun
	- VUE3
- Tech Stack
	- Github Pages
	- Vercel

## RoadMap

- [x] #1260/功能 主页展示个人信息，社交媒体链接
- [x] #1260/功能 博客展示
- [x] #1260/功能 兼容 [[ccbikai-BroadcastChannel|BroadcastChannel]]
- [x] #1260/功能 在线小工具
- [x] #1260/功能 Playground / Labs 展示
- [x] #1260/优化 Markdown 支持 Callout 语法
- [ ] #1260/优化 博客目录显示
	- [ ] https://daily-dev-tips.com/posts/adding-a-toc-in-astro/
	- [ ] https://github.com/remarkjs/remark-toc
	- [ ] https://dev.to/dailydevtips1/adding-a-toc-in-astro-4kehhttps://www.yuloveboyi.com/
- [ ] #1260/功能 增加思维导图
	- [ ] https://coderxi.com/posts/remark-markmap-doc
- [ ] #1260/功能 增加 Projects 页，项目、地址手工维护
- [ ] #1260/优化 每个索引页重新设计，题图 + 引用 + 格子背景
- [ ] #1260/功能 黑暗模式
- [ ] #1260/功能 博客评论，应该使用独立的仓库
- [ ] #1260/功能 Tools 页面增加友情链接
- [ ] #1260/功能 增加友情链接，互换链接地址
	- [ ] https://www.pseudoyu.com/friends
- [ ] #1260/优化 Blog 索引页的切换逻辑 + 样式
- [ ] #1260/功能 探索 Vercel 的部署
- [ ] #1260/功能 看下能不能潜入自己的 BGM、STEAM 数据进行展示
	- [ ] SSR
	- [ ] https://asyncx.top/
- [ ] #1260/功能 多语言支持
- [ ] #1260/优化 底部页签版权声明

daily-dev-tips.com/posts/adding-a-toc-in-astro

### Astro 是什么

核心思想是群岛架构，不同与传统 VUE 的单页应用，而是对于不用页面按需加载，在网页加载速度和架构兼容性上来说是一流。

模板的注入类似 Jekyll，但是比前者更加灵活。

### Bun 是什么

是用 Zig 语言实现的另一个 Javascript 运行时，目标是兼容 `Node.js`，提供更加快速的构建体验。

## 开始动手

### 初始化一个 Astro 项目

```shell
mkdir astro-demo
npm create astro@latest
```

### 添加 Vue / TailwindCSS 等依赖

```shell
npm install @astrojs/vue
npm install @astrojs/tailwind
```

### 创建页面基本骨架、引入博客页面

source via: https://github.com/bGZo/playground/commit/0545ea8c6122266cfe6249497136f1f9543559f5

```ts
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');

  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { post },
  }));
}
```

- [ ] `getStaticPaths` 的作用是什么？为什么加上这一行就会变成静态页面？
- [ ] 为什么命名 `[slug].astro`

- 文档参考: https://docs.astro.build/en/guides/content-collections/
- 利用 `tailwindcss@typography` 优化内容排版显示；

### 迁移 [[ccbikai-BroadcastChannel|BroadcastChannel]]

via: https://github.com/bGZo/playground/commit/cd7875a32ce00d3c5fb150dc5f4e346225a4b54

目前还不清楚为什么原项目用 `ofetch` 可以直接用环境变量的代理，而我迁移过来的代码不行，报错：

```shell
Fetching https://telegram.dog/s/imbgzo { before: '', after: '', q: '', type: 'list', id: '' }
Fetch failed: [GET] "https://telegram.dog/s/imbgzo?before=&after=&q=": <no response> [TimeoutError]: The operation was aborted due to timeout
Error details: FetchError: [GET] "https://telegram.dog/s/imbgzo?before=&after=&q=": <no response> [TimeoutError]: The operation was aborted due to timeout
    at runNextTicks (node:internal/process/task_queues:65:5)
    at process.processTimers (node:internal/timers:546:9)
    at async $fetchRaw2 (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/ofetch/dist/shared/ofetch.03887fc3.mjs:270:14)
    at async $fetch2 (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/ofetch/dist/shared/ofetch.03887fc3.mjs:316:15)
    at async getChannelInfo (file:///home/bgzo/workspaces/playground/astro-demo/dist/server/chunks/index_BEp_DU6L.mjs:219:22)
    at async file:///home/bgzo/workspaces/playground/astro-demo/dist/server/pages/talk.astro.mjs?time=1760286561784:13:19
    at async callComponentAsTemplateResultOrResponse (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/astro/dist/runtime/server/render/astro/render.js:91:25)
    at async renderToAsyncIterable (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/astro/dist/runtime/server/render/astro/render.js:133:26)
    at async renderPage (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/astro/dist/runtime/server/render/page.js:36:24)
    at async lastNext (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/astro/dist/core/render-context.js:201:25) {
  [cause]: Error [TimeoutError]: [TimeoutError]: The operation was aborted due to timeout
      at node:internal/deps/undici/undici:13484:13
      at runNextTicks (node:internal/process/task_queues:65:5)
      at process.processTimers (node:internal/timers:546:9)
      at async $fetchRaw2 (file:///home/bgzo/workspaces/playground/astro-demo/node_modules/ofetch/dist/shared/ofetch.03887fc3.mjs:258:26) {
    code: 23
  }
}
```

所以用硬编码 `HttpsProxyAgent` 和 `SocksProxyAgent` 作 `agent` 的方式，发现仍然不行，最后用 `node-fetch` 替代 `ofetch`，最终成功了，确定是网络因素，关键代码如下：

```ts
export async function getChannelInfo(Astro, { before = '', after = '', q = '', type = 'list', id = '' } = {}) {
  // xxx
  console.info('Fetching', url, { before, after, q, type, id })
  const agent = getEnv(import.meta.env, Astro, 'HTTP_PROXY') ?
    new HttpsProxyAgent(getEnv(import.meta.env, Astro, 'HTTP_PROXY')) : undefined
  // const proxyUrl = 'socks5://127.0.0.1:10800'
  // const agent = new SocksProxyAgent(proxyUrl)
  // console.info('Fetch agent:', agent)
  try {
    const queryString = new URLSearchParams({
      before: before || '',
      after: after || '',
      q: q || '',
    }).toString()
    const fullUrl = queryString ? `${url}?${queryString}` : url
    const response = await fetch(fullUrl, {
      headers,
      agent,
      timeout: 30000,
    })
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`)
    }
    const html = await response.text()
    console.info('Fetch successful, HTML length:', html.length)
    // xxxx
    return channelInfo
  } catch (error) {
    console.error('Fetch failed:', error.message)
    console.error('Error details:', error)
    throw error
  }
}
```

- [ ] `middleware.js` 的作用是什么？
- [ ] `prefetch.json.ts` 的作用是什么？
	- [ ] 提醒浏览器预先加载页面。

### 博客页面排序/分类切换

via: https://github.com/bGZo/playground/commit/11237705d03722c5e63c1a1168761cd7844b17d4

排序原理是 b 的日期比 a 的打，即为正数，即会排到前面：

```ts
posts.sort(
  (a: any, b: any) =>
    new Date(b.data.created).getTime() - new Date(a.data.created).getTime()
);
```

目前博客的分类切换为 CSS 样式切换，关键代码如下：

```js

document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById(
    "category-select"
  ) as HTMLSelectElement;
  const listItems = document.querySelectorAll(
    "li[data-category]"
  ) as NodeListOf<HTMLElement>;
  select.addEventListener("change", () => {
    const selected = select.value;
    listItems.forEach((li: HTMLElement) => {
      const category = li.dataset.category;
      if (selected === "" || category === selected) {
        li.style.display = "";
      } else {
        li.style.display = "none";
      }
    });
  });
});
```

后续打算用 VUE 直接操作展示列表进行动态切换。

### 设置创建时间和更新时间

via: https://github.com/bGZo/playground/commit/11511f4eaac9dbe27ce34ea1f545de79a63a63f7

读取 post 的时间，在博客页面设置属性即可，关键代码如下：

```markdown
---
import dayjs from 'dayjs';
---
<p class="text-gray-600 text-sm">Created: {dayjs(post.data.created).format('YYYY-MM-DD')} | Updated: {dayjs(post.data.modified).format('YYYY-MM-DD')}</p>
```

### 增加在线工具页面，引用 VUE

via: https://github.com/bGZo/playground/commit/44d085d111a33ceb87aaa6681aa16a696b97c0e2

动态加载 `tool` 文件夹下面的工具组件，加载内部的标题和描述；

```ts
// 过滤掉索引页面本身，只保留工具页面
const toolPromises = Object.entries(toolModules)
	.filter(([path]) => path !== './tool.astro') // 排除当前文件
	.map(async ([path, module]) => {
		const page = await module() as any;
		return {
			slug: path.replace('./', '').replace('.astro', ''), // 获取文件名作为 slug
			title: page.title || '未命名工具',
			description: page.description || '暂无描述'
		};
	});

// 等待所有异步操作完成
const tools = await Promise.all(toolPromises);
```

- [ ] `Promiss.all()` 的作用是什么？为什么使用它？

引入 VUE 组件，潜入页面：

```markdown
---
import StringEscape from '../../components/StringEscape.vue';
export const title = '字符串转义工具';
export const description = '用于转义字符串中的特殊字符，如 HTML 实体编码。';
---
<StringEscape client:load/>
```

- [ ] `<StringEscape client:load/>` 中 `client:load` 的作用是什么？

### 合并 `playground` 项目到本博客中

via: https://github.com/bGZo/playground/commit/baa2b2904841639a7f3e3e21e7fbbda935ebc0ec

之前的 playground 实际上只是一个单页应用，潜入进来也比较简单，直接引入 `vue`，然后像 `tool` 页面一样引入即可。

### 主页引入 ICON 图标

via:

- https://github.com/bGZo/playground/commit/2ae4e9e62dc18588603a997b1e191a6149433df4
- https://github.com/bGZo/playground/commit/30ed935aca00999d4a78924f3869b9857b879d94

有几种引入方式：

#### VUE 引入

```vue
<template>
  <svg class="h-6 w-6 align-middle" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" viewBox="0 0 24 24" >
    <path
      d="M12,1C5.9,1,1,5.9,1,12s4.9,11,11,11s11-4.9,11-11S18.1,1,12,1z M20.9,11h-4c-0.2-2.8-1.1-5.4-2.7-7.7C17.8,4.2,20.5,7.3,20.9,11zM9.1,13h5.9c-0.3,2.7-1.3,5.3-2.9,7.4C10.3,18.3,9.3,15.7,9.1,13zM9.1,11c0.3-2.7,1.3-5.3,2.9-7.4c1.7,2.2,2.7,4.8,2.9,7.4H9.1z M9.7,3.3C8.2,5.6,7.3,8.2,7.1,11h-4C3.5,7.3,6.2,4.2,9.7,3.3zM3.1,13h4c0.2,2.8,1.1,5.4,2.7,7.7C6.2,19.8,3.5,16.7,3.1,13z M14.3,20.7c1.5-2.3,2.4-4.9,2.7-7.7h4C20.5,16.7,17.8,19.8,14.3,20.7z">
    </path>
  </svg>
</template>
```

然后在具体位置

```html
<span class="text-lg flex items-center">
	<span class="mr-1"><Location /></span>
	{profile.location}
</span>
```

参考： https://github.com/vuejs/docs/blob/31b4521ad0607a74e284fa7c62502b56a7710e86/src/about/team/TeamMember.vue#L7

### Astro 原生引入

```markdown
---
import bluesky from "../assets/icon/bluesky.svg";
---
{
  profile.socialMedia["Bluesky"] &&
	profile.socialMedia["Bluesky"].length > 0 && (
	  <a
		href={`https://bsky.app/profile/${profile.socialMedia["Bluesky"]}`}
		title="Bluesky"
		target="_blank"
>
		<img
		  {...bluesky}
		  alt={`bsky.app/profile/${profile.socialMedia["Bluesky"]}`}
		  class="social-icon w-6"
		/>
	  </a>
	)
}
```

- [ ] 语法结构如何理解？
- [ ] 官方动态批量引入？

### 引入阅读时间

via: https://github.com/bGZo/playground/commit/019dfde5c80acf2423b42a2f9d6b509f8c27fa03

官方教程: https://docs.astro.build/zh-cn/recipes/reading-time

### 工具增加双拼解码

via: https://github.com/bGZo/playground/commit/c83d30d8dbbad315d457ab0a3e357ffeb2d838e2

编码，参考： https://sspai.com/post/56134

### Markdown 语法拓展

自带的语法当前不支持 Callout(admonition note)，不支持 mark 高亮。

### Callout

安装 https://github.com/myl7/remark-github-beta-blockquote-admonitions

安装完插件后，发现虽然正确解析了，但是没有 CSS 样式，需要自己找。

via: https://ssshooter.com/add-admonitions/, 博主的这个博客没有开源，只能借下它的 CSS 了。

### Mark

- https://github.com/twardoch/remark-mark-plus#usage-with-remark-cli
	- 这个没有生效

## 部署

### Github Pages

via: https://github.com/bGZo/playground/commit/900182f47e79a6fcfa61c8c58c73c93a0ff5ccf8

有几个注意点：

- 声明 `.nojekyll`: 默认 GitHub Pages 的站点是 Jekyll，直接部署上去，无法展示 `_astro` 下面的文件，请求会报错，需要添加 `.nojekyll` 的文件声明非 Jekyll 站点才可，via: https://github.com/withastro/starlight/issues/3339
- 相对路径，因为普通仓库的 Github Pages 命名空间不同，需要声明 `base` 属性：

```ts
export default defineConfig({
  // via: https://docs.astro.build/en/guides/deploy/github/
  site: 'https://bgzo.github.io',
  base: '/github-pages',
})
```

- 网站内有链接跳转的部分同样需要重新处理一遍，我使用了全部路径而非相对路径处理这个问题，额外的替换处理是为了避免不设置 base，导致路径失效

```markdown
---
const { SITE_URL } = Astro.locals
const SITE_URL_NO_SLASH = SITE_URL.endsWith('/') ? SITE_URL.slice(0, -1) : SITE_URL;
---
<a href={SITE_URL_NO_SLASH + '/' + link.path} class={currentPath === link.path ? 'font-bold' : ''}>{link.name}</a>
```

via: https://docs.astro.build/zh-cn/guides/deploy/github, https://docs.astro.build/zh-cn/reference/configuration-reference/#base

### 区分本地和生产

via: https://github.com/bGZo/playground/commit/101009794f945cc97ca5962800d252d317497ea3

本地生产的 `BASE_URL` 不同，正好可以用 `npm run dev` 和 `npm run build` 做区分，直接在 `package.json` 文件中声明环境即可，如：

```json
"dev": "NODE_ENV=development astro dev",
"build": "NODE_ENV=production astro build && touch dist/client/.nojekyll",
```

然后在配置文件中声明 URL:

```ts
site: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:4321' : 'https://bgzo.github.io',
```

### 绑定域名

前几年绑定域名，我记得还需要将 IPv4 的地址写到 DNS 解析记录里，今天测试了下，用 CNAME 也可以。需要在根目录下增加一个 `CNAME` 文件，介入对应域名即可。

## 备忘

有一些不知道要写在哪里的点，就统一放在这里：

- 路由命名，因为主要依靠 Github Pages（下叫 Pages），所以路径上，可能会有个子其他 Pages 命名冲突的情况，比如我我的某个路由叫 `bgzo.github.io/playground`， 正好我有个项目就叫 `playground` 且开启了 Pages，那么 Gihtub 会优先取后者，即其他项目的页面，而不是你当前这个项目的路由。
- [ ] 为什么 Mac 熄屏后再打开，转发的端口、页面就会失效，需要重新转发；

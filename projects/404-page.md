---
aliases:
  - 不存在的页面
created: 2024-08-01
modified: 2025-07-02T22:14
title: 不存在的页面
type: product/done
tags:
  - gtd/done
---

# 不存在的页面

## 「1」

![](https://raw.githack.com/bGZo/assets/dev/2025/1751465395381.png)

## 「2」

这是我构想的第二种形式，根据是否墙内 IP 跳转 Youtube/Bilibili

<iframe src='http://404.bgzo.cc' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='http://404.bgzo.cc' target='_blank' class='external-link'>http://404.bgzo.cc</a></center>

### Issue

```shell
Access to fetch at 'https://pv.sohu.com/cityjson?ie=utf-8' from origin 'https://bgzo.cc' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

> When you are using Postman they are not restricted by this policy. Quoted from *[Cross-Origin XMLHttpRequest](https://developer.chrome.com/docs/extensions/mv2/xhr/)*:
> Regular web pages can use the XMLHttpRequest object to send and receive data from remote servers, but they're limited by the same origin policy. Extensions aren't so limited. An extension can talk to remote servers outside of its origin, as long as it first requests cross-origin permissions.
> https://stackoverflow.com/questions/20035101/why-does-my-javascript-code-receive-a-no-access-control-allow-origin-header-i

---

```shell
Fetch API is blocked by browser
```

> Change API to another
> https://stackoverflow.com/questions/56048166/getting-blockedother-error-status-from-the-browser-in-angular-application

```js
/** <script src="https://pv.sohu.com/cityjson?ie=utf-8"></script>
*/
$(document).ready(function() {
  if (returnCitySN["cname"] == "上海市" || returnCitySN["cid"] == "310000" || returnCitySN["cname"] == "北京市") {
	window.location.href = 'https://www.bilibili.com/233';
	console.log(returnCitySN["cname"]);
  } else {
	$('body').css('display','block');
  };
  $("#player_iframe").allofthelights();
});
```

---

```shell
GET https://pv.sohu.com/cityjson?ie=utf-8
net:ERR_BLOCKED_BY_CLIENT
```

https://stackoverflow.com/questions/23341765/getting-neterr-blocked-by-client-error-on-some-ajax-calls

---
created: 2024-08-01
description: 不存在的页面
type: product/done
---

<iframe src='http://404.bgzo.cc' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'/><center>via: <a href='http://404.bgzo.cc' target='_blank' class='external-link'>http://404.bgzo.cc</a></center>
## References
  - [Getting 'blocked:other' error status from the browser - In Angular application, I made a rest api call to fetch the information from the server - Stack Overflow](https://stackoverflow.com/questions/56048166/getting-blockedother-error-status-from-the-browser-in-angular-application)
    - Fetch API is blocked by browser.
    - Change API to another
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
      - `GET https://pv.sohu.com/cityjson?ie=utf-8 net:ERR_BLOCKED_BY_CLIENT`
        - [google chrome extension - Getting "net:ERR_BLOCKED_BY_CLIENT" error on some AJAX calls - Stack Overflow](https://stackoverflow.com/questions/23341765/getting-neterr-blocked-by-client-error-on-some-ajax-calls)
      - `Access to fetch at 'https://pv.sohu.com/cityjson?ie=utf-8' from origin 'https://bgzo.cc' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.`
        - [jquery - Why does my JavaScript code receive a "No 'Access-Control-Allow-Origin' header is present on the requested resource" error, while Postman does not? - Stack Overflow](https://stackoverflow.com/questions/20035101/why-does-my-javascript-code-receive-a-no-access-control-allow-origin-header-i)
          - When you are using Postman they are not restricted by this policy. Quoted from *[Cross-Origin XMLHttpRequest](https://developer.chrome.com/docs/extensions/mv2/xhr/)*:
            - > Regular web pages can use the XMLHttpRequest object to send and receive data from remote servers, but they're limited by the same origin policy. Extensions aren't so limited. An extension can talk to remote servers outside of its origin, as long as it first requests cross-origin permissions.
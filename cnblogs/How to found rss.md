Some websites will include element whose type is `application/atom+xml` or `application/rss+xml`. They would include RSS link.

```xml
<link rel="alternate" type="application/atom+xml" title="${source.title}" href="${source.url}">
```

And following are some address they mostly used:

```xml
./feed
./rss.xml
./feed.xml
./atom.xml
./rss/index.xml
./index.xml
./rss
./rss/rss
./rss/rss.xml
<!-- Z-Blog via: https://bbs.zblogcn.com/thread-3527.html-->
./feed.asp?user=userID
./feed.asp?tags=TagID
<!-- Youtube -->
https://www.youtube.com/feeds/videos.xml?channel_id=<channel_id>
https://www.youtube.com/feeds/videos.xml?playlist_id=<playlist_id>
```

Source via: https://note.bgzo.cc/
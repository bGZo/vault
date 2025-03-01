---
title: Dashboard
created: 2025-01-18T09:49:12
modified: 2025-01-18T10:33:07
cssclasses:
  - cards
---

## Creation

### Focus on

```dataview
table  
from -"templates"  
where type = "project" or type="product"
```

### Writings

> [!cite]
> 每个伟大的作家都会创造出一个独属于自己的世界，而那个世界——那个世界的色彩、气味、声音甚至触觉——并不会随着阅读的结束而完全消失。好的虚构会侵入现实。
> 
 http://m.wufazhuce.com/one/3122

```dataview
table title as Title
from -"templates"
where 
	status = "writing/idea" or 
	status = "writing/outline" or
	status = "writing/draft" or
	status = "writing/edit" or
	status = "writing/published" or
    type = "writing"
```

## Consume

### Animes

> [!tip]
> 我就是喜欢纸片人。他们是点阵、是数据、这种事情我知道。
> 那你喜欢的那个男孩又是什么? 蛋白质? 钙?
> 重要的是充满爱的心啊。
>
> https://bgm.tv/character/780

```dataview
table
	( "![](" + cover +")" ) as Cover,
	aliases as Naming,
	rating as Rating
from -"templates"
where 
	type = "anime" 
```

### Books

> [!tip]
> 读书和抽鸦片是一样的，都是捧着植物尸体产生幻觉
> 
> https://www.v2ex.com/t/1006112

```dataview
table 
	( "![](" + cover +")" ) as Cover,
	rating as Rating
from -"templates"
where type = "book" or type="book/dev"
sort rating desc

```

### Games

```dataview
table 
	( "![](" + cover +")" ) as Cover,
	rating as Rating
from -"templates"
where type = "game" or type="galgame"
sort rating desc
```


### Video
```dataview
table 
	( "![](" + cover +")" ) as Cover
from -"templates"
where type = "video" 
    and !contains(tags, "NSFW")
sort created desc
```

### Movies
```dataview
table 
	( "![](" + cover +")" ) as Cover
from -"templates"
where type = "video" 
    and contains(tags, "movie")
sort created desc
```



### Podcasts
```dataview
table 
	( "![](" + cover +")" ) as Cover
from -"templates"
where type = "podcast-episode" 
sort created desc
```

### AVs
```dataview
table 
	( "![](" + cover +")" ) as Cover,
	description,
	telegram
from -"templates"
where type = "video" 
    and contains(tags, "NSFW")
sort created desc
```

## Archives

### Webpages

```dataview
table title
from -"templates"
where type = "archive-web" 
sort created desc
```

### Projects

```dataview
table  
from -"templates" 
where type = "project/done" or type="product/done"
```


### Star Repo
```dataview
table 
    description,
	( "![](https://img.shields.io/github/stars/" + title + "?style=for-the-badge&label=stars)" ) as Star,
	( "![](https://img.shields.io/github/repo-size/" + title + "?style=for-the-badge&label=size)" ) as Size,
    ( "![](https://img.shields.io/github/created-at/" + title + "?style=for-the-badge&label=date)" ) as Created-at,
    "#"+tags
from -"templates" 
where type = "repo"
```

## Others

```dataview
list 
from -"templates" 
where type = "hobby"
```

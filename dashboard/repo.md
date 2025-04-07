---
created: 2025-04-07T21:23:11
modified: 2025-04-07T21:23:37
---
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

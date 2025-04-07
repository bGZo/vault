---
created: 2025-04-07T21:17:15
modified: 2025-04-07T21:18:20
---

```dataview
table 
	( "![](" + cover +")" ) as Cover,
	rating as Rating
from -"templates"
where type = "game" or type="galgame"
sort rating desc
```

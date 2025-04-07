---
created: 2025-04-07T21:14:42
modified: 2025-04-07T21:19:20
cssclasses:
  - cards
  - cards-align-bottom
  - cards-cols-3
---

```dataview
table 
	( "![](" + cover +")" ) as Cover
from -"templates"
where type = "video" 
    and !contains(tags, "NSFW")
sort created desc
```

---
draft: true
created: 2025-04-07T21:18:53
modified: 2025-04-07T21:19:07
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
    and contains(tags, "movie")
sort created desc
```

---
draft: true
created: 2025-04-07T21:20:17
modified: 2025-04-07T21:20:31
cssclasses:
  - cards
  - cards-cols-3
  - cards-align-bottom
---
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

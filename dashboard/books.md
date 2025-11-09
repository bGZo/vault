---
draft: true
created: 2025-04-07T20:30:43
modified: 2025-04-07T21:13:51
cssclasses:
  - cards
  - cards-align-bottom
  - cards-cols-5
---
> [!tip]
> 读书和抽鸦片是一样的，都是捧着植物尸体产生幻觉
>
> https://www.v2ex.com/t/1006112

```dataview
table 
	( "![](" + cover +")" ) as Cover,
	rating as Rating
from -"templates"
where 
    type = "book" 
    or type="book/dev"
    or type = "weread-notes"
sort readingDate desc
```

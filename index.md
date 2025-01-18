---
aliases: Home
title: Home
created: 2024-08-14T12:00:00
modified: 2025-01-12T03:16:25
comments: false
---

> [!NOTE] TL;DR
> -  [Configuration](custom/index)
> - Work
> 	- [Skills](skills/index)
> 	- [Projects](projects/index)
> - Life: free time wasting for a better life
> 	- Living (\* required absolutely)
> 		- Health
> 		- Relationship: family and lovers.
> 		- Sex
> 	- Hobbies
> 		- Consuming
> 			- watching [[animes]] / [[manga]]
> 			- playing [[games]]
> 			 - reading [[books]] / [[galgame]]
> 			 - listening to [[musics]] / [[podcasts]]
> 		- Creation
> 			- [Weekly](weekly)
> 			- drawing pixel [[illustration]] 

Welcome my second brain I tried to build with [obsidian](obsidian) & [quartz](https://quartz.jzhao.xyz). I used [logseq](logseq) before and now I [give it up](1218-giving-up-logseq), which is the reason why some part of notes is ugly and wired[^giving-up-logseq].

Anyway, wish you have a fun time. That would be my pleasure.

## Why choose work & life classify?

The hard truth is, we're spending the most time of life to work.[^as-non-work-flow] During this time, solving business problems is the main subject.

![](https://raw.githack.com/bGZo/assets/dev/2024/Screenshot_20240711_224841_Kiwi%20Browser.png)

## Persistent store

Considered working business, the part of working should not be open-source, they deserved a private repository.

Then you should take care avoiding the [wrong second brain](1198-wrong-second-brain), because notes should not be your trash inbox, which always make your system growing up, with high entropy increases, until they being a black hole.

So dealing problem with project is the main subject for this notes, which should have a certain deadline.

## PKM announcement: Soft rules

Whatever you're using, the half life of something (such as rules) is not changed fast. I would try my best to build it to a evergreen tree. [^maintain-soft-rules]

> [!IMPORTANT]
> Using syntax sugar as less as possible.

Such like `macros` /  `properties::` / `org-mode` / `task management` on logseq, `wikitext` / `embed tweet/youtube as image` on obsidian as well.

### Page naming

- Use `-` to connect two word rather blank for **readable url**.
- Use plural of noun to separate different pages
	- using `book` to talk something topic.
	- using `books/xxx` to talk something specific.
- Don't add the `[[]]` in `page_name`
- Never renaming page name after `git commit`.
	- the pain of renaming on git is high, which means the history would be lost at all.

### Properties

Keep order, dictionary order is the best.

### Template

- Every main topic page should have a template.
- All template properties should extend `page`.
	- Keep adding less properties as much as possible.

### Tags

Using `#[[]]` instead of `#`. They would be popped menu friendly, while editing again.

### Hierarchy

Hierarchy/Namespace is not silver bullet. Delay your use of namespaces until you have refined your understanding of how they might suit your workflows. [^namespace-usage]

## © Copyright

Copyright 2022 - 2024 [bGZo](https://github.com/bGZo). All rights reserved. The contents is licensed under a [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/); the code is under [MIT](https://github.com/bGZo/blog/blob/main/LICENSE) licence. The contents and comments are copyright their respective authors, submission implies license to publish on this web site.

<center><img src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" alt="http://creativecommons.org/licenses/by-sa/4.0/"/><img src="https://raw.githack.com/bGZo/assets/dev/2024/Written-By-Human-Not-By-AI-Badge-white.svg" alt="https://notbyai.fyi"/></center>

[^giving-up-logseq]:: two formats would be existed on here: outliner & paragraph.
[^as-non-work-flow]: If you are a student, or someone else, the work could be something you worked for living. Whether they should separate with space time, there are a thousand Hamlets in a thousand people's eyes. At least in China, space time always conflicts with work, so talking about that is always ambiguous...
[^maintain-soft-rules]: Maybe the flow you have to change in next version, or the problem maybe solved, it's really not have too much value.
[^namespace-usage]: https://www.logseqmastery.com/blog/logseq-namespaces, https://discuss.logseq.com/t/outline-overview-for-sidebar/740/19
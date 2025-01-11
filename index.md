---
aliases: 首页
title: Home
created: 2024-08-14T12:00:00
modified: 2025-01-10T08:27:57
---

## TL;DR

- Work
	- [Skills](/skills)
	- [Projects](/projects)
- Life

## PKM announcement

Whatever you're using, half life of something (rules) is not changed. I would try my best to build it evergreen tree. [^maintain-soft-rules]

### Knowledge classify & Second brains index
#### Work time for living

![](https://raw.githack.com/bGZo/assets/dev/2024/Screenshot_20240711_224841_Kiwi%20Browser.png)

The hard truth is, we're spending the most time of life to work.[^as-non-work-flow] During this time, solving business problems is main problem, which needs:

- [Skills](/skills)
	- Hard
		- Tech stack
			- programming language
			- framework
		- Experiences
	- Soft
		- Languages
		- Communication
		- Speech
- [Projects](/projects)
    - Side project
    - Big main project

![](https://raw.githack.com/bGZo/assets/dev/2024/20241214214634.png)

#### Free time wasting for better life

At least, the other time leaving is belonging you, so you could spend on:

  - [[life]] with self problems (\* required absolutely)
	- like living, health, privacy, sex.
	- especially on **relationship** with your family and lover.
  - [[creation]] that exclude consuming, while doing something real.
  - [[inbox]] that collect, classify, link and **delete** info you token.
	  - watching [[animes]] / [[manga]]
	  - playing [[games]] / [[productivity]] [[tools]]
	  - reading [[books]] / [[galgame]]
	  - listening to [[musics]] / [[podcasts]]
	  - drawing the [[illustration]] with [[plex]]
	  - learn the CS knowledge
		  - [[operating-system]]
			- [[windows]]: wsa / wsl
			- [[linux]]: archlinux / steamdeck / minit
			- [[mac]]:
			- [[android]]: OneUI / ColorOS
			- [[ios]]: iPhone / iPad

```dataview
list 
from -"template"
where type = "hobby"

```

### Persistent store

Considered working business info, this part should not open-source, which deserved a private repository.

Then you should take care avoiding [[1198-wrong-second-brain]], because note system should not really be your "repository", which always make your system grow up with high entropy increases, then leading one ending: trash / garbage.

So dealing problem with project management way, under certain deadline, that would help you get rid of info overtake, and keep focus on your business again.

## Soft rules

> [!IMPORTANT]
> Using syntax sugar as less as possible.

Such like `macros` /  `properties::` / `org-mode` / `task management` on logseq.

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

[^maintain-soft-rules]: Maybe the flow you have to change in next version, or the problem maybe solved, it's really not have too much value.
[^as-non-work-flow]: If you are a student, or someone else, the work could be something you worked for living. Whether they should separate with space time, there are a thousand Hamlets in a thousand people's eyes. At least in China, space time always conflicts with work, so talking about that is always ambiguous...
[^namespace-usage]: https://www.logseqmastery.com/blog/logseq-namespaces, https://discuss.logseq.com/t/outline-overview-for-sidebar/740/19

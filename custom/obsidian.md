---
aliases:
  - 黑曜石
created: 2024-12-14T11:52:18
created-link: "[[20241214]]"
modified: 2024-12-28T10:07:49
changelog: https://obsidian.md/changelog
description: Obsidian is the private and flexible writing app that adapts to the way you think.
document: https://help.obsidian.md
status:
  - tool/star
tags:
  - close-source
  - electron
type: tool
---

## Why: [[1218-giving-up-logseq]]

## How

### Is there portable version for obsidian?

No, official not provide this way to install obsidian.

But obsidian build with electron, so unzip `setup.exe`, then you will get the portable version of obsidian[^unzip-way]

### How setting proxy  for obsidian?

We get the portable version above, proxy as well. Electron could launch with following to use proxy address:

```shell
./Obsidian.exe --proxy-server=http://127.0.0.1:7890
```

## What (The function of obsidian)

### Frontmatter 前页/扉页/版权页/目次

Frontmatter is a way to define properties by adding YAML or JSON at the top of the note. See also Property format.

### Ribbon 功能区

The **ribbon** functions as a container for frequently used action icons.

### Obsidian flavored [[markdown]]

#### Callout

```
> [!note] note
> > [!tldr] abstract / summary / tldr
> > > [!info] info
> > > > [!todo] todo
> > > > > [!tip] tip / hint / important
> > > > > > [!done] success / check / done
> > > > > > > [!help] question / help / faq
> > > > > > > > [!warning] warning / caution / attention
> > > > > > > > > [!fail] failure / fail / missing
> > > > > > > > > > [!danger] danger / error
> > > > > > > > > > > [!bug] bug
> > > > > > > > > > > > [!example] example
> > > > > > > > > > > > > [!quote] quote / cite
```

##### Keep same as Github

- [Support all five types of GitHub admonitions/alerts - Feature requests - Obsidian Forum](https://forum.obsidian.md/t/support-all-five-types-of-github-admonitions-alerts/84920/5)
- [\[Markdown\] An option to highlight a "Note" and "Warning" using blockquote (Beta) · community · Discussion #16925 · GitHub](https://github.com/orgs/community/discussions/16925)

#### Embed files

`![[Link]]`

#### Block references

`![[Link#^id]]`

#### Defining a block

`^id`

#### Strikethroughs

`%%Text%%`

### Template

| ariable     | Description                                     |
| ----------- | ----------------------------------------------- |
| `{{title}}` | Title of the active note.                       |
| `{{date}}`  | Today's date. **Default format:** `YYYY-MM-DD`. |
| `{{time}}`  | Current time. **Default format:** `HH:mm`.      |

### Publish #Paied

Hosted on `publish.obsidian.md/your-site` build-in with $10/month pricing.

## References

- [Obsidian - reddit](https://www.reddit.com/r/ObsidianMD/)
- [Glossary - Obsidian Help](https://help.obsidian.md/Getting+started/Glossary)
- [Obsidian Flavored Markdown - Obsidian Help](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown)
- [Introduction to Obsidian Publish - Obsidian Help](https://help.obsidian.md/Obsidian+Publish/Introduction+to+Obsidian+Publish)
- [Pricing - Obsidian](https://obsidian.md/pricing)
    - [What is stopping you of using Obsidian Sync/Obsidian Publish? : r/ObsidianMD](https://www.reddit.com/r/ObsidianMD/comments/1cji7ym/what_is_stopping_you_of_using_obsidian/)
- [Templates - Obsidian Help](https://help.obsidian.md/Plugins/Templates)
- [About Queries - Tasks User Guide - Obsidian Publish](https://publish.obsidian.md/tasks/Queries/About+Queries)
<iframe src="https://www.youtube.com/embed/LrQVQ37y6IU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen/><center>via: <a href='https://www.youtube.com/watch?v=LrQVQ37y6IU' target='_blank' class='external-link'>https://www.youtube.com/watch?v=LrQVQ37y6IU</a></center>

[^unzip-way]: via: https://www.reddit.com/r/ObsidianMD/comments/pyfin2/obsidian_portable/
import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    Component.Comments({
      provider: 'giscus',
      options: {
        repo: 'bGZo/notes',
        repoId: 'R_kgDOM-7h7w',
        category: 'comments',
        categoryId: 'DIC_kwDOM-7h784CmFf2',
      }
    }),
  ],
  footer: Component.Footer({
    links: {
      "🔙 Home": "https://bgzo.github.io/notes",
      "🔙 Weekly": "https://bgzo.github.io/notes/weekly/",
      "🔗 GitHub": "https://github.com/bGZo/wiki",
      "🔗 Telegram": "https://t.me/imbGZo",
      "🔗 RSS": "https://bgzo.github.io/notes/index.xml"
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.TableOfContents(),
  ],
  right: [
    Component.Graph(),
    Component.Backlinks(),
    Component.DesktopOnly(Component.RecentNotes()),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.RecentNotes()),
  ],
  right: [],
}
<!-- # Front Matter (Metadata) -->

<!-- MarkdownTOC -->

* [Examples](#examples)
* [Redirects](#redirects)
* [Jekyll Built-In Variables](#jekyll-built-in-variables)
  * [Site Variables](#site-variables)
  * [Page Variables](#page-variables)
  * [Other](#other)

<!-- /MarkdownTOC -->

Any file that contains a [YAML](https://yaml.org/) [front matter](https://jekyllrb.com/docs/front-matter/)) block will be processed by Jekyll as a special file. The front matter must be the first thing in the file and must take the form of valid YAML set between triple-dashed lines. Here is a basic example:

```yaml
---
layout: post
title: Blogging Like a Hacker
---
```

Between these triple-dashed lines, you can set predefined variables (see [Jekyll Docs - Front Matter](https://jekyllrb.com/docs/front-matter/) or the [Jekyll - Builtins](Jekyll-Builtins.md) doc for a reference), or create custom ones of your own. These variables will then be available to you to access using Liquid tags both further down in the file and also in any layouts or includes that the page or post in question relies on.

<a id="examples"></a>
## Examples

Front Matter is used for a variety of applications for the site

1. Author Files:

```yaml
---
name: Hope Kroog
gravatar_name: hope
email: hope@openhumans.org
---
```

2. Pages & Layouts

```yaml
---
layout: blog
class: blog-feed
title: Blog
permalink: /blog/
---
```

The `class` field above is automatically appended to certain areas in the code, defined by the `blog.html` layout

<a id="redirects"></a>
## Redirects

You can setup page redirects via `redirect_from: /alternate-url/`

For example, we want the url for the main Categories page to be `http://personalgenomes.org/category`, but we suspect the users might try to type `/categories` or `/archive` instead. So in `category.md`, we've set up the following:

```yaml
---
layout: categories
class: categories-main
title: Categories
permalink: /category/
redirect_from:
  - /categories/
  - /archive/
---
```

<a id="jekyll-built-in-variables"></a>
## Jekyll Built-In Variables

Jekyll has a variety of built-in variables that you can access when working on the site. As above, these are defined in front matter (or sometimes within [tags](Liquid-Templates.md#tags)). See [Jekyll Docs - Variables](https://jekyllrb.com/docs/variables/) for more info.

<a id="site-variables"></a>
### Site Variables

Site wide information + configuration settings from `_config.yml`. For a full list of site variables, see [Jekyll Docs - Site Variables](https://jekyllrb.com/docs/variables/#site-variables). The following variables have been used throughout the site:

* `site.pages` - used in the nav menu and search bar
* `site.posts` - used in blog, sidebar, archives, etc
* `site.related_posts` - not used. Replaced by `_includes/related-posts.html` instead
* `site.data` - used in nav menu
* `site.categories` - used in blog and category pages
* `site.[CONFIGURATION_DATA]` - variables from the config file, such as `site.baseurl`, `site.url`, etc.

<a id="page-variables"></a>
### Page Variables
Page specific information that can be defined in front matter. Custom variables set via the front matter will be available here. For a full list of site variables, see [Jekyll Docs - Page Variables](https://jekyllrb.com/docs/variables/#page-variables). The following variables have been used throughout the site:

* page.content
* page.title
* page.excerpt
* page.url
* page.date
* page.categories
* page.collection
* page.name
* page.next
* page.prev

<a id="other"></a>
### Other
* `layout` - Layout specific information + the front matter. Custom variables set via front matter in layouts will be available here.
* `paginator` - When the paginate configuration option is set, this variable becomes available for use. See Pagination for details.

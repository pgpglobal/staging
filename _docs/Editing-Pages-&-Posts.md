<!-- # Editing Pages, Posts, and Authors -->

<!-- MarkdownTOC -->

* [Markdown or HTML](#markdown-or-html)
* [How to Edit](#how-to-edit)
* [Pages](#pages)
* [Blog Posts](#blog-posts)
  * [Name & Location](#name--location)
  * [Metadata](#metadata)
  * [Post Excerpts & Read More](#post-excerpts--read-more)
* [Authors](#authors)

<!-- /MarkdownTOC -->

<a id="markdown-or-html"></a>
## Markdown or HTML

Jekyll gives you the option of writing content in either Markdown or HTML. Markdown tends to allow for a simpler writing and editing process. HTML tends to allow for more control. Often you will need to use both, to achieve a desired result. In either case, they can both utilize [Liquid Templating](Liquid-Templates.md).

If you're unfamiliar with Markdown, checkout this [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). If you're unfamiliar with HTML try poking around [HTML.com](https://html.com/) or [Tutorialspoint - HTML Tutorial](https://www.tutorialspoint.com/html/index.htm).

One thing I like about writing in HTML is that you can retain the indentation formatting a bit better. While you can use either HTML or Markdown in any given file, the way that Jekyll inteprets your file will be determined by the file extension (`.html` for HTML and `.md` `.MARKDOWN`, etc for Markdown)

<a id="how-to-edit"></a>
## How to Edit

There are various methods for editing pages and posts. You can either:

1. Edit locally with a text editor
2. Edit locally with the [Jekyll Admin](jekyll-admin) Graphical Interface
3. Edit via GitHub (Really not recommended)

See the [Tools](Tools.md) doc for more.

<a id="pages"></a>
## Pages

Pages can be located anywhere in your site's root directory or a subdirectory, ex: `/2012/02/`. At the minimum, they should contain `layout` `title` and `class` fields in their [front matter](Front-Matter-(Metadata).md). They can also include a [permalink](https://jekyllrb.com/docs/permalinks/) or other custom attributes.

Example 1 - Archive for 2012 page

```yaml
---
layout: year
permalink: /2012/
redirect_from: "/2012"
title: 2012
year: 2012
---

<h1 class="archive-title">Archive for 2012</h1>
```

* `permalink` ensures that the url will be `https://personalgenomes.org/2012/` instead of `https://personalgenomes.org/2012/index.html`
* `layout` means it will load `_layouts/year.html` and render the archive page based on that
* `year` is a custom variable that is then accessed by `_layouts/year.html` in a for loop

The beginning of the `_layouts/year.html` looks like this:

```html
{%- for post in site.posts -%}
  {%- capture postyear -%} {{ post.date | date: '%Y' }} {%- endcapture -%}
  {%- capture pageyear -%} {{ page.year }} {%- endcapture -%}
```

<a id="blog-posts"></a>
## Blog Posts

<a id="name--location"></a>
### Name & Location

All blog posts must be in the `_posts` directory (or the `_drafts` directory, if unfinished). The file names must look like `YEAR-MONTH-DAY-title.MARKUP`. Ex: `2011-12-31-new-years-eve-is-awesome.md` or `2012-09-12-how-to-write-a-blog.html`

<a id="metadata"></a>
### Metadata

At a minimum, a blog post needs the `layout` and `title` and `categories ` fields defined in its front matter. Here is a full list of useful metadata variables (with sample values), as of the time of writing:

```yaml
layout: post
title: Participant directory
date: 2012-03-07 13:59:23.000000000 -05:00
categories:
- PGP
- Tapestry
tags:
- public profiles
author: Tom Clegg
display_name: Tom Clegg
permalink: "/2012/03/07/participant-directory/"
```

Notes:
* The order of the metadata fields at the top of the file doesn't matter
* `layout` should always be `post`
* The `date` field doesn't need anything beyond `YYYY-MM-DD`, but otherwise can include the following: `YYYY-MM-DD HH:MM:SS.MS TIMEZONE-OFFSET`
* `tags` is actually useless in the current implementation of the site. This can be changed if needed, but based on the setup, it seemed redundant
* `categories` can also be specified as such: [`"Uncategorized", "PGP", "Etc"`]
  * If you're unsure what to categorize a new post as, you should set it as `["Uncategorized"]`. The site isn't currently set up to handle posts with no specified categories. Regardless: [Explicit is better than implicit](https://www.python.org/dev/peps/pep-0020/).
* The previously imported posts have a lot of extra data that was created and utilized by WordPress, but not useful in the current implementation. Feel free to ignore it

<a id="post-excerpts--read-more"></a>
### Post Excerpts & Read More

If you have a long post (or even a medium-length) post, you should
add an excerpt seperator `<!--more-->` to the post. This allows
the main blog page to display the excerpt, instead of the full post.
This saves load time and reader frustration.

You can pull the post excerpt elsewhere on the site via the `post.excerpt` tag. Example:

```html
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
```

<a id="authors"></a>
## Authors

Author files are very straightforward and should have the following front matter data:

```yaml
---
name: Hope Kroog
gravatar_name: hope
email: hope@openhumans.org
---
```

In theory, they can also have an `image` field, or other custom fields; but the site isn't currently set up to process or utilize those tags in anwyay.



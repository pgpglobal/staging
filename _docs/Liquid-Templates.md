<!-- # Liquid Templating -->

<!-- MarkdownTOC -->

* [Basics](#basics)
  * [Objects](#objects)
  * [Tags](#tags)
  * [Filters](#filters)
  * [Front Matter \(Metadata\)](#front-matter-metadata)
* [Includes](#includes)
* [Site Data](#site-data)
* [Collections](#collections)
* [Code Comments](#code-comments)
* [Links](#links)
* [Adding Element Classes and IDs](#adding-element-classes-and-ids)

<!-- /MarkdownTOC -->

Jekyll uses the [Liquid](https://shopify.github.io/liquid/) templating language to process templates.

Generally in Liquid you output content using two curly braces e.g. {{ variable }} and perform logic statements by surrounding them in a curly brace percentage sign e.g. {% if statement %}. To learn more about Liquid, check out the official Liquid Documentation.

Liquid can be used in both HTML and Markdown contexts, and there are a variety of built-in site variables to make certain tasks easier

<a id="basics"></a>
## Basics

<a id="objects"></a>
### Objects

Objects tell Liquid where to output content. They’re denoted by double curly braces: `{{` and `}}`. For example:

`{{ page.title }}`

Outputs a variable called `page.title` on the page.

<a id="tags"></a>
### Tags

TagsPermalink
Tags create the logic and control flow for templates. They are denoted by curly braces and percent signs: {% and %}. For example:

```html
{% if page.show_sidebar %}
  <div class="sidebar">
    sidebar content
  </div>
{% endif %}
```

Outputs the sidebar if `page.show_sidebar` is `true`. You can learn more about the tags available to Jekyll [here](https://jekyllrb.com/docs/liquid/tags/) or on the [Jekyll & Liquid Cheatsheet](https://gist.github.com/ryerh/b2fa73829f1b7b1c39988f09a65eb227#tags) tags section.

<a id="filters"></a>
### Filters

Filters change the output of a Liquid object. They are used within an output and are separated by a `|`. For example:

`{{ "hi" | capitalize }}`

Outputs `Hi`. You can learn more about the filters available to Jekyll [Jekyll Docs - Filters](https://jekyllrb.com/docs/liquid/filters/) or [cloudcannon - Jekyll Cheat Sheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/).

One particularly useful filter is the `sort` filter. It's currently used to create the Sidebar Archives on the blog, as well as the category pages

<a id="front-matter-metadata"></a>
### Front Matter (Metadata)

Front matter is a snippet of [YAML](http://yaml.org/) which sits between two triple-dashed lines at the top of a file. See the [Front Matter (Metadata)](Front-Matter-(Metadata).md) doc for more info.

Front matter is used to set variables for the page, for example:

```yaml
---
my_number: 5
---
```

Front matter variables are available in Liquid under the page variable. For example to output the variable above you would use:

`{{ page.my_number }}`

<a id="includes"></a>
## Includes

One of the most awesome features of Jekyll is that you can include template parts from elsewhere. This is excellent for things like Headers, sidebars, footers, Related Posts sections, etc.

If you take a look at the `_layouts/default.html` file, you'll notice the following tags are included in the code:

* {%- include_cached head.html title=page.title -%}
* {%- include_cached nav.html -%}
* {%- include_cached footer.html -%}

Note: the site uses the incredibly awesome [Jekyll Include Cache](https://github.com/benbalter/jekyll-include-cache) plugin. This saves a lot of redundant code processing at build time. Most of the include statements on the site will look like above. A notable exception is `{% include related-posts.html categories=page.categories %}`, as the suggested posts would be the same across all posts otherwise.

<a id="site-data"></a>
## Site Data

Jekyll supports loading data from YAML, JSON, and CSV files located in a `_data` directory. Data files are a great way to separate content from source code to make the site easier to maintain.

In the PGP Global site, the only data file we have is for the nav menu. In the GET Conference site, there are data files for the agendas, events, and nav menu.

The Agendas data uses subfolders. See [Jekyll Docs - Data - Subfolders](https://jekyllrb.com/docs/datafiles/#subfolders) for an overview. Otherwise, see the [GET Conference docs](https://github.com/pgpconference/pgpconference/wiki)

For examples of different nav menu configurations, see [Jekyll Tutorials - Navigation](https://jekyllrb.com/tutorials/navigation/)

Stuff about accessing Site Data https://jekyllrb.com/docs/step-by-step/06-data-files/#data-file-usage

<a id="collections"></a>
## Collections

Similar to Data are collections. These allow you to group similarly related items in their own `_collection` subdirectories. You can also specify a main `collections_dir`, in order to keep things neat and tidy. The PGP Global site collections can be found in `collections` and are currently:

* `_authors` - Author pages
* `_category` - Post Category pages
* `_news` - News items for News page
* `_projects` - Projects on the front page
* `_social-links` - the image and link attributes for the blog's sidebar links.

Collections must be defined in `_config.yml`. In addition to their names, Collections have an `output` variable.
When set to `true`, there will be a separate page generated for each file in the collection. This is how the individual Author and Category pages are created.

The `collections` section in `_config.yml` currently looks like this:

```yaml
collections:
  authors:
    output: true
  category:
    output: true
  news:
    output: false
  projects:
    output: false
  social-links:
    output: false
```

You can also add custom properties to collections as follows:

```yaml
collections:
  staff_members:
    people: true
```

Items from collections can then be accessed as follows:

```html
<div class="entries">
  <ul class="entry-list">
    {%- for author in site.authors -%}
    <li><a class="post-link" href="{{ author.url | relative_url }}">{{ author.name }}</a></li>
    {%- endfor -%}
  </ul>
</div>
```

Note: If you've written collection files in Markdown (instead of HTML), you'll have to run the content through the `| markdownify` filter

<a id="code-comments"></a>
## Code Comments

A comment block is any code between {% comment %} and {% endcomment %} tags. Note: if you put these in between If or For Loops, or if you try to have nested comments, you may run into issues.

[Add examples]

<a id="links"></a>
## Links

A Jekyll URL involves the following:
* `url` such as `personalgenomes.org`
* `baseurl` such as `/get2015`
* the rest of your link

When writing posts, there are a variety of ways to write links, depending on your needs. While you can just write out the hard link (ex: https://personalgenomeproject.com/authors/hopekroog.html), this allows errors and broken links to creep in, and is generally not recommended. The exception would be for external links to another website.

As a rule, it's almost always better to generate absolute urls like `https://personalgenomeproject.com/authors/abram_connely.html` instead of `authors/abram_connely.html`. This is both for clarity and for SEO purposes.

* Author URL: `{{ site.url }}{{ author_url | relative_url }}`
* Category URL: `{{ site.baseurl }}/category/{{ category | slugify }}`
* Normal Page: `[Privacy Policy]({{ site.url }}{{ site.baseurl }}/privacy-policy)`
* Markdown Image w/ Link: `[![image]({{ site.baseurl }}/images/category/thumb/image-1-th.jpg){: .galleryThumb}]({{ site.baseurl }}/images/category/image-1.jpg){: #galleryImage}`
* Markdown Image w/ Link: `{{ "[![Franklin Institute](assets/images/pgp-logo.png)](http://www.fi.edu/)" | markdownify | remove: '<p>' | remove: '</p>' }}`


<a id="adding-element-classes-and-ids"></a>
## Adding Element Classes and IDs

To add classes or IDs simply type any of the following before the element you wish to add the class or id to. This is useful for scripting or styling

* {:.classname} - adds a single class
* {:.class1.class2} - adds multiple classes
* {:#idname} - adds an ID

Examples:

1. H2 Element

```html
{:.paragraph-header}
## Thank You for Making 2010 a Success!

<!-- Turns into -->
<h2 class="paragraph-header">Thank You for Making 2010 a Success!</h2>
```

2. Add a Margin Class to a paragraph

```html
<!-- The .mt50 class is simply a way of adding margin-top: 50px; to a given element -->
{:.collections-tag .mt50}
Limited sponsorship opportunities are still available.<br>
For more information, please write: [jason@personalgenomes.org](mailto:jason@personalgenomes.org)

<!-- Turns into -->
<p class="mt50">Limited sponsorship opportunities are still available. <br />
For more information, please write: <a href="mailto:jason@personalgenomes.org">jason@personalgenomes.org</a></p>
```

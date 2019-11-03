<!-- # Configuring-Jekyll -->

<!-- MarkdownTOC -->

* [General Site Info](#general-site-info)
* [Minima Theme - Social Media and SEO:](#minima-theme---social-media-and-seo)
* [Jekyll SEO Tag Settings](#jekyll-seo-tag-settings)
* [Build settings](#build-settings)
* [Exclude from processing.](#exclude-from-processing)
* [Collections](#collections)

<!-- /MarkdownTOC -->

This is an explanation of the various settings found in _config.yml.

<a id="general-site-info"></a>
## General Site Info

```yaml
title: "Personal Genome Project: Global Network"
# email: your-email@example.com
description: > # this means to ignore newlines until "baseurl:"
  Write an awesome description for your new site here. You can edit this
  line in _config.yml. It will appear in your document head meta (for
  Google search results) and in your feed.xml site description.

# baseurl: "/PGPGlobal" # the subpath of your site, e.g. /blog
# url: "https://pgp.lunacodesdesign.com" # the base hostname & protocol for your site, e.g. http://example.com
```

<a id="minima-theme---social-media-and-seo"></a>
## Minima Theme - Social Media and SEO:

This site is built off of Jekyll's default theme [Minima](https://github.com/jekyll/minima). Here are some relevant options:

```yaml
twitter_username: PGorg
flickr_username: personalgenomes
# github_username:  jekyll
google_analytics: UA-145673922-1

# Block 2 - is lower down in the config file

minima:
  # refer to https://shopify.github.io/liquid/filters/date/ if you want to customize this
  # date_format: "%b %-d, %Y"

  social_links:
    twitter: pgorg
    # github:  jekyll
    facebook: PersonalGenomesOrg
    linkedin: personalgenomes-org
    youtube: PersonalGenomesOrg
    # Other options include: rss dribbble flickr instagram pinterest
    # youtube_channel youtube_channel_name telegram googleplus microdotblog

```


<a id="jekyll-seo-tag-settings"></a>
## Jekyll SEO Tag Settings

[Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md) is a very awesome plugin that auto-generates SEO info for all the site's pages

```yaml
author: "Personal Genome Project: Global Network"
logo: /assets/images/pgp-logo.png
social:
  - https://twitter.com/pgorg
  - https://www.facebook.com/groups/personalgenomes
  - https://www.linkedin.com/company/personalgenomes-org
  - https://www.youtube.com/user/PersonalGenomesOrg

twitter:
  username: pgorg
  card: summary

show_excerpts: true
excerpt_seperator: "<!--more-->"
# environment: development
```


<a id="build-settings"></a>
## Build settings

Ignore the other build settings. You'll only really need to adjust the [Plugins](Plugins.md). In the excerpt below, I have `jekyll-feed`, jekyll-seo-tag, and jekyll-sitemap disabled for local development. A good way to do this is to use a secondary config file. See [Building-&-Serving-the-Site - Secondary Config File](Building-&-Serving-the-Site#secondary-config-file.md)

```yaml
markdown: kramdown
theme: minima
plugins:
  - github-pages
  - jekyll-admin
  - jekyll-include-cache
  # - jekyll-feed
  - jekyll-redirect-from
  # - jekyll-seo-tag
  # - jekyll-sitemap
  - jekyll-titles-from-headings
```


<a id="exclude-from-processing"></a>
## Exclude from processing.
```yaml
# The following items will not be processed, by default. Create a custom list
# to override the default setting.
exclude:
#  - Gemfile
#  - Gemfile.lock
#  - vendor/bundle/
#   - vendor/cache/
#   - vendor/gems/
#   - vendor/ruby/
```

```yaml
sass:
  # style: expanded
  style: compressed
  sourcemap: always

# Post Variables to enable conditional checks such as {% if page.id %} or
# {% if page.title == "title" %}, etc
defaults:
  - scope:
      path: ""      # empty string for all files
      type: posts   # limit to posts
      type: tags
      type: categories
      type: tag
      type: category
    values:
      is_post: true # automatically set is_post=true for all posts
  - scope:
      path: ""
      type: archive
    values:
      is_archive: true
  - scope:
      path: ""
      type: category
    values:
      layout: category
      class: category body-archive
  - scope:
      path: ""
      type: "authors"
    values:
      class: "archive body-author"
      layout: "author"
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      # categories: Uncategorized
  - scope:
      path: ""
    values:
      layout: "default"
      # image: assets/images/pgp-logo.png
      image: assets/images/pgp_header_420x180.png # specified for jekyll-seo-tag purposes
```


<a id="collections"></a>
## Collections

See [Jekyll Docs - Collections]. `output: true` means that the site will generate pages for each item in the collections - perfect for Author or Category pages!!

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

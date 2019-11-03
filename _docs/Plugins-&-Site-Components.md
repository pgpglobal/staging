<!-- # Jekyll Plugins & Site Components -->

Jekyll works with plugins that handle things like Caching, Sitemaps, SEO, Redirection, etc.

<!-- MarkdownTOC -->

* [GitHub Pages](#github-pages)
* [Local Development](#local-development)
* [Jekyll Without Plugins](#jekyll-without-plugins)
* [Plugin Docs](#plugin-docs)
* [Contact Form](#contact-form)
  * [Staticman + reCAPTCHA](#staticman--recaptcha)
  * [Form Validation](#form-validation)
* [Gravatars](#gravatars)
* [Jekyll SEO Tag](#jekyll-seo-tag)
* [Simple Jekyll Search](#simple-jekyll-search)

<!-- /MarkdownTOC -->

<a id="github-pages"></a>
## GitHub Pages

GitHub Pages restricts what plugins it will allow to run. While you can run other plugins locally, their effects might not show up on GH Pages - so it's best to stick with what's on the Approved list. I've made an exception for the [jekyll-admin](https://github.com/jekyll/jekyll-admin) plugin.

GitHub Pages Default Plugins:

* jekyll-coffeescript
* jekyll-gist
* jekyll-github-metadata
* jekyll-paginate
* jekyll-relative-links
* jekyll-optional-front-matter
* jekyll-readme-index
* jekyll-default-layout
* jekyll-titles-from-headings

GitHub Pages Optional Plugins:

* jekyll-feed
* jekyll-redirect-from
* jekyll-seo-tag
* jekyll-sitemap
* jekyll-avatar
* jemoji
* jekyll-mentions
* jekyll-include-cache

<a id="local-development"></a>
## Local Development

FOr local development, you might not want to have all the plugins running, as they may slow things down. Example: there's no reason you'd need `jekyll-feed` or `jekyll-seo-tag` off. A good way to deal with this is to have an untracked secondary config file (see [Using Git](Using-Git.md)).

I'd recommend setting your local plugins in `config_dev.yml` to the following:

```yaml
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

<a id="jekyll-without-plugins"></a>
## Jekyll Without Plugins

While plugins are super useful for most things, sometimes a plugin-less solution ends up being better. For example, the Search Bar was implemented using [Simple Jekyll Search](https://github.com/christian-fei/Simple-Jekyll-Search)

<a id="plugin-docs"></a>
## Plugin Docs

Here are links to the Plugins' documentation pages

* https://github.com/jekyll/jekyll-admin
* https://github.com/jekyll/jekyll-feed
* https://github.com/benbalter/jekyll-include-cache
* https://github.com/jekyll/jekyll-redirect-from
* https://github.com/jekyll/jekyll-seo-tag
* https://github.com/jekyll/jekyll-sitemap
* https://github.com/benbalter/jekyll-titles-from-headings

<a id="contact-form"></a>
## Contact Form

The Contact Form works through a combination of
[Google Forms](https://forms.google.com), [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display), Staticman, and [Instant Form Validation](https://www.sitepoint.com/instant-validation/).

**Note:** Staticman can only run reCAPTCHA v2 and no v3.

<a id="staticman--recaptcha"></a>
### Staticman + reCAPTCHA

Instructions from [GitHub - eduardoboucas: staticman-recaptcha](https://github.com/eduardoboucas/staticman-recaptcha/)

* Note: If the Staticman [encryption endpoint](https://api.staticman.net/v2/encrypt/) doesn't work, you can also use this [RSA Encryption/Decryption](https://www.devglan.com/online-tools/rsa-encryption-decryption) tool.


After [following the steps](https://staticman.net/docs) to install Staticman, you need to integrate reCAPTCHA.

1. [Sign up](https://www.google.com/recaptcha/admin) to reCAPTCHA. You'll be assigned a *Site key* and *Secret*.

2. Encrypt the secret using Staticman's encryption endpoint:

  ```
  https://api.staticman.net/v2/encrypt/YOUR-SECRET
  ```

3. Take the site key and the encrypted secret and add a reCAPTCHA block to your Staticman config file:

```yml
reCaptcha:
  enabled: true
  siteKey: "YOUR-SITE-KEY"
  secret: "YOUR-ENCRYPTED-SECRET"
```

4. Add the reCAPTCHA credentials to your form:

```html
<input type="hidden" name="options[reCaptcha][siteKey]" value="YOUR-SITE-KEY">
<input type="hidden" name="options[reCaptcha][secret]" value="YOUR-ENCRYPTED-SECRET">
```

5. Add the reCAPTCHA script and DOM element

```html
<div class="g-recaptcha" data-sitekey="YOUR-SITE-KEY"></div>
<script src='https://www.google.com/recaptcha/api.js'></script>
```

<a id="form-validation"></a>
### Form Validation

Due to the importance of the Form Validation code, I've created a local copy at [_form-validation-tutorial](_form-validation-tutorial)

<a id="gravatars"></a>
## Gravatars

The Contributors box on the sidebar uses what's known as [Gravatar API](https://en.gravatar.com/site/implement/) (short for Global Avatar). This is a service that Automattic came up with that allows you to grab a user or author's most up-to-date avatar, instead of having to always update it manually.

This requires the following elements:

1. A post with the `author` defined
2. An individual author page in `/authors/` with the author's `email` defined
3. The code that calls the script and renders the gravatar.

works via a magical script in `scripts/gravatar.js`

Example:

1. A post with the relevant Front Matter metadata

_posts/2016-09-23-survey-about-sharing-health-data-online.html:

```yaml
---
layout: post
title: Survey about sharing health data online
date: 2016-09-23 12:35:34.000000000 -04:00
categories: ["Uncategorized"]
display_name: hk
first_name: Hope
last_name: Kroog
permalink: "/2016/09/23/survey-about-sharing-health-data-online/"
---
```

2. An Author's file with required metadata

_authors/hopekroog.md:

```yaml
---
name: Hope Kroog
gravatar_name: hope
email: hope@openhumans.org
---
```

Note: may of the author files contain the `image` and `src_original` fields. These are deprecated, and no longer necessary.

3. The code that renders the Gravatar in the Blog sidebar
_includes/sidebar.html:

```html
<div id="author_grid-2" class="widget widget_author_grid">
  <h2 class="widget-title">Contributors</h2>
  <ul>
    {% for author in site.authors %}
    {% if author.email %}
      <script>
        document.write('<li><a id="{{ author.gravatar_name }}" href="{{ site.url }}{{ site.baseurl }}{{ author.url }}">')
        document.write('<img src="' + get_gravatar('{{ author.email }}', 48) + '" alt="Author thumbnail for {{ author.name }}" class="avatar avatar-48 grav-hased" height="48" width="48" /></a></li>');
      </script>

    {% endif %}

    {% endfor%}
  </ul>
</div>
```

<a id="jekyll-seo-tag"></a>
## Jekyll SEO Tag

See [jekyll-seo-tag - Basic Usage ](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md), as well as [jekyll-seo-tag - Advanced Usage](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/advanced-usage.md) for more info

The SEO tag will respect the following YAML front matter if included in a post, page, or document:

* `title` - The title of the post, page, or document
* `description` - A short description of the page's content
* `image` - URL to an image associated with the post, page, or document (e.g., /assets/page-pic.jpg)
* `author` - Page-, post-, or document-specific author information (see Advanced usage)
* `lang` - Page-, post-, or document-specific language information

Note: Front matter defaults can be used for any of the above values as described in advanced usage with an image example.

<a id="simple-jekyll-search"></a>
## Simple Jekyll Search

Simple Jekyll Search works via a search script which parses the site data via the info stored in search.json. The script targets a specific page element via ID, and spontaneously generates and outputs the search results.

The HTML code for the Search box looks as follows:

```html
<div id="search-3" class="widget widget_search">
  <!-- HTML elements for search -->
  <h2 class="widget-title">Search</h2>

  <form class="search-form"><input type="text" id="search-input" placeholder="Search blog posts.."></form>
  <ul class="search-results" id="results-container"></ul>

  <!-- script pointing to jekyll-search.js -->
  <script src="{{ site.baseurl }}/scripts/search-script.min.js"></script>

  <!-- Configuration -->
  <script>
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search.json'
  })
  </script>
</div>
```


Examples of Simple Search's JSON file: The JSON file uses [Liquid](Liquid-Templates.md) to produce the results

Example 1 - Posts Only:

```json
---
layout: null
---
[
  {% for post in site.posts %}
    {
      "title"    : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags"     : "{{ post.tags | strip_html | strip_newlines | remove_chars | escape | join: ', ' }}",
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date }}",
      "content"  : "{{ post.content | strip_html | strip_newlines | remove_chars | escape }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```

Example 2 - Posts and Pages:

```json
---
layout: null
---
[
  {% for post in site.posts %}
    {
      "title"    : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags"     : "{{ post.tags | join: ', ' }}",
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date }}",
      "content"  : "{{ post.content | strip_html | strip_newlines }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
  ,
  {% for page in site.pages %}
   {
     {% if page.title != nil %}
        "title"    : "{{ page.title | escape }}",
        "category" : "{{ page.category }}",
        "tags"     : "{{ page.tags | join: ', ' }}",
        "url"      : "{{ site.baseurl }}{{ page.url }}",
        "date"     : "{{ page.date }}",
        "content"  : "{{ page.content | strip_html | strip_newlines }}"
     {% endif %}
   } {% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```

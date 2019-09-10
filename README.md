# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions and Documentation](#instructions-and-documentation)
* [Blog Import](#blog-import)
  * [Archive Pages](#archive-pages)
  * [Sidebar Functionality](#sidebar-functionality)
  * [Captions and Shortcodes](#captions-and-shortcodes)
  * [Post Footer](#post-footer)
* [Styling and Markup adjustments](#styling-and-markup-adjustments)
  * [Medium-Large Tasks](#medium-large-tasks)
  * [Small Tasks](#small-tasks)
    * [Content Needed](#content-needed)
* [Plugins and Configuration](#plugins-and-configuration)
    * [Plugins Staging](#plugins-staging)
    * [Plugins - Local Dev](#plugins---local-dev)
* [Accessibility](#accessibility)
* [Staging and Production](#staging-and-production)
  * [SSL and CDN](#ssl-and-cdn)
  * [SCSS](#scss)
  * [Favicon](#favicon)
* [Questions](#questions)
* [Deprecated](#deprecated)

<!-- /MarkdownTOC -->

<a id="instructions-and-documentation"></a>
## Instructions and Documentation

See A current list of documentation files includes:
* [Documentation](docs/documentation.md) - general documentation
* [Resources](docs/resources.md) - a list of various resources related to in-progress tasks

<a id="blog-import"></a>
## Blog Import

<a id="archive-pages"></a>
### Archive Pages

1. Not currently working, due to GitHub Pages restrictions.
    * Working on a Python or possibly ruby script to address this
    * Do this in Ruby instead though
2. Author Archives not currently working
    * Blog Post links need to be generated
    * Maybe this is related to include_cached??

<a id="sidebar-functionality"></a>
### Sidebar Functionality

1. Flickr needs to be dynamic. Options
    * Get URLs of last 3 and then follow the normal embed method
      * Cache these
    * Parsing RSS Feed seems like the best bet: https://api.flickr.com/services/feeds/photos_public.gne?id=78213110@N06&lang=en-us&format=rss_200
    * See [resources][1]
2. Search Form needs to point to this site - not the old WP blog

<a id="captions-and-shortcodes"></a>
### Captions and Shortcodes

1. Shortcodes need to be replaced with actual code wherever possible. See [here](http://localhost:4000/2012/11/27/wildlife-of-our-homes-q-a-with-rob-dunn/) for an example.
    * `[caption]` covers 21 posts. I can't say for other shortcodes without manually looking through posts.
    * `[youtube]` covers 8 posts
    * `[polldaddy]`covers 1 posts

<a id="post-footer"></a>
### Post Footer

1. Nav links need to become dynamic

<a id="styling-and-markup-adjustments"></a>
## Styling and Markup adjustments

<a id="medium-large-tasks"></a>
### Medium-Large Tasks

1. Blog articles check typography
2. Mobile Sidebar - Social Icons should be less to the right
3. Preference: `_media.css`: convert max-width: 767 into relevant min-width sections, if time-possible (non-essential).

<a id="small-tasks"></a>
### Small Tasks

1. Blog - Social Icons sidebar gets pushed to new line btwn 768-830px
2. Main Page - change `<button> a:hover` color to match original
3. Replace all fixed line heights w/ relative numbers
  * Using a single variable wherever possible
4. Archive pages - Post `<li>` needs background color change on hover
5. Desktop - Fix Nav Menu dropdown color
6. Blog/Archive: `.entries span`  needs more specificity (due to text-align)

<a id="content-needed"></a>
#### Content Needed
1. Site Footer - what goes in it?
    * Possible options: Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance.

```
or us, -- @Sasha, @Edrie @Jeremy @Ward we should make sure we do the correct CCbySA or whatever we want to do to do a correct open copyright for the copyright since it says Copyright © 2019 Personal Genome Project: Global Network
```

2. Contact Page
    * Contact Form vs. Link
    * If contact form - how will the back-end work?
    * I noticed the PGP Conference site just had a normal Google form, instead of the way I'm trying to embed it
        * May be a more straightforward approach, if it turns out that the issue isn't SSL/staging related
3. `_config.yml` - the following fields should be filled in or commented out:
    * email
    * description (important for SEO)
    * any social media we might link to (currently have twitter and flickr)

<a id="plugins-and-configuration"></a>
## Plugins and Configuration
1. SEO setup
    * Need to add email, site description, etc to `_config.yml`
2. Contact Page
    * Choose back-end and implement spam protection (either reCaptcha or other). Possible options:
3. Responsive Images. See [Resources][1] file. Currently attempting to get the [jekyll-picture-tag](https://github.com/robwierzbowski/jekyll-picture-tag) plugin working.
4. Blog comments system
5. Generate favicon files using [Real Favicon Generator](https://realfavicongenerator.net/)

<a id="plugins-staging"></a>
#### Plugins Staging

* "jekyll-feed", "~> 0.6" (why is this versioned?)
* jekyll-seo-tag
* jekyll-sitemap
* jekyll-titles-from-headings


<a id="plugins---local-dev"></a>
#### Plugins - Local Dev

* jekyll-admin
* jekyll-autoprefixer

<a id="accessibility"></a>
## Accessibility

1. Add ARIA Roles into HTML where necessary, across site

<a id="staging-and-production"></a>
## Staging and Production

<a id="ssl-and-cdn"></a>
### SSL and CDN

1. Setup SSL and Test [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https) (this means everything that loads on the page has to start with `https://` instead of `http://`)
      * Cloudflare is probably the most optimal route here. See [Resources][1] file.
2. [Setting up GitHub Pages locally](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll#keeping-your-site-up-to-date-with-the-github-pages-gem)

<a id="scss"></a>
### SCSS

1. Make sure to change `$baseurl` in SCSS for production
    * There should be a way to do this dynamically

<a id="favicon"></a>
### Favicon

1. Run [Favicon Checker](https://realfavicongenerator.net/) once the subdomain is set up

<a id="questions"></a>
## Questions

1. Cloudflare - is the current site hooked up with Cloudflare? the new site will have to be, due to the fact that it's a custom domain. So being setup with Cloudflare already might save some headache.
2. What's the story with comments?
3. Search Form?
4. Contact Form?

<a id="deprecated"></a>
## Deprecated

Comments System (see question above)
~1. Either needs plugin(s) or embedding of Disqus or some other similar thing~


[1]: docs/resources.md


-------------

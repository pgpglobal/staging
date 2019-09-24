# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions and Documentation](#instructions-and-documentation)
* [Footer](#footer)
* [Styles](#styles)
* [Blog Import](#blog-import)
  * [Related Posts](#related-posts)
  * [Categories](#categories)
* [Styling and Markup adjustments \(non-essential\)](#styling-and-markup-adjustments-non-essential)
  * [Small Tasks](#small-tasks)
* [Content Needed](#content-needed)
  * [Site Footer - Copyright and Privacy Info](#site-footer---copyright-and-privacy-info)
* [Plugins and Configuration](#plugins-and-configuration)
    * [Plugins Staging](#plugins-staging)
    * [Plugins - Local Dev](#plugins---local-dev)
* [Accessibility](#accessibility)
* [Cleanup](#cleanup)
* [Staging and Production](#staging-and-production)
  * [Domain & Subdomain Setup](#domain--subdomain-setup)
  * [Favicon](#favicon)
* [Notes](#notes)
  * [Deprecated](#deprecated)
  * [Captions and Shortcodes](#captions-and-shortcodes)

<!-- /MarkdownTOC -->

<a id="instructions-and-documentation"></a>
## Instructions and Documentation

See A current list of documentation files includes:
* [Documentation](docs/documentation.md) - general documentation
* [Resources](docs/resources.md) - a list of various resources related to in-progress tasks

<a id="footer"></a>
## Footer

* Add Privacy Policy and ToS

<a id="styles"></a>
## Styles

* Move styles out of _media.scss
* Setup Autoprefixer

<a id="blog-import"></a>
## Blog Import

<a id="related-posts"></a>
### Related Posts

1. Randomize posts displayed from each tag, if possible
    * Will only work if I write a plugin

<a id="categories"></a>
### Categories

1. Sidebar and Top Nav spacing are slightly off - why??

<a id="styling-and-markup-adjustments-non-essential"></a>
## Styling and Markup adjustments (non-essential)

1. Preference: `_media.css`: convert max-width: 767 into relevant min-width sections, if time-possible (non-essential).
2. 1. Replace all fixed line heights w/ relative numbers
* Using a base SCSS variable wherever possible

<a id="small-tasks"></a>
### Small Tasks

<a id="content-needed"></a>
## Content Needed

<a id="site-footer---copyright-and-privacy-info"></a>
### Site Footer - Copyright and Privacy Info
1. Site Footer - what goes in it?
    * Possible options: Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance.
2. `_config.yml` - the following fields should be filled in or commented out:
    * email
    * description (important for SEO)
    * any social media we might link to (currently have twitter and flickr)

<a id="plugins-and-configuration"></a>
## Plugins and Configuration
1. SEO setup
    * Need to add email, site description, etc to `_config.yml`
2. Responsive Images. See [Resources][1] file. Currently attempting to get the [jekyll-picture-tag](https://github.com/robwierzbowski/jekyll-picture-tag) plugin working.

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

<a id="cleanup"></a>
## Cleanup

* Replace SCSS Media Queries with name variables?
* Replace max-width queries w/ min-width queries
* Why is get2016 folder present in PGP Site?
* Remove `archives.py` when it's 100% clear it's unnecessary
* `_archive.scss` - `.entries` duplicates

<a id="staging-and-production"></a>
## Staging and Production

<a id="domain--subdomain-setup"></a>
### Domain & Subdomain Setup

1. Note that current website seems to prefer `www` over Apex domain.

<a id="favicon"></a>
### Favicon

1. Run [Favicon Checker](https://realfavicongenerator.net/) once the subdomain is set up

<a id="notes"></a>
## Notes

<a id="deprecated"></a>
### Deprecated

~~1. Reinstate the /updates.html et al links that go to [sign-up form](https://personalgenomes.us3.list-manage.com/subscribe?u=3980aaa2746fd428de44b2ab4&id=34d31b2d4b) and similar~~
    * ~~Setup JS redirect via layout or include or something~~
    * ~~use jekyll-redirect to do this possibly?~~
    * Not finding the where/what of this. Not terribly significant in the first place

<a id="captions-and-shortcodes"></a>
### Captions and Shortcodes

1. Shortcodes need to be replaced with actual code wherever possible. See [here](http://localhost:4000/2012/11/27/wildlife-of-our-homes-q-a-with-rob-dunn/) for an example.
    * `[caption]` covers 21 posts. I can't say for other shortcodes without manually looking through posts.
    * `[youtube]` covers 8 posts
    * `[polldaddy]`covers 1 posts

[1]: docs/resources.md

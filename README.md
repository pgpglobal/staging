# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions and Documentation](#instructions-and-documentation)
* [Questions & Content Needed](#questions--content-needed)
  * [SEO - Webmaster Verifications](#seo---webmaster-verifications)
* [Absolute vs Relative URLs](#absolute-vs-relative-urls)
  * [Nav Alignment & Logo Distorting](#nav-alignment--logo-distorting)
* [Blog Import](#blog-import)
  * [Header Image](#header-image)
* [Styling, Markup, and Image adjustments \(non-essential\)](#styling-markup-and-image-adjustments-non-essential)
* [Plugins and Configuration](#plugins-and-configuration)
    * [Plugins Staging](#plugins-staging)
    * [Plugins - Local Dev](#plugins---local-dev)
* [Accessibility](#accessibility)
* [Cleanup](#cleanup)
* [Staging and Production](#staging-and-production)
  * [SEO & Webmaster Tools](#seo--webmaster-tools)
  * [Domain & Subdomain Setup](#domain--subdomain-setup)
  * [Favicon](#favicon)
* [Notes](#notes)
  * [Styles & Vendor Prefixes](#styles--vendor-prefixes)
  * [Captions and Shortcodes](#captions-and-shortcodes)
  * [Deprecated](#deprecated)

<!-- /MarkdownTOC -->

<a id="instructions-and-documentation"></a>
## Instructions and Documentation

See A current list of documentation files includes:
* [Documentation](docs/documentation.md) - general documentation
* [Resources](docs/resources.md) - a list of various resources related to in-progress tasks

<a id="questions--content-needed"></a>
## Questions & Content Needed

<a id="seo---webmaster-verifications"></a>
### SEO - Webmaster Verifications

Good idea to verify with Google Webmaster Tools, etc if not already. Sample config values for `jekyll-seo-tag`:

```yaml
# Just Google
google_site_verification

# Multiple Services
webmaster_verifications:
  google: 1234
  bing: 1234
  alexa: 1234
  yandex: 1234
  baidu: 1234
```

2. What's the correct Facebook link?


<a id="absolute-vs-relative-urls"></a>
## Absolute vs Relative URLs

* Convert relative urls to absolute urls wherever relevant

<a id="nav-alignment--logo-distorting"></a>
### Nav Alignment & Logo Distorting

1. News page is currently off w/ Nav Alignment
    * Home page nav alignment is currently fine
2. Sarah mentioned the Logo looked distorted
    * Seems to be a result of the weird `margin-left: -15px; margin-right: -15px;` setting on `.row` classes

<a id="blog-import"></a>
## Blog Import

<a id="header-image"></a>
### Header Image

1. Crop Header Image (non-essential)

<a id="styling-markup-and-image-adjustments-non-essential"></a>
## Styling, Markup, and Image adjustments (non-essential)

1. Preference: `_media.css`: convert max-width: 767 into relevant min-width sections, if time-possible (non-essential).
2. Replace all fixed line heights w/ relative numbers
    * Using a base SCSS variable wherever possible
3. Month Archives: 425px, 768px - would be nice to tweak the styles a bit, so the Archive Title doesn't split into the next line

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
    * Nav menu

<a id="cleanup"></a>
## Cleanup

* Replace SCSS Media Queries with name variables?
* Replace max-width queries w/ min-width queries
* Remove `archives.py` when it's 100% clear it's unnecessary
  * Doublecheck that running `_plugins/luna_archives_generator.rb` manually is sufficient
  * A Rakefile might be a good way to du this
* `_archive.scss` - `.entries` duplicates
* Verify if `prefixfree.js` is actually doing anything? (It's not breaking anything)
* Figure out what's necessary/relevant of the `defaults` values in `_config.yml`

<a id="staging-and-production"></a>
## Staging and Production

<a id="seo--webmaster-tools"></a>
### SEO & Webmaster Tools

1. Verify with various Webmaster tools
2. Test with Google's [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool/u/0/)
    * See [Google Developers - Understand how structured data works](https://developers.google.com/search/docs/guides/intro-structured-data)

<a id="domain--subdomain-setup"></a>
### Domain & Subdomain Setup

1. Note that current website seems to prefer `www` over Apex domain.

<a id="favicon"></a>
### Favicon

Should be all set - but can run [Favicon Checker](https://realfavicongenerator.net/) another time, once the subdomain is set up

<a id="notes"></a>
## Notes

<a id="styles--vendor-prefixes"></a>
### Styles & Vendor Prefixes

* If there are any issues with `prefixfree.js`, then it may be worth looking into `modernizr.js` - this would be more appropriate for the next iteration of the site

<a id="captions-and-shortcodes"></a>
### Captions and Shortcodes

1. Shortcodes need to be replaced with actual code wherever possible. See [here](http://localhost:4000/2012/11/27/wildlife-of-our-homes-q-a-with-rob-dunn/) for an example.
    * `[caption]` covers 21 posts. I can't say for other shortcodes without manually looking through posts.
    * `[youtube]` covers 8 posts
    * `[polldaddy]`covers 1 posts

<a id="deprecated"></a>
### Deprecated

~~1. Reinstate the /updates.html et al links that go to [sign-up form](https://personalgenomes.us3.list-manage.com/subscribe?u=3980aaa2746fd428de44b2ab4&id=34d31b2d4b) and similar~~
    * ~~Setup JS redirect via layout or include or something~~
    * ~~use jekyll-redirect to do this possibly?~~
    * Not finding the where/what of this. Not terribly significant in the first place


[1]: docs/resources.md

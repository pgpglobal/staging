# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions and Documentation](#instructions-and-documentation)
* [Questions & Content Needed](#questions--content-needed)
  * [SEO - Webmaster Verifications](#seo---webmaster-verifications)
* [Absolute vs Relative URLs](#absolute-vs-relative-urls)
  * [Nav Alignment & Logo Distorting](#nav-alignment--logo-distorting)
    * [Plugins Staging & Production](#plugins-staging--production)
    * [Plugins - Local Dev](#plugins---local-dev)
* [Blog](#blog)
  * [Excerpts](#excerpts)
  * [Post Footer](#post-footer)
* [Accessibility](#accessibility)
* [Cleanup](#cleanup)
  * [SCSS \(extra/non-essential\)](#scss-extranon-essential)
* [Staging and Production](#staging-and-production)
  * [Google Analytics](#google-analytics)
  * [Optimization](#optimization)
    * [Images](#images)
    * [CDN - Cloudflare](#cdn---cloudflare)
  * [SEO & Webmaster Tools](#seo--webmaster-tools)
  * [Domain & Subdomain Setup](#domain--subdomain-setup)
  * [Favicon](#favicon)
  * [Contact Form](#contact-form)
* [Notes](#notes)
  * [Captions and Shortcodes](#captions-and-shortcodes)
  * [Deprecated](#deprecated)

<!-- /MarkdownTOC -->

<a id="instructions-and-documentation"></a>
## Instructions and Documentation

Instructions and documentation can be found at the [PGP Global WIki](https://github.com/pgpglobal/PGPGlobal/wiki). If this is missing locally, then run `git pull --recurse-submodules`

Currently in progress - writing documentation for workflow, snippets, notes about site structure, editing, etc.

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

2. What's the correct Facebook link? `https://facebook.com/PersonalGenomesOrg` results in a 404/Page Not Found.

<a id="absolute-vs-relative-urls"></a>
## Absolute vs Relative URLs

* Finishing replacing relative URLs where relevant
  * See [CDN - Cloudflare](#cdn---cloudflare) section regarding performance

<a id="nav-alignment--logo-distorting"></a>
### Nav Alignment & Logo Distorting

1. News page is currently off w/ Nav Alignment
    * Home page nav alignment is currently fine
2. Sarah mentioned the Logo looked distorted
    * Seems to be a result of the weird `margin-left: -15px; margin-right: -15px;` setting on `.row` classes

<a id="plugins-staging--production"></a>
#### Plugins Staging & Production

These are a list of the plugins enabled in `_config.yml` that will run on production

* jekyll-admin (only runs locally - not on GH Pages)
* jekyll-include-cache
* jekyll-feed
* github-pages
* jekyll-seo-tag
* jekyll-redirect-from
* jekyll-sitemap
* jekyll-titles-from-headings

<a id="plugins---local-dev"></a>
#### Plugins - Local Dev

This is a paired down list, since the others eat up unnecessary build resource and slow down editing and working on the site.

* jekyll-admin - useful for editing posts. Won't run on GH Pages
* jekyll-include-cache
* github-pages
* jekyll-redirect-from
* jekyll-titles-from-headings

<a id="blog"></a>
## Blog

<a id="excerpts"></a>
### Excerpts
The following posts would benefit from `<!--more-->` tags

* 2015/11/03/joining-as-a-pgp-volunteer/
* 2015/08/31/the-2015-harvard-pgp-conference/
* 2015/05/05/oppenheimer-foundation-survey-results/
* 2015/03/06/video-sporty-genomes-are-elite-athletes-born-or-made/
* 2015/02/19/what-are-you-looking-for-in-your-genome-and-how-can-we-help-you-find-it/
* 2014/12/18/pgp-harvard-updates-including-a-new-real-name-option/
* **2014/08/18/pgp-harvard-blood-collection-event-boston-sept-20-saturday/**
* 2014/01/14/open-humans-network-wins-knight-news-challenge-health-award/
* 2013/11/21/pgp-comments-on-genomic-data-sharing-policy/
* 2013/02/25/trait-survey-data-download-and-analysis/
* 2012/12/14/pgp-forum-and-wiki/
* 2012/12/09/personal-genome-project-canada-launches/
* 2012/12/06/presentation-on-pgp-to-the-duke-university-school-of-medicine-class-of-1972/
* 2012/11/30/american-gut-qa-with-jeff-leach/
* 2012/11/29/seeking-diversity/
* 2012/10/01/vistas-and-hazards-of-the-foggy-omic-road/
* 2012/08/01/the-predominant-variant-of-the-app-gene-greatly-increases-risk-for-alzheimers-disease-and-cognitive-decline/
* 2012/07/14/a-public-resource-facilitating-clinical-use-of-genomes/
* 2012/05/14/improved-enrollment-exam-pgp-study-guide/
* 2012/05/03/pgp18-a-23andme-exome/
* 2012/02/29/invulnerability-to-stomach-flu-is-my-secret-superpower/
* **2012/02/08/its-a-boy-or-how-i-learned-to-stop-worrying-and-love-direct-to-consumer-genomics/**
*

<a id="post-footer"></a>
### Post Footer

Prev and Next links have `/category/` attached to them for no reason...

<a id="accessibility"></a>
## Accessibility

1. Add ARIA Roles into HTML where necessary, across site
    * Nav menu

<a id="cleanup"></a>
## Cleanup

* Remove `archives.py` when it's 100% clear it's unnecessary
  * Doublecheck that running `_plugins/luna_archives_generator.rb` manually is sufficient
  * A Rakefile might be a good way to save the trouble of running it manually
* Figure out what's necessary/relevant from the `defaults` settings in `_config.yml`

<a id="scss-extranon-essential"></a>
### SCSS (extra/non-essential)

1. Replace all fixed line heights w/ relative numbers
    * Using a base SCSS variable wherever possible
2. Month Archives: 425px, 768px - would be nice to tweak the styles a bit, so the Archive Title doesn't split into the next line


<a id="staging-and-production"></a>
## Staging and Production

* Run staging site through a broken links checker

<a id="google-analytics"></a>
### Google Analytics

Change Google Analytics code in `head.html` to read:

```html
{%- if jekyll.environment == 'production' and site.google_analytics -%}
  {%- if site.url contains "personalgenomes" -%}
  {%- include google-analytics.html -%}
  {%- endif -%}
{%- endif -%}
```

<a id="optimization"></a>
### Optimization

<a id="images"></a>
#### Images

1. Figure out how to Lazy Load images for blog posts
2. Compress images
3. Find a way to generate and serve device-appropriate source-sets

<a id="cdn---cloudflare"></a>
#### CDN - Cloudflare

* For performance reasons, I'd advise setting up the website with Cloudflare.
    * This will allow for the use of absolute urls (helpful for SEO and general nav, imo) without a substantial performance hit.
    * Currently when using absolute urls instead of relative urls, the difference is very noticeable
* The main issue is the main page of the Blog.
    * Other (not mutually exclusive) solutions may involve Lazy Loading images or adding post excerpts.

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

* Should be all set - but can run [Favicon Checker](https://realfavicongenerator.net/) another time, once the subdomain is set up

<a id="contact-form"></a>
### Contact Form

* Double-check Contact Form just to be on the safe side

<a id="notes"></a>
## Notes

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
* Not finding the where/what of this. It was a minor concern in the first place.


[1]: docs/resources.md

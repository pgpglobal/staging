# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions and Documentation](#instructions-and-documentation)
* [Contact Form](#contact-form)
* [Styles](#styles)
* [Blog Import](#blog-import)
  * [Related Posts](#related-posts)
* [Styling and Markup adjustments](#styling-and-markup-adjustments)
  * [Medium-Large Tasks](#medium-large-tasks)
  * [Small Tasks](#small-tasks)
* [Content Needed](#content-needed)
  * [Site Footer - Copyright and Privacy Info](#site-footer---copyright-and-privacy-info)
* [Plugins and Configuration](#plugins-and-configuration)
  * [Archive Generator and Plugin](#archive-generator-and-plugin)
    * [Plugins Staging](#plugins-staging)
    * [Plugins - Local Dev](#plugins---local-dev)
* [Accessibility](#accessibility)
* [Cleanup](#cleanup)
  * [Authors](#authors)
  * [Git Branches](#git-branches)
* [Staging and Production](#staging-and-production)
  * [Archives Generation](#archives-generation)
  * [SSL](#ssl)
  * [SCSS](#scss)
  * [Favicon](#favicon)
* [Notes](#notes)
  * [Captions and Shortcodes](#captions-and-shortcodes)
  * [Category and Tag Pages](#category-and-tag-pages)

<!-- /MarkdownTOC -->

<a id="instructions-and-documentation"></a>
## Instructions and Documentation

See A current list of documentation files includes:
* [Documentation](docs/documentation.md) - general documentation
* [Resources](docs/resources.md) - a list of various resources related to in-progress tasks

<a id="contact-form"></a>
## Contact Form

* Styling - Should I make the Message field always be the same width as the others??

<a id="styles"></a>
## Styles

* Move styles out of _media.scss

<a id="blog-import"></a>
## Blog Import

<a id="related-posts"></a>
### Related Posts

1. Randomize posts displayed from each tag, if possible
    * Will only work if I write a plugin

<a id="styling-and-markup-adjustments"></a>
## Styling and Markup adjustments

<a id="medium-large-tasks"></a>
### Medium-Large Tasks

1. Preference: `_media.css`: convert max-width: 767 into relevant min-width sections, if time-possible (non-essential).

<a id="small-tasks"></a>
### Small Tasks

1. Reinstate the /updates.html et al links that go to [sign-up form](https://personalgenomes.us3.list-manage.com/subscribe?u=3980aaa2746fd428de44b2ab4&id=34d31b2d4b) and similar
  * Setup JS redirect via layout or include or something
  * use jekyll-redirect to do this possibly?

Optional:
1. Replace all fixed line heights w/ relative numbers
* Using a base SCSS variable wherever possible

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

<a id="archive-generator-and-plugin"></a>
### Archive Generator and Plugin

1. Either convert the `archives.py` file to a Ruby file, or find a way to make a Ruby or gulp file that runs it locally.

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

List of files:

* `scripts/gravatar.js` seems to be generating the gravatars.
    * If so, then delete `_plugins/to_gravatar.rb`
* Replace SCSS Media Queries with name variables

<a id="authors"></a>
### Authors

The `display_name` attribute in the Author files doesn't match anything in the actual posts... either replace with display name from posts, or just delete in all files

<a id="git-branches"></a>
### Git Branches

* Delete extra Git Branches

<a id="staging-and-production"></a>
## Staging and Production

<a id="archives-generation"></a>
### Archives Generation

Make sure Archive generation doesn't mess with staging setup

<a id="ssl"></a>
### SSL

1. Note that current website seems to prefer `www` over Apex domain.

<a id="scss"></a>
### SCSS

1. Make sure to change `$baseurl` in SCSS for production
    * There should be a way to do this dynamically

<a id="favicon"></a>
### Favicon

1. Run [Favicon Checker](https://realfavicongenerator.net/) once the subdomain is set up

<a id="notes"></a>
## Notes

<a id="captions-and-shortcodes"></a>
### Captions and Shortcodes

1. Shortcodes need to be replaced with actual code wherever possible. See [here](http://localhost:4000/2012/11/27/wildlife-of-our-homes-q-a-with-rob-dunn/) for an example.
    * `[caption]` covers 21 posts. I can't say for other shortcodes without manually looking through posts.
    * `[youtube]` covers 8 posts
    * `[polldaddy]`covers 1 posts

<a id="category-and-tag-pages"></a>
### Category and Tag Pages

1. I only set up Category archives, since none of the posts have Tag info and Jekyll mostly treats them the same

[1]: docs/resources.md

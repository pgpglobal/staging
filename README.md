# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions](#instructions)
  * [Setup](#setup)
  * [Keeping Up-To-Date](#keeping-up-to-date)
  * [Working on the Site](#working-on-the-site)
* [Documentation](#documentation)
* [Remaining Development Tasks](#remaining-development-tasks)
  * [Blog Import](#blog-import)
    * [Sidebar Functionality](#sidebar-functionality)
    * [Archive and Author Pages](#archive-and-author-pages)
    * [Captions and Shortcodes](#captions-and-shortcodes)
  * [General](#general)
    * [Styling and Markup adjustments](#styling-and-markup-adjustments)
    * [Content Needed](#content-needed)
  * [Plugins and Configuration](#plugins-and-configuration)
  * [Accessibility](#accessibility)
* [Staging and Production](#staging-and-production)
* [Completed](#completed)
* [Questions](#questions)
* [Deprecated](#deprecated)

<!-- /MarkdownTOC -->

<a id="instructions"></a>
## Instructions

<a id="setup"></a>
### Setup

In order to run this site locally, follow the following steps:

1. Download and install [Ruby](https://www.ruby-lang.org/en/downloads/) v. 2.4.0 or higher. See [Ruby Docs - Installation](https://www.ruby-lang.org/en/documentation/installation/) for more info.
    * If there's an option to install with developer kit, I recommend doing so.
2. Install [RubyGems](https://rubygems.org/pages/download)
3. Install [GCC](https://gcc.gnu.org/install/) and [Make](https://www.gnu.org/software/make/)
4. Download and install [Jekyll](https://jekyllrb.com/). In terminal: `gem install bundler jekyll`
    * See [Jekyll Docs - Installation](https://jekyllrb.com/docs/installation/#requirements) for more detailed, OS-specific instructions, as well as system requirements.
5. Download and install [Git](https://git-scm.com/downloads)
6. Download or clone this repo. In the terminal, this is done by typing `git clone https://github.com/lunacodes/PGPGlobal.git`
7. Navigate to the directory that was just created (PGPGlobal by default, unless you gave it a custom name)
8. Terminal: `bundle exec jekyll serve`
    * In the future, you can simply run `jekyll serve`, however you may need to run `bundle exec jekyll serve` and/or `bundle install` when new plugins or other elements are added to the site.

<a id="keeping-up-to-date"></a>
### Keeping Up-To-Date

In order to keep the site up-to-date with future changes, you should run `git pull` in your terminal.

<a id="working-on-the-site"></a>
### Working on the Site

See the [Docs](docs/documentation) page.

<a id="documentation"></a>
## Documentation

I've started writing up some [documentation](docs/documentation.md). Please let me know specific questions or topics, and I'll add those in.

A current list of documentation files includes:
* [Documentation](docs/documentation.md) - general documentation
* [Resources](docs/resources.md) - a list of various resources related to in-progress tasks

<a id="remaining-development-tasks"></a>
## Remaining Development Tasks

<a id="blog-import"></a>
### Blog Import

<a id="sidebar-functionality"></a>
#### Sidebar Functionality

1. Archive Months List needs to become dynamic
2. Flickr needs to be dynamic. Options
    * Get URLs of last 3 and then follow the normal embed method
      * Cache these
    * Parsing RSS Feed seems like the best bet: https://api.flickr.com/services/feeds/photos_public.gne?id=78213110@N06&lang=en-us&format=rss_200
    * See [resources][1]
3. Search form needs to be functional

<a id="archive-and-author-pages"></a>
#### Archive and Author Pages

1. Category pages aren't working. Unsure why - tags work fine.

<a id="captions-and-shortcodes"></a>
#### Captions and Shortcodes

1. Shortcodes need to be replaced with actual code wherever possible. See [here](http://localhost:4000/2012/11/27/wildlife-of-our-homes-q-a-with-rob-dunn/) for an example.
    * For `[caption]` this covers 21 posts. I can't say for other shortcodes without manually looking through posts.

<a id="general"></a>
### General

<a id="styling-and-markup-adjustments"></a>
#### Styling and Markup adjustments
1. Change all .date to time.dt-published
    * Figure out styles for date + author on blog posts
2. Blog articles check typography
3. Blog - Social Icons sidebar gets pushed to new line btwn 768-830px
4. Main Page - change `<button> a:hover` color to match original
5. Replace all fixed line heights w/ standard numbers
6. Archive pages - Post `<li>` needs background color change on hover
7. Desktop - Fix Nav Menu dropdown color
8. Minor: `_media.css`: convert max-width: 767 into relevant min-width sections, if time-possible (non-essential).

<a id="content-needed"></a>
#### Content Needed
1. Site Footer - what goes in it?
    * Possible options: Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance.
2. Contact Page
    * Contact Form vs. Link
    * If contact form - how will the back-end work?
3. `_config.yml` - the following fields should be filled in or commented out:
    * email
    * description (important for SEO)
    * any social media we might link to (currently have twitter and flickr)

<a id="plugins-and-configuration"></a>
### Plugins and Configuration
1. SEO setup
    * Need to add email, site description, etc to `_config.yml`
2. Configure il8n (internationalization)
3. Contact Page
    * Choose back-end and implement spam protection (either reCaptcha or other). Possible options:
4. Responsive Images. See [Resources][1] file. Currently attempting to get the [jekyll-picture-tag](https://github.com/robwierzbowski/jekyll-picture-tag) plugin working.
5. Blog comments system
6. Generate favicon files using [Real Favicon Generator](https://realfavicongenerator.net/)

<a id="accessibility"></a>
### Accessibility

1. Add ARIA Roles into HTML where necessary, across site

<a id="staging-and-production"></a>
## Staging and Production

1. Setup SSL and Test [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https) (this means everything that loads on the page has to start with `https://` instead of `http://`)
      * Cloudflare is probably the most optimal route here. See [Resources][1] file.
2. [Setting up GitHub Pages locally](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll#keeping-your-site-up-to-date-with-the-github-pages-gem)

<a id="completed"></a>
## Completed
* Moved News section to its own page
* Fixed 404 Page header
* Nav Menu logic for seperator and dropdown-header added in
* Split the "International Projects" section into a jekyll collection of markdown files (similar to News files)?
* Added alt text to pgp-logo.png
* Retrieved missing Blog images
* Refactored SCSS code
* Created auto-generated Author pages
* Fixed private Author Metadata displaying in post header
* Sidebar and Main layouts on blog, archive, and author pages
* Google Analytics
* Gravatar links dynamic
* Author/Archive layouts default, month, day, category, tag
* Related Posts
* Blog Share buttons

<a id="questions"></a>
## Questions

1. Cloudflare - is the current site hooked up with Cloudflare? the new site will have to be, due to the fact that it's a custom domain. So being setup with Cloudflare already might save some headache.
2. I noticed that comments were turned off on the old blog anyway. Can I assume that this means we won't be needing comments on here either?

<a id="deprecated"></a>
## Deprecated

Comments System (see question above)
~1. Either needs plugin(s) or embedding of Disqus or some other similar thing~


[1]: docs/resources.md

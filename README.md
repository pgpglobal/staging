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
    * [Missing Images](#missing-images)
    * [Styles and Appearance](#styles-and-appearance)
    * [Sidebar Functionality](#sidebar-functionality)
    * [Archive Pages](#archive-pages)
  * [Plugins and Configuration](#plugins-and-configuration)
  * [Accessibility](#accessibility)
* [Staging](#staging)
* [Production](#production)
* [Completed](#completed)
  * [Completed - Production](#completed---production)
* [Miscellaneous & Questions](#miscellaneous--questions)

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
    * In the future, you can simply run `jekyll serve`, however you may need to run `bundle exec jekyll serve` when new plugins or other elements are added to the site.

<a id="keeping-up-to-date"></a>
### Keeping Up-To-Date

In order to keep the site up-to-date with future changes, you should run `git pull` in your terminal.

<a id="working-on-the-site"></a>
### Working on the Site

See the [Docs](docs/documentation) page.

<a id="documentation"></a>
## Documentation

I've started writing up some [documentation](docs/documentation.md). Please let me know specific questions or topics, and I'll add those in.


<a id="remaining-development-tasks"></a>
## Remaining Development Tasks

<a id="blog-import"></a>
### Blog Import

<a id="missing-images"></a>
#### Missing Images

List of images that I was unable to import (which need to be found individually from original blog) include:
* 14008052589_c3c301f8d6_z.jpg
* porsche_drives.jpg
* genom-austria-logo.png
* blut-edta.jpg
* getlabs2014_booklet.jpg
* getlabs2014_stamps.jpg
* knight.png
* fny_gv_logo_bold_line.png
* new_personalgenomesorg_website.png
* get_logo.jpg
* get2013_groupshot_6858-2.jpg
* circles_in_human_evolution2.jpg
* hela_cells_stained_with_hoechst_33258.jpg
* 20130208_misha_2.jpg
* help_wanted_gottgraphicsdesign_flickr.jpg
* headshot.jpeg
* microbiome_kits_processing_2012-06-11_13-07-20_594.jpg
* badge_genomicarts.jpg
* saliva_freezer.jpg
* lauerman_blood_draw2.jpg
* 20120120_x_inheritance.png
* 20120121_x_inheritance_2.png

<a id="styles-and-appearance"></a>
#### Styles and Appearance

The following need more styling:

1. Main page
2. Archive pages

<a id="sidebar-functionality"></a>
#### Sidebar Functionality

1. List Archive pages
2. Flickr options (username: personalgenomes)
    * Get URLs of last 3 and then follow the normal embed method
      * Cache these
    * Parsing RSS Feed seems like the best bet: https://api.flickr.com/services/feeds/photos_public.gne?id=78213110@N06&lang=en-us&format=rss_200
    * [Jekyll and responsive Flickr photos](https://heipei.io/2016/05/28/jekyll-and-responsive-flickr-photos/)
    * [Keith Marran - Integrating Flickr and Jekyll](http://www.marran.com/tech/integrating-flickr-and-jekyll) - has useful info on caching

<a id="archive-pages"></a>
#### Archive Pages

1. Need layouts for month, day, year, category, tag
  * May be able to cover these all with the default layout


1. Pull in blog posts from the former [PGP WordPress blog](https://personalgenomes.wordpress.com/)
    * Working on a technical glitch with this
2. Responsive Styling tweaks (mostly done)
3. Site Footer
    * Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance.
4. Contact Page content and styling

<a id="plugins-and-configuration"></a>
### Plugins and Configuration
1. Configure SEO Plugin(s) and setup
    * Need to add email, site description, etc to `_config.yml`
2. Configure il8n (internationalization)
3. Contact Page
    * Choose back-end and implement spam protection (either reCaptcha or other). Possible options:
        * [Brisk Forms](https://www.briskforms.com/)
        * [Formspree](https://formspree.io/)
        * Google Forms
    * Tweak open/close animation on mobile menu
4. Responsive Images

<a id="accessibility"></a>
### Accessibility

1. Add ARIA Roles into HTML where necessary, across site

<a id="staging"></a>
## Staging

1. Test [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https)

<a id="production"></a>
## Production

1. Setup SSL/HTTPS. Steps:
  * Set custom domain on GitHub repo. See [here](https://help.github.com/en/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site)
  * Create A records pointing to [GitHub's servers](https://help.github.com/en/articles/setting-up-an-apex-domain#configuring-a-records-with-your-dns-provider)
    * 185.199.108.153
    * 185.199.109.153
    * 185.199.110.153
    * 185.199.111.153
  * Remove and re-add custom domain on GitHub account to trigger the process of enabling HTTPS.
  * [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https) (this means everything that loads on the page has to start with https instead of http)

<a id="completed"></a>
## Completed
* Moved News section to its own page
* Fixed 404 Page header
* Nav Menu logic for seperator and dropdown-header added in
* Split the "International Projects" section into a jekyll collection of markdown files (similar to News files)?
* Added alt text to pgp-logo.png

<a id="completed---production"></a>
### Completed - Production
* Google Analytics

<a id="miscellaneous--questions"></a>
## Miscellaneous & Questions
1. Blog Twitter Feed - Are the pictures and spacing ok? (these are twitter defaults)
    * Should I limit it to 3 tweets instead?

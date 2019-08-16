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
      * [General](#general)
    * [Styles and Appearance](#styles-and-appearance)
    * [Sidebar Functionality](#sidebar-functionality)
    * [Archive and Author Pages](#archive-and-author-pages)
  * [General](#general-1)
    * [Content Needed](#content-needed)
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


<a id="remaining-development-tasks"></a>
## Remaining Development Tasks

<a id="blog-import"></a>
### Blog Import

<a id="general"></a>
##### General

1. Spacing between <main> and sidebar is too wide, relative to previous
2. Needs Responsive Design
3. Change <li> elements to <article> elements
4. Seperate sidebar SCSS into separate file
5. Need to grab styles for blog posts from old site

<a id="styles-and-appearance"></a>
#### Styles and Appearance

1. Change all .date to time.dt-published
    * Figure out styles for date + author on blog posts
    * Make sure single blog displays full month name, not 3 letter abbreviation
2. Main Page - fix button styles... they're picking up the blog by accident
3. Replace all fixed line heights w/ standard numbers
The following need more styling:
4. Archive pages - Post <li> needs background color change on hover
5. Fix Nav Menu Colors
6. Refactor _blog.scss - probably split into_
7. _media.css convert max-width: 767 into relevant min-width sections, if time-possible
8. Blog articles check typography

<a id="sidebar-functionality"></a>
#### Sidebar Functionality

1. Archive Months List needs to become dynamic
2. Flickr options (username: personalgenomes)
    * Get URLs of last 3 and then follow the normal embed method
      * Cache these
    * Parsing RSS Feed seems like the best bet: https://api.flickr.com/services/feeds/photos_public.gne?id=78213110@N06&lang=en-us&format=rss_200
    * [Jekyll and responsive Flickr photos](https://heipei.io/2016/05/28/jekyll-and-responsive-flickr-photos/)
    * [Keith Marran - Integrating Flickr and Jekyll](http://www.marran.com/tech/integrating-flickr-and-jekyll) - has useful info on caching

<a id="archive-and-author-pages"></a>
#### Archive and Author Pages

1. Need layouts for month, day, year, category, tag
    * May be able to cover these all with the default layout
2. Individual authors need Author pages. Guides:
    * [Jekyll Docs - Collections](https://jekyllrb.com/docs/step-by-step/09-collections/)
    * [CodepediaOrg - How to handle multiple authors in Jekyll](https://www.codepedia.org/ama/how-to-handle-multiple-authors-in-jekyll/)
3. Change all absolute links to relative links

<a id="general-1"></a>
### General
1. Responsive Styling tweaks (mostly done)

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
1. Configure SEO Plugin(s) and setup
    * Need to add email, site description, etc to `_config.yml`
2. Configure il8n (internationalization)
3. Contact Page
    * Choose back-end and implement spam protection (either reCaptcha or other). Possible options:
        * [Brisk Forms](https://www.briskforms.com/)
        * [Formspree](https://formspree.io/)
        * Google Forms
    * Relevant Tutorials and Resources
        * https://github.com/toperkin/staticformemails
        * https://blog.webjeda.com/jekyll-contact-form/
        * https://bbc.github.io/a11y-tutorials/forms/
4. Responsive Images
    * [Responsive Images in Jekyll without a plugin](https://benseymour.com/2017/03/02/Responsive-Images-in-Jekyll-without-a-plugin)
5. Blog comments system
6. Generate favicon using [Real Favicon Generator](https://realfavicongenerator.net/)
    * [How do I get Jekyll to copy favicons from a subdirectory to root when publishing?](https://stackoverflow.com/questions/52223620/how-do-i-get-jekyll-to-copy-favicons-from-a-subdirectory-to-root-when-publishing)
7.

<a id="accessibility"></a>
### Accessibility

1. Add ARIA Roles into HTML where necessary, across site

<a id="staging"></a>
## Staging

1. Test [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https)
    * [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https) (this means everything that loads on the page has to start with https instead of http)
      * Cloudflare may be necessary see:
      * [Secure and fast GitHub Pages with CloudFlare](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/)
      * [How to setup a static website using GitHub Pages and Cloudflare with your own Domain Name](https://www.codementor.io/landonpatmore/how-to-setup-a-static-website-using-github-pages-and-cloudflare-with-your-own-domain-name-jb99nbuoe)
      * [How to Deploy Websites on Custom Domains using Cloudflare and Github Pages](https://medium.com/crowdbotics/annie-azana-how-to-deploy-websites-using-cloudflare-and-github-pages-c415c55fea36)
2. [Setting up GitHub Pages locally](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll#keeping-your-site-up-to-date-with-the-github-pages-gem)

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


<a id="completed"></a>
## Completed
* Moved News section to its own page
* Fixed 404 Page header
* Nav Menu logic for seperator and dropdown-header added in
* Split the "International Projects" section into a jekyll collection of markdown files (similar to News files)?
* Added alt text to pgp-logo.png
* Retrieved missing Blog images

<a id="completed---production"></a>
### Completed - Production
* Google Analytics

<a id="miscellaneous--questions"></a>
## Miscellaneous & Questions
1. Blog Twitter Feed - Are the pictures and spacing ok? (these are twitter defaults)
    * Should I limit it to 3 tweets instead?

# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

<!-- MarkdownTOC -->

* [Instructions](#instructions)
  * [Setup](#setup)
  * [Keeping Up-To-Date](#keeping-up-to-date)
  * [Working on the Site](#working-on-the-site)
* [Remaining Tasks](#remaining-tasks)
  * [Development](#development)
  * [Staging](#staging)
  * [Production](#production)
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

<a id="remaining-tasks"></a>
## Remaining Tasks

<a id="development"></a>
### Development

1. Responsive Styling tweaks
2. Configure SEO
3. Configure il8n (internationalization)
4. Update content/copy for Contact page and Footer.
    * Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance
5. ~Move News section to its own page~
6. Pull in blog posts from the former [PGP WordPress blog](https://personalgenomes.wordpress.com/)
7. Google Analytics
8. Create documentation for file structure, update and editing procedures, etc
10. Add Email and Site Description to `_config.yml` (Site description is helpful for SEO)_
11. Contact Page
  * Choose back-end and implement spam protection (either reCaptcha or other). Options:
    * [Brisk Forms](https://www.briskforms.com/)
    * [Formspree](https://formspree.io/)
    * Google Forms
  * Style contact form
12. Nav Menu - add logic for the "Project Websites" item to function as a section header, and not a link
  * Tweak open/close animation on mobile menu
13. ~~Fix 404 Page header~~
14. Swap CDN versions of bootstrap et al. for local versions
15. Break International Projects section into a jekyll collection?

<a id="staging"></a>
### Staging

1. Test [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https)

<a id="production"></a>
### Production

1. Setup SSL/HTTPS. Steps:
  * Set custom domain on GitHub repo. See [here](https://help.github.com/en/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site)
  * Create A records pointing to [GitHub's servers](https://help.github.com/en/articles/setting-up-an-apex-domain#configuring-a-records-with-your-dns-provider)
    * 185.199.108.153
    * 185.199.109.153
    * 185.199.110.153
    * 185.199.111.153
  * Remove and re-add custom domain on GitHub account to trigger the process of enabling HTTPS.
  * [Enforce HTTPS](https://help.github.com/en/articles/securing-your-github-pages-site-with-https) (this means everything that loads on the page has to start with https instead of http)

1.
<a id="miscellaneous--questions"></a>
## Miscellaneous & Questions

1. News Page - should 2018 items have the same line break as all the other years?

# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

## Instructions

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

<!-- ### Modifying

Make a bran
 -->
### Keeping Up-To-Date

In order to keep the site up-to-date with future changes, you should run `git pull` in your terminal. Note: If you've made local changes, this task me be a bit more complicated.

## Remaining Tasks:

1. Responsive Styling tweaks
    * Add Back to Top button for mobile
2. Implement custom domain for production environment
3. Configure SEO
3. Configure il8n (internationalization)
4. Update copy for Contact page and Footer.
    * Licensing, Copyright, and possibly Privacy Policy, if relevant for [EU GDPR](https://eugdpr.org/) compliance
5. Move News section to its own page
6. Pull in blog posts from the former [PGP WordPress blog](https://personalgenomes.wordpress.com/)
7. Google Analytics
8. Create documentation for file structure, update and editing procedures, etc
9. Setup SSL/HTTPS
10. Add Email and Site Description to `_config.yml` (Site description is helpful for SEO)_
11. Contact Page
  * Choose back-end and implement spam protection (either reCaptcha or other).
  * Style contact form
12. Nav Menu - add logic for the "Project Websites" item to function as a section header, and not a link
  * Fix open/close animation on mobile menu
13. 404 Page header needs fixing
14. News Page - should 2018 items have the same line break as all the other years?

# Personal Genome Project: Global Network (Jekyll)

This is the repo for the rewrite of the [PGP Global](https://www.personalgenomes.org/) website

## Instructions

In order to run this site locally, follow the following steps:

1. Download and install [Ruby](https://www.ruby-lang.org/en/downloads/) v. 2.4.0 or higher. See [Ruby Docs - Installation](https://www.ruby-lang.org/en/documentation/installation/) for more info.
    * If there's an option to install with developer kit, I recommend doing so.
2. Install [RubyGems](https://rubygems.org/pages/download)
3. Install [GCC](https://gcc.gnu.org/install/) and [Make](https://www.gnu.org/software/make/)
4. Download and install [Jekyll](https://jekyllrb.com/). In terminal: `gem install bundler jekyll`
    * See [Jekyll Docs - Installation](https://jekyllrb.com/docs/installation/#requirements) for more detailed, OS-specific instructions, as well as system requirements.
5. Download or clone this repo. In the terminal, this is done by typing `git clone https://github.com/lunacodes/PGPGlobal.git`
6. Navigate to the directory that was just created (PGPGlobal by default, unless you gave it a custom name)
7. Terminal: `bundle exec jekyll serve`
    * In the future, you can simply run `jekyll serve`, however you may need to run `bundle exec jekyll serve` when new plugins or other elements are added to the site.

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

# Resources

<!-- MarkdownTOC -->

* [Jekyll & Liquid](#jekyll--liquid)
* [Author Collections](#author-collections)
* [Flickr Integration](#flickr-integration)
* [Plugins](#plugins)
* [Contact Form](#contact-form)
* [Responsive Images](#responsive-images)
* [Favicon](#favicon)
* [SSL Setup](#ssl-setup)
  * [Cloudflare](#cloudflare)
  * [GitHub Pages](#github-pages)
* [Staging - Simulating GitHub Pages](#staging---simulating-github-pages)
* [Other Tools](#other-tools)

<!-- /MarkdownTOC -->


This is primarily a list of resources for Luna, related to various remaining or in-progress tasks.

<a id="jekyll--liquid"></a>
## Jekyll & Liquid

* [Shopify - Liquid Docs](https://shopify.github.io/liquid/filters/date/)
  * [Array Filters](https://help.shopify.com/en/themes/liquid/filters/array-filters)
* [Jekyll Cheatsheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/)
* [Jekyll Documentation Theme - YAML tutorial in the context of Jekyll](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_yaml_tutorial)

<a id="author-collections"></a>
## Author Collections

* [Jekyll Docs - Collections](https://jekyllrb.com/docs/step-by-step/09-collections/)
* [CodepediaOrg - How to handle multiple authors in Jekyll](https://www.codepedia.org/ama/how-to-handle-multiple-authors-in-jekyll/)

<a id="flickr-integration"></a>
## Flickr Integration

* [Jekyll and responsive Flickr photos](https://heipei.io/2016/05/28/jekyll-and-responsive-flickr-photos/)
* [Keith Marran - Integrating Flickr and Jekyll](http://www.marran.com/tech/integrating-flickr-and-jekyll) - has useful info on caching

<a id="plugins"></a>
## Plugins

GitHub Pages Default Plugins:

* jekyll-coffeescript
* jekyll-gist
* jekyll-github-metadata
* jekyll-paginate
* jekyll-relative-links
* jekyll-optional-front-matter
* jekyll-readme-index
* jekyll-default-layout
* jekyll-titles-from-headings

GitHub Pages Optional Plugins:

* jekyll-feed
* jekyll-redirect-from
* jekyll-seo-tag
* jekyll-sitemap
* jekyll-avatar
* jemoji
* jekyll-mentions
* jekyll-include-cache

<a id="contact-form"></a>
## Contact Form

Possible Options:

* [Brisk Forms](https://www.briskforms.com/)
* [Formspree](https://formspree.io/)
* Google Forms

Relevant Tutorials and Resources:

* https://github.com/toperkin/staticformemails
* https://blog.webjeda.com/jekyll-contact-form/
* https://bbc.github.io/a11y-tutorials/forms/

<a id="responsive-images"></a>
## Responsive Images

* [Responsive Images in Jekyll without a plugin](https://benseymour.com/2017/03/02/Responsive-Images-in-Jekyll-without-a-plugin)
* [Designing responsive image layouts with Jekyll](https://www.lizheidner.com/front-end/responsive-images/)

<a id="favicon"></a>
## Favicon

* [Real Favicon Generator](https://realfavicongenerator.net/)
* [How do I get Jekyll to copy favicons from a subdirectory to root when publishing?](https://stackoverflow.com/questions/52223620/how-do-i-get-jekyll-to-copy-favicons-from-a-subdirectory-to-root-when-publishing)

<a id="ssl-setup"></a>
## SSL Setup

<a id="cloudflare"></a>
### Cloudflare

* [Secure and fast GitHub Pages with CloudFlare](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/)
* [How to setup a static website using GitHub Pages and Cloudflare with your own Domain Name](https://www.codementor.io/landonpatmore/how-to-setup-a-static-website-using-github-pages-and-cloudflare-with-your-own-domain-name-jb99nbuoe)
* [How to Deploy Websites on Custom Domains using Cloudflare and Github Pages](https://medium.com/crowdbotics/annie-azana-how-to-deploy-websites-using-cloudflare-and-github-pages-c415c55fea36)

<a id="github-pages"></a>
### GitHub Pages

* Set custom domain on GitHub repo. See [here](https://help.github.com/en/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site)
* Create A records pointing to [GitHub's servers](https://help.github.com/en/articles/setting-up-an-apex-domain#configuring-a-records-with-your-dns-provider)
  * 185.199.108.153
  * 185.199.109.153
  * 185.199.110.153
  * 185.199.111.153
* Remove and re-add custom domain on GitHub account to trigger the process of enabling HTTPS.

<a id="staging---simulating-github-pages"></a>
## Staging - Simulating GitHub Pages

* [Setting up GitHub Pages locally](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll#keeping-your-site-up-to-date-with-the-github-pages-gem)

<a id="other-tools"></a>
## Other Tools

* [HTML to Markdown Converter](https://www.browserling.com/tools/html-to-markdown)
* [Creating An Asset Pipeline In Python With-paver](https://www.codementor.io/jstacoder/creating-an-asset-pipeline-in-python-with-paver-du107wjs3)
* [How To Run Bash Commands In-gulp](https://stackoverflow.com/questions/21128812/how-to-run-bash-commands-in-gulp)
* [jekyl-tidy](https://github.com/apsislabs/jekyll-tidy) - HTMLTidy

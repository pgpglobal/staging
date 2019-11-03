<!-- # Miscellaneous -->

This is a scratch list of things that are in-progress, will get incorporated into other sections of the docs, or that otherwise don't fit elsewhere.

## Favicon

Generate and test Favicons using [Real Favicon Generator](https://realfavicongenerator.net/).

## Optimization

* compress.html layout

## Other

* Add docs for mobile-friendly Nav Menu

## SCSS - Main File & Source Maps & Overrides and Stuff

* https://jekyllrb.com/docs/step-by-step/07-assets/
* Main File
* Source Maps
* SCSS
* Bootstrap
* Font Awesome
* Possibly base future versions on https://github.com/plusjade/jekyll-bootstrap


## Assets

Using CSS, JS, images and other assets is straightforward with Jekyll. Place them in your root site folder and they’ll copy across to the built site. The default location for them is in the `assets` directory, but you can put them anywhere that doesn't have a `_` in front of it.

Currently the Assets structure looks like this:

assets/
├── fonts
└── images

## Link Structures

<li><a class="post-link" href="{{ author.url | relative_url }}">{{ author.name }}</a></li>

## Jekyll Environments

Add about Production vs Dev vs Other environments

## Cool Wiki Markup

> [[Wiki|Home]] ▸ [RC Resources](https://github.com/recursecenter/wiki/wiki#rc-resources) ▸ **Advice on finding housing in New York**

## Include Relative
https://jekyllrb.com/docs/includes/#including-files-relative-to-another-file


<a id="jekyll-seo-tag"></a>
### jekyll-seo-tag

See [jekyll-seo-tag - Basic Usage ](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md), as well as [jekyll-seo-tag - Advanced Usage](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/advanced-usage.md) for more info

The SEO tag will respect the following YAML front matter if included in a post, page, or document:

* `title` - The title of the post, page, or document
* `description` - A short description of the page's content
* `image` - URL to an image associated with the post, page, or document (e.g., /assets/page-pic.jpg)
* `author` - Page-, post-, or document-specific author information (see Advanced usage)
* `lang` - Page-, post-, or document-specific language information

Note: Front matter defaults can be used for any of the above values as described in advanced usage with an image example.


<a id="git-techniques"></a>
## Git Techniques

* Track a branch via `git branch -u branchname`


## Other

* What files correspond to what templates?
* Archive Generation instructions

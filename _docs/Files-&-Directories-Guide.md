<!-- # Files and Directories -->

<!-- MarkdownTOC -->

* [General Overview](#general-overview)
* [Directories List](#directories-list)
  * [Directories Explanation](#directories-explanation)
  * [Files](#files)
    * [Scripts](#scripts)
  * [SASS \(Styling the Site\)](#sass-styling-the-site)

<!-- /MarkdownTOC -->

<a id="general-overview"></a>
## General Overview

Most of these should be pretty self explanatory. You'll notice that many of the files are in Markdown. Jekyll magically builds these files into the html files in the `_site` directory. If you want to exclude a file (say for example the readme or docs files), go to the `exclude` section of `_config.yml`.

**Data**

Right now the only file in `_data` is `navigation.yml`. This allows you to modify the main nav menu, and could also be used to create additional menus.

**Layouts**

The html files in the `_layouts` directory allow you to create custom templates for different page/post types.
  * Right now almost everything is using the `default.html` layout.
  * A cool feature of layouts is that they can extend other layouts. Pretty much all of the layouts currently inherit the `default.html` layout - as it sets the basic scaffolding for the pages on the site.

**Includes**

The `_includes` directory contains the various building blocks of the site (such as page head, footer, header and nav menu, etc).
* `head.html` is where all the javascript and css files are loaded, as well as where SEO and other relevant info is traditionally defined (though that's mostly being handled by jekyll plugins in our case)
* `footer` and `nav.html` are exactly what they sound like. There isn't a separate header file, since the header essentially is the nav menu.

**Posts**

Posts must be named in `yyyy-mm-dd-postname.md` format (otherwise Jekyll will ignore them). Additionally, there is a variety of metadata that posts can have - which we can make use of via Jekyll's `Liquid` templating language. See the [Liquid](#liquid) section for more info.

<a id="directories-list"></a>
## Directories List

As of 10/31/19 the directory structure is as follows:

```bash
├── _data
├── _drafts
├── _includes
├── _layouts
├── _plugins
├── _posts
├── _sass
│   └── partials
├── _site
├── 2012
├── 2013
├── 2014
├── 2015
├── 2016
├── assets
│   ├── fonts
│   └── images
├── collections
│   ├── _authors
│   ├── _category
│   ├── _news
│   ├── _projects
│   └── _social-links
├── docs
├── favicon
├── scripts
├── styles
└── webfonts


# Important files
├── _config.yml
├── Gemfile
```

<a id="directories-explanation"></a>
### Directories Explanation

* `assets` is where media files such as images, videos, etc live
* `collections` contains the various collections directories
  * `_authors` contains the files for the Contributors sidebar
  * `_category` contains the files with the metadata for the main Category page
  * `_news` contains the files for the `News` page. Each year has been seperated into its own markdown file.
  * `_projects` contains the project listings used on the Homepage
  * `_social-links` contains the social media images and links for the blog sidebar
  * `_posts` and `_drafts` have also been moved to here
* `_data` contains `navigation.yml`. This is where you edit the nav menu
* `_docs` contains all the documentation for the repo
  * Note: this is managed in the Wiki Repo
* `_drafts` is for any incomplete blog posts
  * Moved to `_collections`
* `favicon` contains relevant files for the favicon
* `_includes` contains template files for things like the header, footer, nav menu, etc. These can be mixed in with differen layouts.
* `_layouts`
* `_plugins` contains the archives generator. Not terribly useful otherwise
* `_posts` contains all the blog posts from.
  * Moved to `collections`
* `_sass` is where the styles for the site live. Sass ([Syntactically Awesome Style Sheets](https://sass-lang.com/)) is a pre-processor for CSS.  The central file is `minima.scss`, and the actual code is found in the various files in the `partials` directory. See below for more info.
* `_site` is the compiled version of the site. You can basically ignore this. Always make sure this is listed in your `.gitignore` file. You *do not* want to commit this to the repo.
* `scripts` contains javascript files essential for different site features
* `styles` contains any extra styles that needed to be incorporated, such as [Bootstrap](https://getbootstrap.com/) or other css files that are loaded separately from the main scss files
* `webfonts` contains the font files used by FontAwesome (important for Mobile Menu and possible other icons)
* `2012-2016` auto-generated archive folders and files.

<a id="files"></a>
### Files

Mechanical Files:

* `.gitignore` tells Git what to ignore. This is great if you have local files or folders that are helpful for you, but not relevant to anyone else. (ex: I have a `scratch` directory where I keep code snippets or unidentified miscellaneous code)
* `_config.yml` contains various settings for things like: site info, plugins, collections, and backend configuration
* `Gemfile` manages packages, plugins, and Ruby "gems"
  * There is an accompanying `Gemfile.lock`. Ignore this file, unless you know that you know for sure that you need to edit it.


<a id="scripts"></a>
#### Scripts

* `form-validate.js` and `form-validate.min.js` validates the Contact Form (double check which is actually running)
* `gravatar.js` - fetches the Gravatar images for the Contributors sidebar
* `prefixtree.js` or `prefixtree.min.js` - auto-prefixes the rendered CSS code, for compatibility with older browsers
* `search-script.min.js - powers the search bar`

<a id="sass-styling-the-site"></a>
### SASS (Styling the Site)

Under Construction

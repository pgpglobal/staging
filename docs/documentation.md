# PGP Website Documentation

<!-- MarkdownTOC -->

* [Last Updated](#last-updated)
* [Working on the Site Locally with Git](#working-on-the-site-locally-with-git)
  * [Branching](#branching)
  * [Solving Merge Conflicts](#solving-merge-conflicts)
* [Jekyll Admin Graphical Editor](#jekyll-admin-graphical-editor)
* [Files and Directories Guide](#files-and-directories-guide)
  * [Directories](#directories)
  * [Files](#files)
* [Permalinks](#permalinks)
  * [Archives](#archives)
* [Coding in Jekyll](#coding-in-jekyll)
  * [Liquid](#liquid)

<!-- /MarkdownTOC -->

<a id="last-updated"></a>
## Last Updated

This Documentation was last updated on 8/13/2019.

<a id="working-on-the-site-locally-with-git"></a>
## Working on the Site Locally with Git

1. Always run `git pull origin master` before doing any local work. This pulls any changes other people made from the online repo, and then updates your local files. If you forget to do this, you will get merge conflicts. Merge conflicts are a headache. See [Solving Merge Conflicts](#merge-conflicts) section below.

<a id="branching"></a>
### Branching

If you're making more complex edits (say updating layouts or scss files), then your best bet is to create and work off of a branch. Follow the procedure below:

1. Type `git branch` to view whatever current branches are on your local repo
2. Type `git branch some_name` to make a new branch
3. Type `git checkout branch_name` to switch to the branch
4. Make your changes.

From here there are two routes:

1. Update via a pull request

Type `git push origin branch_name` to push your branch to the remote repo. Then [create a pull request](https://help.github.com/en/articles/creating-a-pull-request) for whoever's maintaining the repo to approve and merge your files. For an overview on pull requests, see [here](https://help.github.com/en/articles/about-pull-requests)

2. Merge the branches locally and then push to the remote repo.

Steps:

1. Type `git checkout master` to return to the main branch
2. Run `git pull origin master` to get the latest changes from the online repo
3. Type `git merge branch_name`
4. If there were no merge conflicts, then you can push to the remote repo via `git push origin master`. Otherwise, see [Solving Merge Conflicts](#merge-conflicts)

If you run into trouble with push to the remote repo, this may involve some not so simple troubleshooting. More to come on that later.

<a id="solving-merge-conflicts"></a>
### Solving Merge Conflicts

Coming Soon

<a id="jekyll-admin-graphical-editor"></a>
## Jekyll Admin Graphical Editor

A visual interface powered by [Jekyll Admin](https://github.com/jekyll/jekyll-admin) is available for editing the site. Access it by appending `/admin` to the site url, ex: `localhost:4000/admin`

<a id="files-and-directories-guide"></a>
## Files and Directories Guide

As of 8/31/19, the directory structure looks like this.

```bash
├── assets
├── _data
├── _drafts
├── _includes
├── _layouts
├── _news
├── _posts
├── _sass
│   └── partials
├── _site
│   ├── about
│   ├── assets
│   │   └── images
│   ├── blog
│   ├── contact
│   ├── docs
│   ├── news
│   └── styles
├── assets
│   └── images
├── docs
├── ref
├── scratch
└── styles

# Important files
├── _config.yml
├── Gemfile
```

<a id="directories"></a>
### Directories

* `assets` is where media files such as images, videos, etc live
* `_data` contains `navigation.yml`. This is where you edit the nav menu
* `_docs` contains all the documentation for the repo
* `_drafts` is for any incomplete blog posts
* `_includes` contains template files for things like the header, footer, nav menu, etc. These can be mixed in with differen layouts.
* `_news` contains the files for the `News` page. Each year has been seperated into its own markdown file.
* `_posts` contains all the blog posts from. These have not been included in the site just yet, due to an importation glitch I'm working out.
* `_sass` is where the styles for the site live. Sass ([Syntactically Awesome Style Sheets](https://sass-lang.com/)) is a pre-processor for CSS.  The central file is `minima.scss`, and the actual code is found in the various files in the `partials` directory. See below for more info.
* `_site` is the compiled version of the site. You can basically ignore this. Always make sure this is listed in your `.gitignore` file. You *do not* want to commit this to the repo.
* `styles` contains any extra styles that needed to be incorporated, such as [Bootstrap](https://getbootstrap.com/) or other css files that are loaded separately from the main scss files

<a id="files"></a>
### Files

Mechanical Files:

* `.gitignore` tells Git what to ignore. This is great if you have local files or folders that are helpful for you, but not relevant to anyone else. (ex: I have a `scratch` directory where I keep code snippets or unidentified miscellaneous code)
* `_config.yml` contains various settings for things like: site info, plugins, collections, and backend configuration
* `Gemfile` manages packages, plugins, and Ruby "gems"
  * There is an accompanying `Gemfile.lock`. Ignore this file, unless you know that you know for sure that you need to edit it.
*

Site Files:

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

<a id="permalinks"></a>
## Permalinks

<a id="archives"></a>
### Archives

Archive permalinks work as follows:
url.com/YYYY
url.com/YYYY/MM
url.com/YYYY/MM/DD
url.com/tag/tag_name
url.com/category/category_name


<a id="coding-in-jekyll"></a>
## Coding in Jekyll

<a id="liquid"></a>
### Liquid

Coming Soon

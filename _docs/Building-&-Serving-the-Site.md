<!-- # Using the Command Line -->

<!-- MarkdownTOC -->

* [Secondary Config File](#secondary-config-file)
* [Basic Commands](#basic-commands)
* [Command-Line-Options](#command-line-options)
  * [Build Commands](#build-commands)
  * [Serve Commands](#serve-commands)

<!-- /MarkdownTOC -->

The heart of Jekyll is in the command line. Here is some background and some useful options.


<a id="secondary-config-file"></a>
## Secondary Config File

Sometimes when developing locally you'll want to use a second
config file to specify things like the `url`, `baseurl`, `plugins`, etc.
If this is the case, simply type `bundle exec jekyll serve --config _config.yml _config_local.yml`, etc as necessary.

This is especially useful if you want to disable plugins to speed up your build time. Anything you put in your second config file will override the settings in the first.

<a id="basic-commands"></a>
## Basic Commands

Here is a list of the main Jekyll commands you'll need in the terminal.
You can find a full list at [Jekyll Docs - Command Line Usage](https://jekyllrb.com/docs/usage/).
Note: You should always run these commands using bundler (ex: `bundle exec jekyll serve`)

* `jekyll build` or `jekyll b` - Performs a one off build your site to `./_site` (by default)
* `jekyll serve` or `jekyll s` - Builds your site any time a source file changes and serves it locally
* `jekyll clean` - Removes all generated files: destination folder, metadata file, Sass and Jekyll caches.
`jekyll help` - Shows help, optionally for a given subcommand, e.g. jekyll help build

Typically you’ll use jekyll serve while developing locally and
jekyll build when you need to generate the site for production.
You won't really have to worry about using `jekyll build` much though,
as GitHub Pages will build the site for you.

**Note:** `_config.yml` is not reloaded automatically when using `bundle exec jekyll serve`. You'll need to kill the server process (Ctrl-C on Windows) and then restart it.

<a id="command-line-options"></a>
## Command-Line-Options

These can make your life easier while you're editing locally

<a id="build-commands"></a>
### Build Commands

Note: Running `bundle exec jekyll serve` will trigger an initial site build.
To skip this, add `--skip-initial-build` to your command (see [Serve Commands](###Serve Commands) for more)

For a full list see here: https://jekyllrb.com/docs/configuration/options/#build-command-options

--limit-posts

<a id="serve-commands"></a>
### Serve Commands

**Note:** `_config.yml` is not reloaded automatically when using `bundle exec jekyll serve`. You'll need to kill the server process (Ctrl-C on Windows) and then restart it.

For a full list, see [Jekyll Serve Options](https://jekyllrb.com/docs/configuration/options/#serve-command-options)

* --port
* --baseurl
* --limit-posts - You usually ddon't need Jekyll to regenerate every single post each time you press save. This will save you lots of time.
* --livereload - Reload a page automatically on the browser when its content is edited.
* --skip-initial-build

Usage Examples:

```bash
bundle exec jekyll serve --port 6000 # runs site at localhost:6000 instead of the default localhost:4000
bundle exec jekyll serve --baseurl pgpglobal # main site address will be localhost:4000/pgpglobal/
bundle exec jekyll serve --limit-posts 10 # Only rended 10 of the site's posts
bundle exec jekyll serve --livereload
bundle exec jekyll serve --skip-initial-build
```

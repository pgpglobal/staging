# Bash Aliases

<!-- MarkdownTOC -->

* [Jekyll](#jekyll)
  * [Build](#build)
  * [Serve](#serve)
  * [Troubleshoot/Clean](#troubleshootclean)
* [Git Aliases](#git-aliases)

<!-- /MarkdownTOC -->

Aliases can make your life in the terminal easier, by saving you from
always having to retype and remember long commands. These will work for any *nix system (Linux, Mac OS, Git Bash, etc).
The simplest way to set these up is to add them to
a `.bashrc` or `.bash_profile` file in your home directory.
Note: You'll need to have hidden files enabled in order to see said file.

<a id="jekyll"></a>
## Jekyll

<a id="build"></a>
### Build

```bash
alias jbuild='bundle exec jekyll build'
alias jblocal='bundle exec jekyll build --config "_config.yml,_config_dev.yml"'
alias jbstage='bundle exec jekyll build --config "_config.yml,_config_staging_remote.yml"'
alias jbstglocal='bundle exec jekyll build --config "_config.yml,_config_staging_local.yml"'
```

<a id="serve"></a>
### Serve

```bash
alias jsrv='bundle exec jekyll serve'
alias jsdev='bundle exec jekyll serve --config "_config.yml,_config_dev.yml"'
alias jstg='bundle exec jekyll serve --config "_config.yml,_config_staging_remote.yml"'
alias jstglocal='bundle exec jekyll serve --config "_config.yml,_config_staging_local.yml"'
```

<a id="troubleshootclean"></a>
### Troubleshoot/Clean

```bash
alias jclean='bundle exec jekyll clean'
```

<a id="git-aliases"></a>
## Git Aliases

There are endless variations of Git Aliases out there. These are some aliases you'll likely find useful.

```bash

# General
alias gc='git commit -v' # -v means a verbose commit log
alias gca='git commit -v -a' # commit all verbose
alias gcam='git commit -v -am' commit all verbose, specify message in terminal (instead of text editor)

alias gcl='git clone'

alias gco='git checkout' # checkout a branch
alias gcom='git checkout master' # checkout master branch
alias gcours='git checkout --ours' # checkout local version of file
alias gctheirs='git checkout --theirs' # checkout remote version of file

alias gd='git diff'
alias gdom='git diff master origin/master' # See changes btwn  current branch and master
alias gdomn='git diff master origin/master --name-only'
alias gdsgp='git diff staging/gh-pages staging'

alias gf='git fetch' # fetch changes, but don\'t merge into current branch
alias gfo='git fetch origin master'

alias gnew="git log HEAD@{1}..HEAD@{0}" # Show commits since last pull

alias gplom='git pull origin master'
alias gplum='git pull upstream master'

# Specific
alias gfogp='git fetch origin gh-pages'
alias gfsgp='git fetch staging gh-pages'

alias gpl='git pull' # equiv of git fetch + git merge
alias gpogp='git push origin gh-pages'

alias gps='git push staging'
alias gpsgp='git push staging staging:gh-pages'

## Advanced ##

# List all branches with last commit and ref numbers
alias gbls="git for-each-ref --sort=committerdate refs/heads/ --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'"

# Same as above, but for remote branches specifically
alias gblsr="git for-each-ref --sort=committerdate refs/remotes/origin --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'"
```

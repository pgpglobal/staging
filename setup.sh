#!/usr/bin/env bash

# Remind the user to install dependencies, if they haven't already
cat << EndOfMessage
Welcome to the PGP Global setup script.

In order to run the website locally, you'll need to have the following installed:

* Ruby 2.6.3
* Bundler 2.0
* Jekyll 3.8.5

Installation Instructions (in order):
* Install Ruby via https://www.ruby-lang.org/en/documentation/installation/
* Install Bundler: gem install bundler
* Install Jekyll: gem install jekyll bundle

Proceeding with setup script.
EndOfMessage

# Don't mess with the CNAME File!!!!
git update-index --skip-worktree CNAME

# Tell Git to ignore _config_local.yml - so we can change whatever we want.
git update-index --skip-worktree _config_local.yml

# Get the Docs
git submodule update --init

# Add Staging remote and fetch all changes from both remotes
git remote add staging https://github.com/pgpglobal/staging.git
git fetch --all

# Create and checkout local staging branch
git checkout -b staging
# Tell staging to track Remote staging:gh-pages
git branch -u staging/gh-pages

# Pull any changes for our branches
git pull --all

# set `push.default` to always have staging push to staging:gh-pages.
git config push.default upstream

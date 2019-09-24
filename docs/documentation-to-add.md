# Documentation to Add

* Multiple Config Files
* Stuff about Liquid?
* What files correspond to what templates?
* Archive Generation instructions
  * Would still love to set up a Gulp thing... though that might unnecessarily complicate things for them?
  * Ruby Plugin is the best way to go there

## Tools to Add

* Admin plugin?
* Jekyll Simple Search
*

## Workflow Plan

Branch for features

### Thorough Version

One Local Repo
Two Remote Repos: Origin and Staging

Branches:

* gh-pages - This is where the site is served from
* master - this is
* Master (Local & Origin) - this is only used on Origin
* Staging (Local) - this is used to test locally, and to push to the staging server, and test remotely
  * The Remote version of this is Staging:gh-pages. (the gh-pages branch is where the files are served from, locally and remotely)
* gh-pages (both remotes) - This is where the site is served from on both remote servers
  * You could also run this locally, but that may be too redundant, given the existence of the master branch... have to think about that.

1. Start off by working on the local staging branch (or if you need to do a separate feature branch, see below).
2. If everything looks good locally, then git commit all (or relevant files) and git push to staging:gh-pages. If all's well there, the git checkout master, and git pull origin:master (note: it may be better to start off with this??). Make sure to do this *before* you merge
3. git merge staging, then run the server from the master branch. If all's well then git push origin master
4. From here you can either:
  A. Create a Pull Request on GitHub and then accept it on there
  B. git checkout gh-pages. git merge master. git push origin gh-pages

## Troubleshooting - Specific Errors

1. If `jekyll 3.8.5 | Error:  undefined method empty?' for 2012:Integer` comes up after building or serving the site, run `ruby _plugins/luna_archives_generator.rb`


## Category and Tag Pages

1. I only set up Category archives, since none of the posts have Tag info and Jekyll mostly treats them the same

<!-- # Installation & Setup -->

These instructions are being adadpted from the GET Conference repo

## Installation & Dependencies

This website requires you to have the following installed:

* Ruby 2.6.3
* Bundler 2.0
* Jekyll 3.8.5

## Setup

Clone Repo & `cd` into repo dir:

```bash
git clone https://github.com/pgpglobal/PGPGlobal.git
cd PGPGlobal
```

If you want to give the folder a different local name:
`git clone https://github.com/pgpglobal/PGPGlobal.git staging-pgp` (or any other desired name).

Pull and update the _docs submodule:

```bash
git pull --recurse-submodules
git submodule update --recursive
```

### Automated Setup

run setup.sh after cloning the repo `source setup.sh` or `. setup.sh`


### Manual Setup

1. Add Staging Remote & Fetch

```bash
git remote add staging https://github.com/pgpglobal/staging.git
git fetch staging
```

2. Create and checkout local staging branch
  `git checkout -b staging`
3. Tell staging to track Remote staging:gh-pages (note: you must currently be on the staging branch for this to work)
  `gb -u staging/gh-pages`
4. Optional: set `push.default` to always have staging push to staging:gh-pages.

```bash
git config push.default upstream
```

If you don't do this, then you'll have to do the following:

```bash
# To push (local) staging to (remote) staging/gh-pages
git push staging HEAD:gh-pages

# To push (local) staging to (remote) staging/staging
git push staging HEAD
```

5. **Ignore CNAME File**

You must run `git update-index --skip-worktree CNAME`. Not doing so will cause havoc between the staging and production sites.

## Editing

### Main Workflow

Now that we're set up, we can work on the changes locally, push them to staging, and then once all is good, push to the production site.

1. Run `git pull --all` to pull in all the changes for the branches currently on your local environment
2. Create a branch for the feature you're working on. Ex: if you're working on a post, you might type `git checkout -b abbrev-post-name`. If you're making changes to the menu, you might type `git checkout -b luna-nav-menu` or `nav-menu-fix`, etc.
3. Once you've made your changes, run `bundle exec jekyll serve` to test it out locally
4. If everything looks good, then switch to `staging`, merge the new changes, and push to `staging/gh-pages`. Example:

```bash

# Let's say we named our branch new-feature

# Go back to the main staging branch
git checkout -b staging

# Bring in the new changes
git merge new-feature

# Push the changes to the staging site.
# If you set push.default earlier, then simply git push
# Otherwise:
git push staging HEAD:gh-pages
```

### Alternate Workflow

**Note:** If you think you're going to have multiple people working on new staging features at the same time, and are worried about running into merge conflicts, then instead you can do as follows:

1. Make the new feature branch `git checkout -b new-feature`
2. Make your changes
3. Test locally via `bundle exec jekyll serve`
4. Push the `new-feature` branch to the remote staging repo. Ex: `git push new-feature staging/new-feature`
5. Sign into the GitHub Repo and make a Pull Request to integrate the new feature into the main branch. You'll need a maintainer to do this.

I think this alternative workflow may ultimately be redundant, as long as everyone is running `git pull` and/or `git fetch` properly

### Finalize Changes

After everything looks great on the staging site, and you've incorporated everything into the (local) `staging` branch, then push those changes to the (remote) `staging/master` branch. This serves as a backup, so that if something gets messed up later with the `gh-pages` branch, we have a stable working version of the site.

## Incorporate Changes to Production Site

1. Return to your (local) master branch `git checkout master`
2. Merge the changes from the staging site `git merge staging`
3. Test that the changes are working correctly via `bundle exec jekyll serve`
4. If everything's working correctly then `git push origin master`, and setup a pull request on GitHub
5. The project maintainer can then pull those changes into the (remote) `master` branch, and once that's ready can push them to the `gh-pages`.

If you want to make this less redundant, then people can simply do `git push origin master` and the maintainer can `git pull origin master`, make sure everything's working fine and then `git push origin gh-pages`

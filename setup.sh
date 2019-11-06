# Don't mess with the CNAME File!!!!
git update-index --skip-worktree CNAME

# Fetch the _docs submodule (i.e. the PGPGlobal Wiki)
git submodule update --init

# Add Staging remote and fetch all changes from both remotes
git remote add staging https://github.com/pgpglobal/staging.git
git pull --all

# Create and checkout local staging branch
git checkout -b staging
# Tell staging to track Remote staging:gh-pages
git branch -u staging/gh-pages
# Pull again - just to be on safe side
git pull --no-edit
# set `push.default` to always have staging push to staging:gh-pages.
git config push.default upstream

# Create and/or switch to gh-pages and master branches
# Pull any changes for the new branches
git checkout gh-pages
git branch -u origin/gh-pages
git pull --no-edit
# set `push.default` to always have gh-pages push to origin:gh-pages.
git config push.default upstream

git checkout -b master
git branch -u origin/master
git pull --no-edit

# set `push.default` to always have master push to origin:master.
git config push.default upstream

# set `push.default` to always have staging push to staging:gh-pages.
git config push.default upstream

<!-- # Using-Git -->

<!-- MarkdownTOC -->

* [Working on the Site Locally with Git](#working-on-the-site-locally-with-git)
  * [Keeping Up-To-Date](#keeping-up-to-date)
  * [Branching](#branching)
    * [Staging](#staging)
* [Updating Index](#updating-index)

<!-- /MarkdownTOC -->

Note: This doc needs to be double-checked, but should serve as good general info. See also the [Installation-&-Setup](Installation-&-Setup) doc.

<a id="working-on-the-site-locally-with-git"></a>
## Working on the Site Locally with Git

1. Always run `git pull origin master` before doing any local work. This pulls any changes other people made from the online repo, and then updates your local files. If you forget to do this, you will get merge conflicts. Merge conflicts are a headache. See [Solving Merge Conflicts](#merge-conflicts) section below.

<a id="keeping-up-to-date"></a>
### Keeping Up-To-Date

In order to keep the site up-to-date with future changes, you should run `git pull` in your terminal.

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

<a id="staging"></a>
#### Staging

`git push origin local-name:remote-name`

<a id="updating-index"></a>
## Updating Index

Add Assume Index Unchanged for CNAME and such

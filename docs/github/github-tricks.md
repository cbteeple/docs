---
layout: default
title: GitHub Tricks
permalink: github-tips/github-tricks
parent: Github
nav_order: 1
font_awesome: "fas fa-hat-wizard"
---


# <i class="{{ page.font_awesome }}"></i> Become a GitHub Wizard
{: .no_toc }


1. TOC
{:toc}

---


## Undo `git add` before a commit
Documentation from [freeCodeCamp](https://www.freecodecamp.org/forum/t/how-to-undo-a-git-add-with-git-reset/13237)

- `git reset <file>` for each file you want to revert
- `git reset` to unstage all changes.


## Undo local changes to files
Documentation from [GitLab](https://docs.gitlab.com/ee/topics/git/numerous_undo_possibilities_in_git/)

- `git stash` - Discard all local changes, but save them for possible re-use later
- `git checkout -- <file>` - Discard local changes (permanently) to a file
- `git reset --hard` - Discard all local changes to all files permanently



## Untrack files and remove them from remote

Thanks to [Jonathan Klughertz](http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/) for the instructions!

1. Commit all changes first
2. Remove everything from the repository
3. Re-add everything
4. Commit and push

```shell
git add .
git commit -m "added a few things to gitignore"
git rm -r --cached .
git add .
git commit -m ".gitignore fix"
git push
```
 

## Ignore everything except a subdirectory

Thanks to [this stack overflow post](https://stackoverflow.com/questions/1248570/how-do-i-tell-git-to-ignore-everything-except-a-subdirectory) for the instructions!

```shell
/*
/*/
!/bin/
```


## Delete a branch
Thanks to [freeCodeCamp](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/) for the instructions:
``` shell
// delete branch locally
git branch -d <branchName>

// delete branch remotely
git push origin --delete <branchName>
```


## Split a repo into two
[Instructions from Atlassian](https://support.atlassian.com/bitbucket-cloud/docs/split-a-repository-in-two), with 
[extra instructions also from Atlassian](https://www.atlassian.com/blog/git/tear-apart-repository-git-way).

1. Make a [new repo on github](https://github.com/new) (called "_newrepo_"" in these instructions)
2. Make a local copy of your existing repo into a folder called "newrepo":
```shell
git clone <EXISTING REPO URL> newrepo
``` 
3. Remove the origin: `git remote rm origin`
4. Remove folders you don't want in the new repo (this might take a while):
```shell
git filter-branch --index-filter "git rm -r --cached --ignore-unmatch <FOLDER>" --prune-empty -f
```
5. Add the new repo as remote
```shell
git remote add origin <NEW REPO URL>
```
6. Push the newly pruned repo: `git push origin`


## Store your login credentials

[Here's how to do it.](https://help.github.com/en/github/using-git/caching-your-github-password-in-git)



## Use forks to organize your workflow
when multiple people are working on a project, forks make it easier to keep track of the different changes people are making.

### Basics
I use the [standard github fork workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)

If somthing goes wrong, here are some [lesser used commands](https://digitaldrummerj.me/git-syncing-fork-with-original-repo/)


### Turning any repo into a fork
This is from a great tutorial by [handong1587](https://handong1587.github.io/linux_study/2015/12/18/create-multi-forks.html).

Recently I needed to do this for [Marlin Firmware](https://github.com/MarlinFirmware/Marlin), since I have a variety of devices I'm developing on that us different versions:

```shell
git clone https://github.com/MarlinFirmware/Marlin.git
cd Marlin
```
Now create a new repo on github. Mine was **"marlin-cr10s"**


```shell
git remote rename origin upstream
git remote add origin https://github.com/cbteeple/marlin-cr10s.git
git push -u origin


```




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


## Store your login credentials

[Here's how to do it.](https://help.github.com/en/github/using-git/caching-your-github-password-in-git)


## Use forks to organize your workflow
when multiple people are working on a project, forks make it easier to keep track of the different changes people are making.

I use the [standard github fork workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)

If somthing goes wrong, here are some [lesser used commands](https://digitaldrummerj.me/git-syncing-fork-with-original-repo/)





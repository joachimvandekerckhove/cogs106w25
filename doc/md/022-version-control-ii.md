---
title: "Version Control II"
author: "Joachim Vandekerckhove"
date: today
date-format: "[Winter] YYYY"

---

# Version control

* Allow tracking of changes
* Allow branching and merging
* Highly secure

---

# git

* Lots of functionality
* High performace
* Industry standard
* Not too hard to get started
* Quite hard to master

---

# git commands

* git status
* git pull
* git push
* git add
* git commit
* git clone
* git checkout
* git diff
* git fetch
* git merge

---

# git habits

* commit often
* always pull latest versions
* use branches
* comment on commits a lot
* test changes before committing

---

# git first time

1. Create an ssh key pair and copy the public key to GitHub
2. Make a new repo on github.com
3. Give git your identity locally

    ```bash
    git config --global user.email "jv@class-docker"
    git config --global user.name "joachim"
    git config --global --list
    ```
    
4. Clone the repo locally **not inside the workspace**

    ```bash
    mkdir /repo
    cd /repo
    git clone git@github.com:<you>/<repo>.git
    ```

---

# Example workflow

1. Create a new branch

    ```bash
    git checkout -b small-edits
    ```
    
2. Make changes, commit frequently

    ... (make new file)
      
    ```bash
    git add my.new.file.name
    git commit -m "New file added!"
    ```

    ... (make small edit)

    ```bash
    git commit -a -m "I made a small change"
    ```
    
    ... (make tiny edit)

    ```bash
    git commit -a -m "I made a tiny change"
    ```

7. Push

    ```bash
    git push --set-upstream origin main
    git push
    ```
    
---

# Different example workflow

1. Make sure you have all the latest

    ```bash
    git checkout main
    git fetch --all --prune
    git rebase
    git checkout -b bugfix
    ```

2. _(make small edit)_

    ```bash
    git commit -a -m "Fixed bug"
    git push
    ```

3. _(open pull request)_

---

# Resources

[Git tutorial](https://www.atlassian.com/git/tutorials/)

[Git cheat sheet](../../img/git-cheat-sheet.pdf)

[Ubuntu CLI cheat sheet](../../img/ubuntu-cli-cheat-sheet.pdf)

[Linux-fu](https://linuxjourney.com/)


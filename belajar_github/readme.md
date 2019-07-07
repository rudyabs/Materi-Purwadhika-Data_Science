# Tutorial Git and Git Bash #

Change Directory

    cd <path_name>/

Initialize Local Repository

    git init

Make **folder/directory** inside path with *git bash*

    mkdir <name_directory>

Make file inside *git bash*

    touch <file_name.extension>

Show git repository **status**

    git status

Add all file in directory to the **local repository** (staging area)

    git add .

**Commit** (actions ex: delete, add, etc) file to the **local repository**

    git commit -m "<message>"

Add **specific** file to the **local repository** before commiting

    git add <file_name>

**Delete** file from the **local repository**

    git rm --cached <file_name>

## Configuration ##

Set **global username** that reveal **your username** whenever you commit to local or cloud/remote repository.

    git config --global user.name <your_name/username/alias>

Set **global email** that reveal **your email** whenever you commit to local or cloud/remote repository.

    git config --global user.email <your_email>

## Branches ##

Make branches from the main (master) **code base**.  

Create **master** branch :

    git branch <name_branch>

Go to specific **master** and **branch**

    git checkout <name_branch_or_master>

## Merge ##

To merge specific **branch** file to **master**  

Back to **master** area

    git checkout master

**Merge** file

    git merge <branch_name>

## Remote Repository ##

### How to upload file to cloud repository (github) ###

Using **github** for hosting platform, create new repository, etc.  

Add files to cloud repository **(github)**

    git remote add <alias> <repository link>

Push **master** to **online** repository

    git push -u <alias/repository link> master

Push **branch** to **online** repository

    git push -u <alias/repository link> <branch_name>

## Pull ##

To **pull/clone** the **remote repository** so you can use for your *project*

**Init** in the folder you want to do your project

    git init

Pull the **repository**

    git pull <HTTPS link>

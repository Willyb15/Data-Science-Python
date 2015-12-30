# Intro to Git and Github

At the end of this lesson, you should be able to: 

* Describe the importance of using Git for version control
* Describe the difference between Git and Github
* Understand how to initialize a Git repository 
* Understand basic Git/Github commands and how to use them, namely
adding, committing, cloning, pushing, pulling, and forking

## Background 

At the heart of Github is Git, a distributed version control system for 
software development. It allows us to keep track of and manage all of the 
different versions of our files for a project. It does this by keeping a 
history of all of the changes we have ever made to our files, and effectively
works as a backup of all of our files. At any point, we can roll back any of 
the files that we are using with Git and revert back to a previous version.

While Git is a distributed version control system, Github is a hosting service
for Git repositories (you can think of a repository as a directory/folder).
Another way of looking at this is that Github is a hosting service for projects 
that use Git. Github allows us to share our projects with other people, and 
to allow other people to collaborate with us on our projects. We interact with 
Git locally on our labtops/desktops, whereas we interact with Github through 
our web browser.

## Diving In

Before we can work and interact with a Git repository (either locally or 
through Github), we first have to get a Git repository! We get this through 
initializing one, so we'll cover that first. Then we'll move on to the actual
commands that we'll use to interact with our Git repository. 

### Intializing a Git Repository Locally 

A Git repository is a **local** collection of files and contains a .git 
subdirectory in its root. Git keeps track of the state of the files in the 
repository's directory on disk (so long as those files have been added to the 
index - we'll get to that below). There are a couple of different ways to 
create a new repository - the two most common of these are through: 

* Initializing an empty, new local repository
* Downloading another repository (also known as *cloning* in git)

For the time being, we're going to focus on the first one (we'll come back 
to the second later, since it typically involves working with Github). We 
can initialize an empty, new local repository from the command line in the 
following ways: 

```bash 
git init my_new_repo # Initialize a new git repository called my_new_repo. 
git init # Initialize the current directory to be a git repository. 
```

### Interacting with a Git Repository

Now that we have a Git repository, we can start working in that repository 
(directory), and have Git keep track of the changes that we are making to 
any of the files in our repo. The standard workflow within a Git repository 
is that you will change one or more files in the repository, possibly review
the changes, add them to the *index* (a file that Git uses to keep track of 
tracked files), and then create a new commit with those changes. Let's look
at some commands, and then we'll go into a little bit more detail about how
this all works. 

The following are all commands that we would issue on the command line from 
within our Git repository. Note that any time we issue a Git command, it 
will be prefixed by `git`. 

```bash
git status # Will give you the the status of your repository (i.e. what 
           # files have been modified/created/added since your last commit). 
git add my_file.txt # Add the file my_file.txt to the staging area. 
git add my_folder/ # Add the folder my_folder (and all its contents) to the 
                   # staging area. 

git commit -m 'I commited!' # Commit all files in the index staging area with
                            # the commit message 'I commited'.
```

I've mentioned the *index* file above, and while understanding it isn't 
necessary, it can help understand exactly how Git works. The *index* file
(which is hidden in the .git subdirectory of any Git repository) keeps track
of all files that the Git repository is actually responsible for tracking. 
The `git add` command above will put files into the index the first time it 
is run on a file, and from then on out will only note changes to the file (i.e.
what's different from the last time it was commited). For example, if I already
run a `git add` on the `my_file.txt` above, then that `git add my_file.txt` 
command would have added only changes to that file since the last commit. If 
I had already added `my_file.txt` to the index but not made changes to it 
since the last commit, then the `git add my_file.txt` would be worthless. 
`git commit` simply commits the files or changes to files that have been 
added to the *index* to the repository. You can more or less think of the 
`git commit` command as making your changes official; they've gone down in 
history (the Git history). 

### Initializing a Git Repository Through Cloning

Often times, instead of initializing a new, emptry Git repository locally, 
we will be downloading an existing repository to use on your local. The 
process of creating a new local repository from an existing remote repository
is known as *cloning* a repository. To clone a repository, we simply issue
the `git clone` command followed by a URL. 

```bash 
git clone URL # This will copy (clone) an existing repository from the given
              # URL, giving it the same name as the existing repository. Often
              # times this will be a URL that you grabbed from somebody's repo
              # on Github. 
git clone URL unique-folder-name # This will also clone the existing repository
                                 # from the given URL, but rather than giving 
                                 # it the name as denoted by the URL, it will 
                                 # put it in a Git repository called 
                                 # unique-folder-name. 
```

The URL that you copy an existing repository from will almost always be the 
URL of somebody's repo on Github (or your own repo on Github). 

### Working with a Cloned Repository 

Now that we know how to clone a repository, it's time to talk about pushing
and pulling, the process by which we keep a remote copy of our repository 
up to date and in sync with a local copy of our repository (and vice versa). 
Anytime that we have cloned a repository from a URL, the copy of the 
repository at that URL will become the *remote* copy of that repository. 
Pulling is the way that we will keep our local copy of the repository up to 
date with any changes made to the *remote* (by somebody else), and pushing
is the way that we will keep the *remote* up to date with changes to the 
local repository (i.e. changes that we have made that we want to share with
others). Note that you will have to have push access to the repository to be 
able to push your changes to it. 

The last thing to note about how pushing and pulling work is that they will 
only work with changes that have been *commited*. This means that if you 
have changed a file but not gone through the process of *adding* and 
*committing* it, then issuing the push commands below will not actually push
any changes to the remote. Similarly, if there have been no changes to the
remote repository since you last issued a pull, then issuing the pull commands
below will not actually pull anything. 

To issue pushes and pulls: 

```bash 
git push # Push any locally commited changes that aren't in the remote to the remote. 
git pull # Pull any changes in the remote that aren't in the local to the local.
```

### Forking

*Forking* is kind of like *cloning*, but there are two important distinctions: 

* *Forking* occurs on Github, and is specific to Github (i.e. you can't go 
*Fork* on your local machine - it's not an option). 
* *Forking* does not set up the repository that you fork as a remote. It 
creates you're own personalized copy of the repository on your Github account. 
It's as if you cloned the repository, but now any changes that you make will 
not be pushed to where you forked it from, but rather to your personal copy 
on Github. 

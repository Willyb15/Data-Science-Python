# Installing Git 

## Windows Users

If you've gone through the anaconda installation in anaconda.md, you're all 
set! If you haven't, then visit the anaconda.md file and follow the 
the instructions to install Git Bash. 

## Mac Users

1.) Open the terminal, and enter the following command: 

```bash
xcode-select --install
```

Follow the prompts to install it (if you get an error telling you that it 
is already installed, skip to step 2). What this will do is take care of 
installing `git` for you, and making sure it is in the right place on your 
computer. 

2.) In the terminal, type `git` and press `Enter`. You should see something 
along these lines if it has installed correctly: 

```bash 
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
....
....
....
```

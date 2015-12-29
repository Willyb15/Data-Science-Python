# Installing Anaconda 

Follow along with the instructions below for your particular operating 
system. If you're working off a unix distribution that is not Mac OS X, 
you should be able to just work off the Mac OS X instructions, but change
which installation of Anaconda you're downloading (i.e. the Ubuntu install 
if you're running Ubuntu, or the Linux install if you're running a different
installation of Linux).

## Windows Users 

1.) You will first need to install Git Bash. This will become the terminal
through which you run commands, interact with your programs, etc. It also 
has the benefit of handling git installation on your Windows machine. Download
it here: 

[www.git-scm.com/download/vim](https://www.git-scm.com/download/vim)

Follow through the installation instructions. You should be able to just
click next through all of the instructions, **but** along the way make
sure that on the following two screens you make sure the following 
are checked: 

* `Git Bash Here` in the `Select Components` screen. 

![select_components_img](readme_imgs/select_components.JPG)

* `Use Git from Git Bash only` in the `Adjusting your PATH environment` 
  screen. 

![path_img](readme_imgs/path.JPG)

2.) Navigate to the folder where Git Bash was installed, and open git-bash
by clicking on the `git-bash.exe` executable. Once it opens, I would suggest
either creating a shorcut to it on your Desktop or pinning it to your 
taskbar. 

3.) Run the following command in the Git Bash terminal: 

```bash
conda update --all
```

If prompted, enter `yes` when prompted. If you aren't prompted, then 
all your packages are up to date and you are good to go!

## Mac OS X Users

1.) Open up your terminal application, and navigate to your root directory. 
You can find the terminal application in `Finder`, and you can navigate to 
your root directory by typing `cd` into the terminal and pressing enter. 

2.) Enter the following command to download Anaconda: 

```bash 
curl -O https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-2.4.1-MacOSX-x86_64.sh 
```

3.) Enter the following command to install Anaconda: 
    
```bash 
bash Anaconda2-2.4.1-MacOSX-x86_64.sh
```

4.) Enter the following command to update all of the packages within Anaconda: 

```bash 
conda update --all 
```

If prompted, enter `yes` when prompted. If you aren't prompted, then 
all your packages are up to date and you are good to go!

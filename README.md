# Project Initializer

[![demo](https://asciinema.org/a/423713.svg)](https://asciinema.org/a/423713?autoplay=1)


## Initial Set Up
1. Clone the repository
```bash
$ git clone git@github.com:ysomad/project-initializer.git
```
2. Move to project initializer folder
```bash
$ cd /path/to/project-initializer
```
3. Run `setup.sh` and enter github API token and github login
```bash
$ source setup.sh
Enter GitHub API token(with repo scope): 
Enter your GitHub login: 
```

## Usage
Run `init` in the terminal
```bash
$ init -n projectname
```
### Options
Option | Description
------------ | -------------
-n | project name
-f | path to folder where to create a new project
-e | code editor to open newly created project 

# The Purpose of the Project

The purpose of the project is to show a basic CI/CD process, including the following stages:

1. Source code management of the application (managing a remote repo, branching)
1. Building the application (I'll use Docker for it)
1. Testing (to be continued)
1. Deploying (to be continued)

# Prerequisites

The following installed:
1. Git
1. Docker
# The Applicaiton

My personal blog.
During the process I'm using [Jekyll](https://jekyllrb.com/) to compile the files written in Markdown into a fully functioning small site.

Stages of the project:
| Stage | Corresponding branch |
|---|---|
| My site as a standalone Docker container | `standalone-site`| 

In this step of the project, Jykell serves as a server which serves the content of the site locally.

# The Steps

- Choosing the base image version for the application based on the official documentation provided by Jykell.
Jykell depends on Ruby (version 2.5.0 or higher). I chose an Alpine-based image, since these are one of the most lightweight images available.
The base image is based on an absolute version of Ruby and Alpine. By choosing the latest (the default) version of Alpine I could risk in introducing breaking changes into the dependent tools.
- Installing the OS-level dependencies. Jykell depends on such tools as `make`, `gcc`, `musl-dev` and etc.
- Creating a basic scaffolding for the project: `jekyll new myblog --blank`
- Copying the `Gemfile` which lists the packages the project depends on and installing these packages.
- Removing all the redundancies. Jykell introduces some redundant files, which aren't overriden during this stage of the project.
- Copying the actual contents of the site
- `ENTRYPOINT` (the shell form) makes Jykell PID 0 for the container, so it's capable of receiving SIGTERM signals when the container is running. The sole purpose of the container at this stage is to run Jykell.
- The `CMD` options specify additional options for the `bundle` command, namely for Jykell to build and run the site.

#### Some Useful Resources about `ENTRYPOINT` and `CMD` in Docker:

[Docker's official documentation](https://docs.docker.com/engine/reference/builder/#entrypoint)

# To Build and Run the Demo

```bash
git clone https://github.com/nickminaev/mysitedemo.git
cd mysitedemo
docker build -t mysite .
```
To run the demo:
```bash
docker run --name site -v $PWD:/myblog -p 4000:4000 -d mysite
```
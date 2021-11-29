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

| Stage | Corresponding branch |
|---|---|
| My site as a standalone Docker container | `standalone-site`| 
| Smaller version of the image, serving the contents with an NGINX container | `small-site-image` |

In this step of the project, Jykell serves as a server which serves the content of the site locally.

Refer each branch separately for different steps used to build and run the project.
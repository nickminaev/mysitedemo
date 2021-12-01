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

| Stage | Corresponding branch | Link to the post |
|---|---|---|
| My site as a standalone Docker container | `standalone-site`| [post](https://www.nickminaev.com/posts/my-site-project-post1.html)
| Smaller version of the image, serving the contents with an NGINX container | `small-site-image` | [post](https://www.nickminaev.com/posts/my-site-project-post2.html) |
| Automate the site build & deployment | `automate-site-deployment` | [post](https://www.nickminaev.com/posts/my-site-project-post3.html) |


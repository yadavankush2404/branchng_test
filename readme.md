# Testing Branch and feature branch creation.

### clone.

`git checkout backend`

`git pull origin backend`

`git chekout -b feature/add-user-api`

`git add .`

`git commit -m "message" `

### fetch the latest backend branch and rebase

`git checkout backend`
`git pull origin backend`
`git checkout feature/add-user-api`
`git rebase backend`

### create a pull request

`git push origin feature/add-user-api`

### merge the pull request from feature branch to backend branch into the backend branch 

### clean up

` git checkout backend`

`git branch -d feature/add-user-api`

`git push origin --delete feature/add-user-api`

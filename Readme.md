1. We need to create a seperate app for each model/function/requirement of our main project/website
2. `Django-admin startproject telusko ` can be used to start the Django project, which will create a folder and required files in that folder.
3. `python manage.py runserver` to start the Django light weight server 
4. `python manage.py startapp calce` to create a seperate app in your project
5. Added into git with below commands after creating new public repository
```
git init
git add .
git commit -m "Initial commit of telusko Django project"
git remote add origin https://github.com/hariiisai/mylearning.git
git branch -M main
git push -u origin main
#added Readme.md
git add .
(venv) apple@LAPTOP484-PN-IN telusko % git commit -m "Added readme file"
git push
```
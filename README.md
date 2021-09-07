
# Django New Project Template

[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## About
Starter template to make life easier when starting new Django projects

## How to Use
1. Clone repo
2. Run either of the two commands
   ```shell
   $ pip install -r requirements.txt
   ```
3. Do a complete search and replace for `template_project` with whatever 
   name you want to give the project
4. Django migrations
   ```shell
   $ python manage.py makemigrations
   ```
   ```shell
   $ python manage.py migrate
   ```
5. Start the development server
    ```shell
    $ python manage.py runserver
    ```
6. ***You should see a 404 error.*** Add one of the two to the URL 
   * Add `accounts/login/` -> You will see a default login screen from 
     `django-allauth`
   * `/admin`

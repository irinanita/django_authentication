# STARTING

1. `sudo pip3 install django==1.11`
2. `django-admin startproject django_auth .`
3. `django-admin startapp accounts` (accounts it the app's name)
4. In `setting.py` add `accounts` to the  `INSTALLED_APPS`
5. Go to `.bash_aliases` and add  `alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"`
6. In terminal `. ~/.bash_aliases` - to reload the aliases file
7. `python3 manage.py migrate`
8. In `settings.py` update the allowed hosts -- add `os.environ.get("C9_HOSTNAME") to the array

# Django admin panel 

Django comes with built in authentication functionality.

In order to gain acces to Django admin panel we need to create a superuser:
`python3 manage.py createsuperuser`
To access the panel add `/admin` in the url

# Seting up templates
1. create a `templates` folder, add index.html file
2. in `views.py` create the view that will render that file
3. in `urls.py`: `from accounts.views import index` 
    in url patterns `url(r'^$',index)`

`Reverse` allows us to pass the name of the url instead of the view name

`from django.contrib import messages` then we need to update our `settings.py` file
and add `MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"`

In order for django to recognise templates from a different directory we need to go
ti `settings.py` and add `os.path.join(BASE_DIR,'templates')` to `DIRS`

`@login_required` decorator - Allows us to redirect users depending on whether or not they're authenticated;
will redirect users to the login page by default

`registration_form.as_p` rende form as `p` elements

`User` is the standar user object stored in the request
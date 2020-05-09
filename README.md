Once the Vagrant environment is being setted up by installing the vagrant and checking for the version we have

```
$ vagrant init 
```

By doing the above command we have the Vagrantfile being created and the files are as follows .

```
$ ls
Vagrantfile 
```

and then configuration is being placed in the Vagrantfile as shown .'
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8080, host: 8080

  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language
    sudo locale-gen en_GB.UTF-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python-pip
    # Upgrade pip to the latest version.
    sudo pip install --upgrade pip
    # Install and configure python virtualenvwrapper.
    sudo pip install virtualenvwrapper
    if ! grep -q VIRTUALENV_ALREADY_ADDED /home/ubuntu/.bashrc; then
        echo "# VIRTUALENV_ALREADY_ADDED" >> /home/ubuntu/.bashrc
        echo "WORKON_HOME=~/.virtualenvs" >> /home/ubuntu/.bashrc
        echo "PROJECT_HOME=/vagrant" >> /home/ubuntu/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/ubuntu/.bashrc
    fi
  SHELL

end
```

and then the following things are done on the localMachine
```
$ vagrant up
```

The above command does the process of initiating the box of the vagrant by pulling the ubuntu/bionic-64 image and setting up the environment as shown in the Vagrant file.
```
sudo pip install virtualenvwrapper
if ! grep -q VIRTUALENV_ALREADY_ADDED /home/ubuntu/.bashrc; then
    echo "# VIRTUALENV_ALREADY_ADDED" >> /home/ubuntu/.bashrc
    echo "WORKON_HOME=~/.virtualenvs" >> /home/ubuntu/.bashrc
    echo "PROJECT_HOME=/vagrant" >> /home/ubuntu/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/ubuntu/.bashrc
fi
```


```
(env) vagrant@ubuntu-xenial:/vagrant$ pip install -r requirements.txt
Collecting django==2.2
  Downloading Django-2.2-py3-none-any.whl (7.4 MB)
     |████████████████████████████████| 7.4 MB 1.3 MB/s 
Collecting djangorestframework==3.9.2
  Downloading djangorestframework-3.9.2-py2.py3-none-any.whl (911 kB)
     |████████████████████████████████| 911 kB 1.6 MB/s 
Collecting pytz
  Downloading pytz-2020.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 1.2 MB/s 
Collecting sqlparse
  Downloading sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 1.7 MB/s 
Installing collected packages: pytz, sqlparse, django, djangorestframework
Successfully installed django-2.2 djangorestframework-3.9.2 pytz-2020.1 sqlparse-0.3.1

```


Now we will try to setup and create a new project in this folder 
# Creating a new project
```
  $ django-admin startproject profiles_project .
```
  - The anove is the command that is used to create a new project under the current directory

```
  $ python3 manage.py startapp profiles_api
```
  - The above command is used to setup a new app directory under the current prjoect and then 
  structure of the project would be as follows .

  ```
    .
    ├── manage.py
    ├── profiles_api
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── profiles_project
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   └── settings.cpython-35.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── README.md
    ├── requirements.txt
    ├── ubuntu-xenial-16.04-cloudimg-console.log
    └── Vagrantfile
  ```

The next step would be creating the UserModel in profile_api/models.py 
  and this can be done by using the code in the models.py

and then we need to create the migration for the created model using

```
  python3 manage.py make_migration profiles_api
```

and then we need to run the created migrations by

```
  python3 manage.py migrate
```

to run the migrations
output:
```
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, profiles_api, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying profiles_api.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying sessions.0001_initial... OK

```

For the sake of creating the superuser i have did something of this sort
```
  $ python manage.py createsuperuser
```


For the sake of the enabling the django adming for the user profile model we do the following thing


in admin.py
```
from django.contrib import
from profiles_api import models
admin.site.register(models.UserProfile)
```


### Interesting things on routes

> How have i built the routes

Unlike the Rails i have to map the urls to the respect views over here and the interesting thing is that in the profiles_api/views.py i have something of this sort

profiles_api/views.py
```
  from rest_framework.views import APIView
  from rest_framework.response import Response
  #and then wrote some code
  class HelloApiView(APIView):
    """Test the API View"""

    def get(self, request, format=None):
        """Returns the list of the APIView features"""
        an_api_view = [
          "Maps the HTTP Verbs as the functions that is get, post, put, patch(partial update), delete",
          "It is similar to the django views",
          "Gives you the most control over your application",
          "Is mapped manually to URLs"]
        # here we utlise the Response object that whic we have got from the Response definition if in the response.py from rest_framework
        return Response({"message": "Hello","an_api_view": an_api_view})
```

create a file in the profiles_api as urls.py
```

from django.urls import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
```


and in the profile_project/urls.py we have
```
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
```


For the sake of the Login API View we have the following things 
being done
at first in the views.py 

```
  from rest_framework.authtoken.views import ObtainAuthToken
  # this will be used for the sake of the tokenAuthentication usage
  from rest_framework.authentication import TokenAuthentication
  
  class UserLoginView(ObtainAuthToken):
      renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
```


ModHeader is the browser extension that we have used unlike the postman usage we have used it and to enable the token based authentication for this 
we click on the extension and then we add the field called as

Authorization
and the value for this would be "Token ed36e9bd9c6e5be05914ff050f7a24177078bf36"
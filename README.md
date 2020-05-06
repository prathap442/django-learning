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



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
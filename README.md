QuickStart Checklist
===========
- You know a little Python
- You understand pip and virtual environments
- That's all!


1. Clone this repo
2. Create your virtualenv
3. python app.py
4. Navigate to localhost:5000

Whoa Whoa Whoa! That's way too fast!
============
<b>Disclaimer: Sorry Windows people, I'm really not well versed in how this translates. I'll try to keep it as agnostic as possible but we really need that virtual machine set up. (Or try Vagrant!)</b>

<b>Setting up Python:</b>    
I hope you have python, but if not [here's where you can get it](https://www.python.org/downloads/).
We will be using Python2 for this prototyping phase because it works for what we need.

<b>Installing pip:</b>    
Pip is the Python package manager. It stands for "Pip Installs Python". [Here](http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#install-pip-setuptools-and-wheel) are the docs if you are insterested, but I'll cut to the chase. You should actually have pip installed as part of downloading Python. You may want to upgrade though.    
In Mac/*nix:    
```pip install -U pip setuptools```

In Windows:    
```python -m pip install -U pip setuptools```

<b>Optional: Install virtualenvwrapper</b>    
A virtualenv is used to keep packages separated. This is more of a best practice then a requirement, but I think it's really nice to have. With this package we can easily manage virtual environments. We can create a virtualenv with ```mkvirtualenv [name]``` or delete one with ```rmvirtualenv [name]```. Probably the most useful is ```workon [name]```. This one is nice because you don't have to be in any specific directory to switch virtualenvs. It just works. If you need some docs, [here ya go!](https://virtualenvwrapper.readthedocs.org/en/latest/).

<b>Getting to the Development:</b>    
So now that that is set up, navigate to the cloned repo. Make sure you're in your virtualenv (or don't, I'm not your dad) and run: ```pip install -r requirements.txt```. This will, you guessed it, install our required packages (flask). Boom! You're done! Run ```python app.py``` and go to localhost:5000 to see the hello world app.

Vagrant
=======

<b>What is Vagrant?</b>    
Vagrant allows you to spin up a standardized development environment on any platform. The project has been set up so that you can run the code in an Ubuntu virtual machine while editing the code and viewing the webpage using the editors and browsers on your host system. If you want to do this you will first need to [install Vagrant](https://www.vagrantup.com/downloads.html).

<b>Getting Started</b>    
Once you have Vagrant installed (and on Windows you might need to put it on your path) you can download the base image for Ubuntu 14.04 LTS with `vagrant box add ubuntu/trusty64`. Then, while in the directory for this project, launch a VM with `vagrant up`. Finally, you can log into the VM with `vagrant ssh`.

It will already have pip, setuptools, virtualenv, and virtualenvwrapper installed, but you will still need to install the modules from `requirements.txt`, either globally or within a virtualenv. Our project files will be mounted inside of the VM at `/vagrant`. You will see the exact same files from within the guest as well as on the host, and you can edit them from either side. Run the project inside the guest with `./app.py --bind 0.0.0.0`, which is necessary for the port forwarding. Then navigate to `http://localhost:5000/` on your host system and you will see the home page.

What's an SSH key?
============
Some of you may have this set up, but if not here's somthing to help you out. By using SSH keys you never have to log in to Github through the terminal again. I'll just link to the Github guide because it's [pretty good](https://help.github.com/articles/generating-ssh-keys/#platform-all).

Current Issues
=============
 - [ ] Define api function that returns a JSON response for mock data
 - [ ] Transform Feature Flag doc into JSON file
 - [ ] Create Skeleton HTML
 - [ ] Create fancy search bar component
 - [ ] Create Feature Flag component
 - [ ] Create Selection Component(Combo boxes to select System/Application) that will have search bar within it


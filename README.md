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
<b>Disclaimer: Sorry Windows people, I'm really not well versed in how this translates. I'll try to keep it as agnostic as possible but we really need that virtual machine set up.</b>

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
A virtualenv is use to keep packages separated. This is more of a best practice then a requirement, but I think it's really nice to have. With this package we can easily manage virtual environments. We can create a virtualenv with ```mkvirtualenv [name]``` or delete one with ```rmvirtualenv [name]```. Probably the most useful is ```workon [name]```. This one is nice because you don't have to be in any specific directory to switch virtualenvs. It just works. If you need some docs, [here ya go!](https://virtualenvwrapper.readthedocs.org/en/latest/).

<b>Getting to the Development:</b>
So now that that is set up, navigate to the cloned repo. Make sure you're in your virtualenv (or don't, I'm not your dad) and run: ```pip install -r requirement.txt```. This will, you guessed it, install our required packages (flask). Boom! You're done! Run ```python app.py``` and go to localhost:5000 to see the hello world app.

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


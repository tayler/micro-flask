#Yet Another Flask Boilerplate Repo.

###About

Flask is a micro framework, and this is a micro Flask setup.

The repo. contains just enough to get a new Flask app off the ground. No Bootstrap, no SQLAlchemy, etc.

I'm new to Flask and Python, and I wanted a decent starting point for new Flask apps, something where I understood all the moving parts.

The setup is mostly from the Package structure in [Explore Flask](http://exploreflask.com/organizing.html#organization-patterns), but some stuff was filled in from the Flask tutorial at [Real Python](http://www.realpython.com/blog/python/python-web-applications-with-flask-part-i/).

###Project Structure

```sh
├── README.md
├── config.py (configuration that is not environment specific. Config values set in instance/config.py override those set in this config.py)
├── instance/ (config. that should not be in version control, e.g., sensitive creds. and/or environment specific variables like `DEBUG`)
│   └── config.py
├── requirements.txt
├── run.py (used only in development. Test site with `python run.py`. You need to modify the `import` statement around line 5 to match the name of the package)
└── yourappname/ (change to the name of your app)
    ├── __init__.py
    ├── forms.py
    ├── models.py
    ├── static/
	|	├── img
    │   ├── js
    │   │   ├── main.js
    │   │   └── vendors/
    │   └── style
    │       └── main.css
    ├── templates/
    │   ├── home.html (very, very basic home page template)
    │   └── layout.html (very basic layout file)
    └── views.py
```

See [Explore Flask](http://exploreflask.com/organizing.html#organization-patterns) for more setup possibilities.

###Setup

1. Clone this repo
2. Change package name (currently yourappname) to the name of your app
3. Repeat for `import` statement in run.py
4. Setup virtualenv for this directory & activate (because I always forget, virtualenvwrapper command is `mkvirtualenv <env-name>`)
5. Create an instance/ dir containing a config.py file
6. `pip install -r requirements.txt`
7. `python run.py`
8. Navigate to 127.0.0.1:5000 in your browser to test it out

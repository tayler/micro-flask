from flask import Flask
from .views import public

# If we set instance_relative_config=True when we create our app with the
# Flask() call, app.config.from_pyfile() will load the specified file from
# the instance/ directory
app = Flask(__name__, instance_relative_config=True)
# this brings in the settings from config.py (at the project's root)
# Now we can access the configuration variables via app.config["VAR_NAME"].
app.config.from_object('config')
# this brings in settings from instance/config.py
app.config.from_pyfile('config.py')

# register blueprint we defined in views.py
app.register_blueprint(public)

# http://exploreflask.com/organizing.html#organization-patterns
# This is the file that is invoked to start up a development server.
# It gets a copy of the app from your package and runs it.
# This won't be used in production, but it will see a lot of mileage
# in development.

# change `yourappname` to whatever the app should be called;
# it matches the name of the package in the root dir.
# right now, the package dir is called yourappname
from yourappname import app

if __name__ == '__main__':
    app.run()

#import the app factory function. import create_app from petfax folder.
from petfax import create_app
#Now that we have access to the factory function in petFax folder, we can create an instance
#of app.py by invoking a function and saving it to a variable call app.
app= create_app()
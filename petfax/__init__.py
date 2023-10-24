from flask import Flask

# application factory function


def create_app():
    app = Flask(__name__)  # create new app instance of Flask

    @app.route('/')
    def hello():  # create index route that goes to '/' and just returns "hello.." as a string
        return 'Hello, PetFax!'
    
     # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)
   
    from . import fact
    app.register_blueprint(fact.bp)
    
    # @app.route('/pets')
    # def pets():
    #     return 'Hello, These are our pets looking for forever homes'
    # register the pet Blueprint
    

    return app  # return app

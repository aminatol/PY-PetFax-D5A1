from flask import Flask
from flask_migrate import Migrate
#  SQL factory


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ace88yZoro97@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Call the init_app method on it(SQLAlchemy class method through models.py) and pass it the app instance.
    #databse config
    from . import models

    models.db.init_app(app)
    migrate = Migrate(app, models.db)
# application factory function

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

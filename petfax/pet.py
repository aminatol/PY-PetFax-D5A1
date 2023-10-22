from flask import (Blueprint, render_template)
import json
# open() the pets.json file by passing it as an argument and pass
pets = json.load(open('pets.json'))
# open function as an argument to json.load. this will open json file and passing to json file will enable python to read it
print(pets)
bp = Blueprint('pets', __name__, url_prefix='/pets')


@bp.route('/')
def index():
    return render_template('index.html', pets=pets)


@bp.route('/<int:pet_id>')
def show(pet_id):
    pet = pets[pet_id-1]

    return render_template('pets_show.html', pet=pet)


@bp.route('facts/new/<int:pet_id>')
def form(pet_id):
    pet = pets[pet_id-1]

    return render_template('form.html', pet=pet)

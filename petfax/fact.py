from . import models
from flask import (Blueprint, render_template, request, redirect)
bp = Blueprint('fact', __name__, url_prefix="/facts")

# new instance of Fact model


@bp.route('/new')
def form():
    return render_template('facts/form.html')


# POST

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(f'{request.form} request')
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')

    results = models.Fact.query.all()
        

    return render_template('facts/index.html', facts=results)

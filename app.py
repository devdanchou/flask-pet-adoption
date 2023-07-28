"""Flask app for adopt app."""

import os

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """show homepage with list of pets"""

    pets = Pet.query.order_by("id").all()
    print("\n\n****", "pets:", pets[0])

    return render_template('homepage.html', pets=pets)

@app.get('/add')
def show_add_pet_form():
    """display the add pet form """

    return render_template

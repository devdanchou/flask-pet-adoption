"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_URL = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")

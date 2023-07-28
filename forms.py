"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
        validators=[InputRequired()])

    photo_URL = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    age = SelectField(
        "Age",
        choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")],
        validators=[InputRequired()])

    notes = StringField(
        "Notes",
        validators=[Optional()])

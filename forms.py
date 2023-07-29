"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
        validators=[InputRequired()])

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    age = SelectField(
        "Age",
        choices=[("baby", "Baby"),
                 ("young", "Young"),
                 ("adult", "Adult"),
                 ("senior", "Senior")],
        validators=[InputRequired()])

    notes = StringField(
        "Notes",
        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet info"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()])

    notes = StringField(
        "Notes",
        validators=[Optional()])

    available = BooleanField(
        "Available",
        validators=[Optional()])

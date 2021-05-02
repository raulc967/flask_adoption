from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Name of Pet", validators=[InputRequired()])
    species = SelectField("Species Type", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],)
    photo_url = StringField("Photo's URL", validators=[Optional(), URL()])
    age = FloatField("Pet's Age", validators=[Optional(), NumberRange(min=0, max=35)])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[InputRequired()])

class EditPetForm(FlaskForm):
    """ Form for editing pets """

    photo_url = StringField("Photo's URL", validators=[Optional(), URL()])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Available")
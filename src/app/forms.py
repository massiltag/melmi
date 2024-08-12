from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Nom de l\'évènement', validators=[DataRequired()])
    submit = SubmitField('Créer')

class AvailabilityForm(FlaskForm):
    name = StringField('Ton prénom', validators=[DataRequired()])
    available_times = HiddenField('Tes disponibilités', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')

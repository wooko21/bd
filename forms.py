import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, IntegerField, \
    DecimalField, DateTimeLocalField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, ValidationError


class AddReservationForm(FlaskForm):
    movie_name = SelectField('wybierz tytul filmu')
    showings = SelectField('wybierz show')
    seat = SelectField('wybierz miejsce na sali')


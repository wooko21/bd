import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, IntegerField, \
    DecimalField, DateTimeLocalField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, ValidationError


class AddReservationForm(FlaskForm):
    movie_name = SelectField('wybierz tytul filmu', validators=[DataRequired(message='To pole nie może być puste')])
    showings = SelectField('wybierz show', validators=[DataRequired(message='To pole nie może być puste')])
    seat = SelectField('wybierz miejsce na sali', validators=[DataRequired(message='To pole nie może być puste')])


class AddMovie(FlaskForm):
    movie_name = StringField('wpisz nazwe filmu', validators=[DataRequired(message='To pole nie może być puste')])


class AddCityForm(FlaskForm):
    city = StringField('Dodaj nowe miasto do bazy danych:')
    province = StringField('W jakim województwie znajduje się miasto?')
    submit = SubmitField('Zatwierdź')


class SelectMovie(FlaskForm):
    movie_name = SelectField('wybierz film na który chcesz zarezerwować miejsce')
    submit = SubmitField('zatwierdź')


class SelectShowing(FlaskForm):
    showing_date_auditorium = SelectField('wybierz konkretny seans')
    submit = SubmitField('zatwierdź')


class SelectSeat(FlaskForm):
    seat = SelectField('wybierz siadanie - kelnerka miała piękne')
    submit = SubmitField('zatwierdź')

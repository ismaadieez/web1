from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Teléfono', validators=[DataRequired(), Length(max=30)])
    message = TextAreaField('Mensaje', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Enviar')

class ReservationForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Teléfono', validators=[DataRequired(), Length(max=30)])
    message = TextAreaField('Observaciones', validators=[Length(max=1000)])
    submit = SubmitField('Reservar')

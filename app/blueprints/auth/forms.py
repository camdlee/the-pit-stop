# -------------- IMPORTS -------------
from flask_wtf import Flaskform
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo



# ------------------- FORMS ------------------

#------------ Register Form --------------
class RegistrationForm(Flaskform):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo(password)])
    submit_btn = SubmitField('Sign Up')



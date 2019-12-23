from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


required_message = "This is required"

class login_form(FlaskForm):
    email = TextField("Email",validators=[InputRequired(message=required_message),Email(message='Invalid email'), Length(min=5, max=50, message='Length error')])
    password = PasswordField("Password",validators=[InputRequired(required_message)])
    # password2 = PasswordField("Password",validators=[InputRequired(required_message), EqualTo("password", message="Password does not match")])
    login_button = SubmitField('Login')
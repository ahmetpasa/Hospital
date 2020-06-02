from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RoomForm(FlaskForm):
    roomID = IntegerField('Room_ID',validators=[DataRequired()])
    patient = StringField('Patient',validators=[DataRequired()])
    nurse = StringField('Nurse',validators=[DataRequired()])
    update = SubmitField('Update')
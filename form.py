from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RoomForm(FlaskForm):
    roomID = IntegerField('Room_ID',validators=[DataRequired()])
    patient = StringField('Patient',validators=[DataRequired()])
    nurse = StringField('Nurse',validators=[DataRequired()])
    update = SubmitField('Update')
    
class MeetingForm(FlaskForm):
    description = StringField('Description',validators=[DataRequired()])
    appointment = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], default=date.today)
    add = SubmitField('Add')
    
class MeetingUpdateForm(FlaskForm):
    recordID = IntegerField('Record ID',validators=[DataRequired()])
    appointmentupd = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()], default=date.today)
    upd = SubmitField('Update')
    
class MeetingDeleteForm(FlaskForm):
    recordIDdel = IntegerField('Record ID',validators=[DataRequired()])
    dele = SubmitField('Delete')
    
class AddDiagnosis(FlaskForm):
    diag = SelectField("Choose Diagnosis", validators=[DataRequired()], choices=[])
    to_patient = SelectField("To Which Patient", validators=[DataRequired()], choices=[])
    upd_2 = SubmitField('Update')

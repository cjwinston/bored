from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
class ProfileForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=25)])
    birthDate = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    allergies = StringField('Allergies')
    medicalConditions = StringField('Medical Conditions')

class MedicationsForm(FlaskForm):
    medications = StringField('Medications')
    time =  TimeField('Time', format='%H:%M')
    number_of_times = IntegerField('Number of times each day') # Use radio field instead??
    submit = SubmitField('Add')
    # Could use python schedular to send notifications to user
    # Add 
    
class SearchForm(FlaskForm):
    search = StringField('Enter search')
    submit = SubmitField('Search')
    
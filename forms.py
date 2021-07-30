from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms import PasswordField, SubmitField, TimeField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


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


class SearchForm(FlaskForm):
    search = StringField('Enter search')
    submit = SubmitField('Search')


class TriviaForm(FlaskForm):
    number_of_questions = IntegerField("Number of Questions",
                                       validators=[NumberRange(min=0, max=10, message='Please select a number')])
    # API call to determine how the list of categories is ordered
    # inorder to assign category values
    category = SelectField('Select Category',
                           choices=[(0, 'Any'),
                                    (9, 'General Knowledge'),
                                    (10, 'Entertainment: Books'),
                                    (11, 'Entertainment: Film'),
                                    (12, 'Entertainment: Music'),
                                    (13, 'Entertainment: Musicals & Theatres'),
                                    (14, 'Entertainment: Television'),
                                    (15, 'Entertainment: Video Games'),
                                    (16, 'Entertainment: Board Games'),
                                    (17, 'Science & Nature'),
                                    (18, 'Science: Computers'),
                                    (19, 'Science: Mathematics'),
                                    (20, 'Mythology'),
                                    (21, 'Sports'), (22, 'Geography'),
                                    (23, 'History'), (24, 'Politics'),
                                    (25, 'Art'), (26, 'Celebrities'),
                                    (27, 'Animals')])
    difficulty = SelectField('Select Type',
                             choices=[(0, 'Any'),
                                      ('easy', 'Easy'), ('medium', 'Medium'),
                                      ('hard', 'Hard')])
    types = SelectField('Select Difficulty',
                        choices=[(0, 'Any'),
                                 ('multiple', 'Multiple Choice'),
                                 ('boolean', 'True or False')])
    submit = SubmitField('Submit')


class WatchForm(FlaskForm):
    filmType = SelectField('Select Movie or Show',
                           choices=[(0, 'Movie'), (1, 'Show')])

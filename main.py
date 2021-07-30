from flask import Flask, render_template, url_for, flash, redirect
from flask import session, request
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from forms import RegistrationForm, LoginForm, TriviaForm, WatchForm, EventForm
from flask_login import LoginManager, UserMixin
from flask_login import login_required, login_user, logout_user
from trivTest import *
from movieTVData import getFilmData, parseData
from events import getData, createDict


# test login_info
#1 email: test@gmail.com, password = 12345
#2 email: test2@gmail.com, pass = 67890


# for TMDB API
tmdb_apikey = '25cd471bedf2ee053df9b1705494367d'
tmdb_base_url = 'https://api.themoviedb.org/3/'


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
# login = LoginManager(app)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'c3eec5c8ffb8f4c3b45f24e2b11bf875'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# this tells you the URL the method below is related to
@app.route("/")
@app.route("/home.html")
def home():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


@app.route("/trivia",  methods=['GET', 'POST'])
@login_required
def trivia():
    form = TriviaForm()
    if form.validate_on_submit():
        number = str(form.number_of_questions.data)
        category = form.category.data
        difficulty = form.difficulty.data
        types = form.types.data
        getData(number, category, difficulty, types)
        # correctly takes in input for if all sections have data, have not tested for 'Any' option
        return redirect("home.html")
    return render_template('trivia.html', subtitle='Trivia Page',
                           form=form)


@app.route("/events")
@login_required
def events():
    form = EventForm()
    if form.validate_on_submit():
        keyword = form.eventType.data
        city = form.city.data
        r = getData(keyword, city)
        d = createDict(r)
        return render_template('eventsResults.html',
                               subtitle='Results',
                               data=d,
                               )
    return render_template('events.html', subtitle='Enter an event')


# https://flask-login.readthedocs.io/en/latest/#configuring-your-application
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                # session['logged_in'] = True
                # msg = 'You have successfully logged in!'
                # return render_template('search.html', msg=msg)
                flash(f'You have successfully logged in!', 'success')
                return redirect(url_for('events'))
            else:
                # msg = 'Incorrect password.
                #       Check your login credentials and try again.'
                # return render_template('login.html', msg=msg)
                flash('Incorrect password. Check your login credentials and try again.')
                return redirect(url_for('login'))
        else:
            # msg = "Sorry. We couldn't find an account with that email. Please check your login credentials and try again."
            # return render_template('login.html', msg=msg)
            flash("Sorry. We couldn't find an account with that email. Please check your login credentials and try again.")
            return redirect(url_for('login'), form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    # session.pop('logged_in', None)
    flash(f'Sucessfully Logged Out', 'success')
    return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('It seems there is an account with this email already. Please Log In.')
            return redirect(url_for('login'))
        else:
            newUser = User(email=form.email.data, password=form.password.data)
            db.session.add(newUser)
            db.session.commit()
            flash(f'Account created for {form.email.data}!', 'success')
            return redirect(url_for('search'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route("/movietv", methods=['GET', 'POST'])
@login_required
def movietv():
    form = WatchForm()
    if form.validate_on_submit():
        filmType = form.filmType.data
        trendTpe = form.trendTpe.data
        d = getFilmData(tmdb_apikey, filmType, trendType)
        dict = parseData(d)

            
    return render_template('movietv.html', form=form)

# NOTE: NO USERNAME NEEDED
# profile page from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
# @app.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = [
#         {'author': user, 'body': 'Test post #1'},
#         {'author': user, 'body': 'Test post #2'}
#     ]
#     return render_template('user.html', user=user, posts=posts)


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

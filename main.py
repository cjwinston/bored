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
from events import getEventData, createDict


# test login_info
# 1 email: test@gmail.com, password = 12345
# 2 email: test2@gmail.com, pass = 67890


# for TMDB API
tmdb_apikey = '25cd471bedf2ee053df9b1705494367d'
tmdb_base_url = 'https://api.themoviedb.org/3/'


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
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


@app.route("/trivia", methods=['GET', 'POST'])
@login_required
def trivia():
    form = TriviaForm()
    if form.validate_on_submit():
        number = str(form.number_of_questions.data)
        category = form.category.data
        difficulty = form.difficulty.data
        types = form.types.data
        r = getData(number, category, difficulty, types)
        global d
        d = createTrivia(r)
        return render_template('triviaQues.html', subtitle='Questions', data=d)
    return render_template('trivia.html', subtitle='Trivia Page',
                           form=form)


@app.route("/triviaAns", methods=['GET', 'POST'])
@login_required
def triviaAns():
    correct = 0
    data = request.form
    for i in d.keys():
        answered = data[str(i)]
        if d[i]['correct answer'] == answered:
            correct += 1
    return render_template('triviaAns.html', correct=str(correct))


@app.route("/events", methods=['GET', 'POST'])
@login_required
def events():
    form = EventForm()
    if form.validate_on_submit():
        keyword = form.eventType.data
        city = form.city.data
        try:
            r = getEventData(keyword, city)
            d = createDict(r)
        except KeyError:
            return render_template('eventsError.html')
        return render_template('eventsResults.html',
                               subtitle='Event Results',
                               data=d,
                               )
    return render_template('events.html', subtitle='Enter an event', form=form)


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
                return redirect(url_for('events'))
            else:
                flash('Incorrect password. Check your login credentials and try again.')
                return redirect(url_for('login'))
        else:
            flash("Sorry. We couldn't find an account with that email. Please check your login credentials and try again.")
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash(f'Sucessfully Logged Out', 'success')
    return redirect(url_for('login'))


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
        trendType = form.trendType.data
        d = getFilmData(tmdb_apikey, filmType, trendType)
        dic = parseData(d)
        return render_template('watchResults.html',
                               subtitle='Watch Results',
                               data=dic
                               )
    return render_template('movietv.html', form=form)


@app.route("/watchResults", methods=['GET', 'POST'])
@login_required
def watch():
    return render_template('watchResults.html')


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

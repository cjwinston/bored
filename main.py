from flask import Flask, render_template, url_for, flash, redirect
from flask import session, request
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from forms import RegistrationForm, LoginForm, MedicationsForm
# from flask_login import LoginManager
# from flask_login import login_required


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
# login = LoginManager(app)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'c3eec5c8ffb8f4c3b45f24e2b11bf875'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.email}')"


# this tells you the URL the method below is related to
@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


@app.route("/medications")
def medications():
    form = MedicationsForm()
    return render_template('medications.html', subtitle='Medication Page',
                           form = form)


@app.route("/search")
def search():
    return render_template('search.html', subtitle='Enter a Medical/Wellness Topic')


# https://flask-login.readthedocs.io/en/latest/#configuring-your-application
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data)
        if user:
            if user.password == form.password:
                flash('You have successfully logged in!')
                return redirect(url_for('medications'))
        else:
            flash('Incorrect email or password. Check your login credentials and try again.')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('medications'))
    return render_template('signup.html', title='Sign Up', form=form)
    

# NOTE: NO USERNAME
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

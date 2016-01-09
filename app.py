from flask import Flask, render_template, request, session, flash, redirect, url_for
from pymongo import MongoClient

import utils
import secrets

app = Flask(__name__)
app.secret_key = secrets.secret_key

client = MongoClient()

@app.route('/')
@utils.require_login
def home():
    return render_template('home.html')

@app.route('/submit-work')
@utils.require_login
def submit_work():
    return render_template('submit-work.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # check password
        if request.form['password'] == secrets.password:
            # set cookie and redirect
            session['logged_in'] = 'yaaaas'
            session.permanent = True
            return redirect(url_for('home'))
        else:
            # set alert and fall through to normal get request
            flash('bad password')

    # GET request
    return render_template('login.html')

@app.route('/log-out')
@utils.require_login
def log_out():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run('0.0.0.0', 9000, debug=True)

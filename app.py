from datetime import date
from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
from pymongo import MongoClient
from werkzeug import secure_filename

import config
import secrets
import utils

app = Flask(__name__)
app.secret_key = secrets.secret_key
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

client = MongoClient()

state = {
    'currentTheme': 'no theme'
}

@app.route('/')
@utils.require_login
def home():
    return render_template('home.html')

@app.route('/submit-work', methods=['GET', 'POST'])
@utils.require_login
def submit_work():
    if request.method == 'GET':
        return render_template('submit-work.html')

    # POST
    # save any files of allowed filetypes
    files = request.files.getlist('images')
    for f in files:
        # if the file is an appropriate type, save it
        if config.allowed_file(f.filename):
            # get the full path name
            themeFolder = secure_filename(state['currentTheme'])
            today = date.today()
            dayFolder = '%s-%s-%s' % (today.year, today.month, today.day)
            filename = secure_filename(f.filename)
            fullPath = os.path.join(
                app.config['UPLOAD_FOLDER'],
                themeFolder,
                dayFolder,
                filename
            )

            # make directories if necessary
            if not os.path.exists(fullPath):
                os.makedirs(os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    themeFolder,
                    dayFolder,
                ))

            # save file
            f.save(fullPath)
            flash('uploaded image: %s' % f.filename)
        else:
            # otherwise inform the user they fucked up
            flash('bad image type: %s' % f.filename)

    return redirect(url_for('home'))

@app.route('/gallery')
@utils.require_login
def gallery():
    templateArgs = {}
    templateArgs['themes'] = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', templateArgs=templateArgs)

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

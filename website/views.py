from flask import render_template
from website import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/members/')
def members():
    return render_template('members.html')


@app.route('/jobs/')
def jobs():
    return render_template('jobs.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/logout/')
def logout():
    pass


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/forgot-password/')
def forgot_password():
    return render_template('forgot_password.html')

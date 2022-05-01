from flask import render_template, request, redirect, session
from flask_app.models.email import User
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if not User.validate_form(request.form):
        return redirect('/')
    data = {"email": request.form['email']}
    id = User.save(data)
    return redirect(f'/success/{id}')

@app.route('/success/<int:id>')
def show(id):
    email = User.get_one(id)
    emails = User.get_all()
    return render_template("success.html", email=email, all_emails=emails)

@app.route('/go-back')
def clear():
    session.clear()
    return redirect('/')


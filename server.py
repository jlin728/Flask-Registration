from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
app = Flask(__name__)
app.secret_key="SecretKeyPassword"


# @app.route('/', methods=['get']) < the GET doesn't work. Why?
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/submit', methods=['post'])
def submit():
  name = request.form['name']
  last = request.form['last']
  email = request.form['email']
  password = request.form['password']
  confirm = request.form['confirm']

  if len(request.form['name']) and len(request.form['last']) < 1:
    flash('Name cannot be empty')
  if not request.form['name'].isalpha() or request.form['last'].isalpha():
    flash('Name can only contain letters')
  if len(request.form['email']) < 1:
    flash('Email cannot be empty')
  if not EMAIL_REGEX.match(request.form['email']):
    flash('Invalid Email')
  if len(request.form['password']) or len(request.form['confirm']) < 1:
    flash('Password cannot be blank')
  if password != confirm:
    flash('Passwords do not match')
  else:
    flash('Success')

  print request.form #put print before return to see data in console
  return redirect('/')


app.run(debug=True) # run our server
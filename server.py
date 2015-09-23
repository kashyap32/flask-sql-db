from flask import Flask, request, redirect, url_for, session, render_template, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
a#p.secret_key = '\xed\xee\x92\xcfMF\x98\xaf]\x08X\xad\x9eR\xd7\x03w\xb7\xcb\xba\xe7\xfa\x8b['
#kashyap
mysql = MySQLConnector('YOUR DATABASE NAME Should be HERE') #NAme of your database

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create():
	error = False
	name = request.form['name']
	email = request.form['email']
	password = request.form['password']
	password_confirm = request.form['password_confirm']
	
	if len(name) < 3:
		error = True
		flash('Name cannot be blank')
	if len(email) < 1:
		error = True
		flash('Email cannot be blank')
	if len(password) < 3:
		error = True
		flash('Password cannot be blank')
	if len(password_confirm) < 3:
		error = True
		flash('Password confirmation cannot be blank')
	if not EMAIL_REGEX.match(email):
		error = True
		flash('Email is invalid')
	if password != password_confirm:
		error = True
		flash('Passwords do not match')

	if error is True:
		return redirect(url_for('index'))

	pw_hash = flask_bcrypt.generate_password_hash(password)
	insert_query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(name, email, pw_hash)
	print insert_query
	mysql.run_mysql_query(insert_query)
	return redirect(url_for('show'))

@app.route('/show')
def show():
	if 'id' not in session:
		return redirect(url_for('signin'))
	return render_template('show.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		return render_template('signin.html')

	email = request.form['email']
	password = request.form['password']
	signin_query = "SELECT * FROM users WHERE email='{}' LIMIT 1".format(email)
	user = mysql.fetch(signin_query)
	if user:
		if flask_bcrypt.check_password_hash(user[0]['password'], password):
			session['id'] = user[0]['id']
			session['name'] = user[0]['name']
			return redirect(url_for('show'))
	flash('Invalid email or password')
	return redirect(url_for('signin'))

@app.route('/signout')
def signout():
	session.pop('id')
	session.pop('name')
	return redirect(url_for('index'))
app.run(debug=True)






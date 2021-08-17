from flask import Flask, render_template, request, redirect, url_for, session
import re
from flask_mysqldb import MySQL
from assets.credentials import *


print(r'''
     __       _       _           
    /  \     | |     | | 
   /    \    | | /\  | | /\   _   _
  /  /\  \   | |/ /  | |/ /  | | | |  
 /  ____  \  | |\ \  | |\ \  | |_| |
/__/    \__\ |_| \_\ |_| \_\  \___/  ''')
print("\n*************************************")
print("\n* Copyright of Akash, 2021          *")
print("\n* https://www.github.com/akkupy     *")
print("\n* https://t.me/akkupy               *")
print("\n*************************************")

app = Flask(__name__)

app.secret_key = "akku"

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = database
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/favicon.ico') 
def favicon(): 
    return ""

@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor()
		cursor.execute('SELECT * FROM people WHERE email = % s AND password = % s', (email, password))
		retreive = cursor.fetchone()
		if retreive:
			session['loggedin'] = True
			session['id'] = retreive['s_id']
			session['email'] = retreive['email']
			session['name'] = retreive['name']
			session['date_of_birth'] = retreive['date_of_birth']
			msg = 'Logged in successfully !'
			return render_template('loggedin.html', msg = msg)
		else:
			msg = 'Invalid Credentials!'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('email', None)
	msg="You are Logged Out"
	return render_template('index.html',msg=msg)

@app.route('/signup', methods =['GET', 'POST'])
def signup():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'date_of_birth' in request.form and 'gender' in request.form and 'name' in request.form:
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		dob=request.form['date_of_birth']
		gender=request.form['gender']
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT * FROM people WHERE email = '{}'".format(email))
		back = cursor.fetchone()
		cursor.execute("select * from people")
		ids=cursor.fetchall()
		h=len(ids)+101
		if back:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z]+', name):
			msg = 'Username must contain only characters !'
		elif not password or not email:
			msg = 'Please fill out the form !'
		elif gender not in ['M','F','O']:
			msg = "Please choose gender correctly"
		else:
			cursor.execute("INSERT INTO people VALUES ({}, '{}','{}', '{}','{}','{}')".format(h,name, email, password,dob,gender ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('signup.html', msg = msg)

if __name__ == '__main__':
	app.run(threaded=True)
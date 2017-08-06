from flask import Flask, render_template, redirect, request, session, flash
import re, time
from datetime import date
app = Flask(__name__)
app.secret_key = "whoknows"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

"""
Ninja Version:
Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.
"""

def has_number(check_this):
	for i in check_this:
		if i.isdigit():
			return True
	return False

"""
Hacker Version:
Add a birth-date field that must be validated as a valid date and must be from the past.
"""

def is_dob(check_date):
    try:
        d = time.strptime(check_date, "%m/%d/%Y")
        today = time.strptime(date.today().strftime("%m/%d/%Y"), "%m/%d/%Y")
        if d >= today:
            return False
        return True
    except ValueError:
        return False

@app.route('/')
def index():
	session['email'] = ["valid", '']
	session['first_name'] = ["valid", '']
	session['last_name'] = ["valid", '']
	session['password'] = ["valid", '']
	session['pass_conf'] = ["valid", '']
	session['bdate'] = ["valid", '']
	session['success'] = None
	return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
	session['email'] = ["valid", request.form['email']]
	session['first_name'] = ["valid", request.form['first_name']]
	session['last_name'] = ["valid", request.form['last_name']]
	session['password'] = ["valid", request.form['password']]
	session['pass_conf'] = ["valid", request.form['pass_conf']]
	session['bdate'] = ["valid", request.form['bdate']]
	session['success'] = None
	mood = "freakout"

	if len(session['email'][1]) < 1 or EMAIL_REGEX.match(session['email'][1]) == None:
		flash("Please enter a valid email address.")
		session['success'] = False
		session['email'][0] = "notvalid"
	if len(session['first_name'][1]) < 1:
		flash("First name cannot be blank.")
		session['success'] = False
		session['first_name'][0] = "notvalid"
	if len(session['last_name'][1]) < 1:
		flash("Last name cannot be blank.")
		session['success'] = False
		session['last_name'][0] = "notvalid"
	if len(session['bdate'][1]) < 1 or is_dob(session['bdate'][1]) == False:
		flash("Please enter a valid date of birth in MM/DD/YYYY format (e.g. for July 28 1989 enter 07/28/1989).")
		session['success'] = False
		session['bdate'][0] = "notvalid"
	if len(session['password'][1]) < 1 or has_number(session['password'][1]) == False or session['password'][1].islower() == True:
		flash("Please enter a valid password, containing at least one uppercase letter and one numeric value.")
		session['success'] = False
		session['password'][0] = "notvalid"
	if session['password'][1] != session['pass_conf'][1]:
		flash("Password confirmation must match password.")
		session['success'] = False
		session['pass_conf'][0] = "notvalid"
	elif session['success'] != False:
		flash("Thank you for submitting your information.")
		mood = "happy"
	return render_template('index.html', mood=mood)

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "SuperSecret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
	session['your_name'] = request.form['your_name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	if len(request.form['your_name']) < 1:
		flash("Name cannot be blank!")
		return redirect('/')
	if len(request.form['comment']) < 1 or len(request.form['comment']) > 120:
		flash("Comment cannot be blank, and must be less than 120 characters.")
		return redirect('/')
	else:
		return render_template("result.html")

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

'''
TODO:
Save successfully submitted form data in session so user doesn't have to resubmit.
'''

app.run(debug=True)
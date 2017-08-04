from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "counter"


@app.route('/count')
def counting():
	session['count'] += 1
	return render_template("index.html")

@app.route('/')
def index():
	session['count'] = 0
	return redirect('/count')

#Ninja Lvl 1
@app.route('/plustwo', methods=['POST'])
def plus_two():
	session['count'] += 1
	return redirect('/count')

#Ninja lvl 2
@app.route('/reset', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/count')


app.run(debug=True)
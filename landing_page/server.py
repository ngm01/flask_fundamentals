from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas/')
def ninjas():
	return render_template('ninjas.html')

@app.route('/dojos/news/')
def news():
	return render_template('dojos.html')

@app.route('/nowhere', methods=['POST'])
def go_nowhere():
	name = request.form['name']
	email = request.form['email']
	return redirect('/dojos/news')

app.run(debug=True)
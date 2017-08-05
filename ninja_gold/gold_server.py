from flask import Flask, render_template, request, redirect, session
import random, time
app = Flask(__name__)
app.secret_key = "ninjagold"



@app.route('/')
def index():
	session['gold'] = 0
	session['updates'] = []
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	update_color = 'green'
	if request.form['building'] == 'farm':
		earnings = random.randint(10, 21)
		session['gold'] += earnings
		session['updates'] += [[update_color, "Earned " + str(earnings) + " gold from the farm!"]]
	if request.form['building'] == 'cave':
		earnings = random.randint(5, 11)
		session['gold'] += earnings
		session['updates'] += [[ update_color, "Earned " + str(earnings) + " gold from the cave!"]]
	if request.form['building'] == 'house':
		earnings = random.randint(2, 6)
		session['gold'] += earnings
		session['updates'] += [[update_color, "Earned " + str(earnings) + " gold from the house!"]]
	if request.form['building'] == 'casino':
		gamble = random.randint(-50, 51)
		session['gold'] += gamble
		if gamble < 0:
			update_color = 'red'
			session['updates'] += [[update_color, "Entered a casino and lost " + str(abs(gamble)) + " gold. Ouch..."]]
		elif gamble == 0:
			update_color = 'black'
			session['updates'] += [[update_color, "Entered a casino and won no gold."]]
		else:
			session['updates'] += [[update_color, "Entered a casino and won " + str(gamble) + " gold!"]]
		session['gold'] += gamble
	return render_template("index.html")

app.run(debug=True)
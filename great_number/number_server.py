from flask import Flask, redirect, request, render_template, session
import random


app = Flask(__name__)
app.secret_key = "numbergame"


@app.route('/')
def set_game():
	random_number = random.randrange(1, 101)
	print random_number
	session['random_number'] = random_number
	return redirect('/welcome')

@app.route('/welcome')
def index():
	return render_template('/index.html')


@app.route('/guess', methods=["POST"])
def guess():
	box_size = '200px'
	try:
		player_guess = int(request.form["guess"])
		if player_guess > session['random_number']:
			box_text = "Too High!"
			box_color = 'red'
		elif player_guess < session['random_number']:
			box_text = "Too Low!"
			box_color = 'blue'
		else:
			return render_template('/won.html')
	except ValueError:
		box_text = "That is not a number!"
		box_color = 'orange'
	return render_template('/index.html', box_color = box_color, box_text = box_text, box_size = box_size)

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)
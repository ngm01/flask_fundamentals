from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', turtle="tmnt.png")

@app.route('/ninja/<color>')
def routethis(color):
	tmnt = {
	'blue': 'leonardo',
	'purple': 'donatello',
	'red': 'raphael',
	'orange': 'michelangelo'
	}
	colors = []
	for c in tmnt:
		colors += [c]
	print colors
	if color not in colors:
		return render_template('index.html', turtle="notapril.jpg")
	else:
		turtle = tmnt[color] + '.jpg'
		return render_template('index.html', turtle=turtle)

@app.errorhandler(404)
def error(e):
	msg = "ERROR 404 TURTLES NOT FOUND"
	return render_template('index.html', turtle="shredder.jpg", msg=msg)

app.run(debug=True)


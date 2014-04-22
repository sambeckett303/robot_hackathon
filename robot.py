from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.debug = True


@app.route('/browse')
def browse():
	return render_template('browse.html')

@app.route('/robot/go/<int:num>', methods=['POST', 'GET'])
def go(num = 1):
	numbra = num*1400
	print numbra
	return render_template('robotgo.html', number = numbra)

@app.route('/robot/square/<int:num>')
def square(num = 1):
	return render_template('robotsquare.html', number = num)

@app.route('/robot/hexagon/<int:num>')
def hexagon(num =1):
	return render_template('robothexagon.html', number = num)

@app.route('/robot/trick1')
def trick1():
	return render_template('trick1.html')

@app.route('/robot/trick2/<int:num>/<int:length>')
def trick2(num = 1, length = 1):
	return render_template('trick2.html', number = num, length = length)

if __name__ == '__main__':

	app.run()


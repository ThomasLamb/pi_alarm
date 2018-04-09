import datetime

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route("/")
@app.route('/index')
@app.route('/home')
def index():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	tomorrow = datetime.date.today() + datetime.timedelta(days=1)
	tomorrowDayName = tomorrow.strftime("%A")

	templateData = {
		'application': 'Pi Alarm Clock',
		'title': 'Main',
		'time': timeString,
		'day': tomorrowDayName
	}
	return render_template('main.html', **templateData)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)

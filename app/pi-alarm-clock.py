import datetime

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    now = datetime.datetime.now()
    currentTimeString = now.strftime('%A, %B %-d, %Y %-H:%M %S %p')
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrowDayName = tomorrow.strftime("%A")
    tomorrowAlarmTimeString = '06:45:00'

    templateData = {
        'application': 'Pi Alarm Clock',
        'title': 'Main',
        'currentTime': currentTimeString,
        'alarmDay': tomorrowDayName,
        'alarmTime': tomorrowAlarmTimeString
    }
    return render_template('main.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

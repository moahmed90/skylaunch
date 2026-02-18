from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PRAYERS = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

DUAS = {
    'Fajr': 'Allahumma inni as\'aluka ilman nafi\'an — O Allah, I ask You for beneficial knowledge.',
    'Dhuhr': 'Allahumma anta al-salam wa minka al-salam — O Allah, You are peace and from You comes peace.',
    'Asr': 'Hasbunallahu wa ni\'mal wakeel — Allah is sufficient for us and He is the best disposer of affairs.',
    'Maghrib': 'Allahumma inni as\'aluka al-jannah — O Allah, I ask You for paradise.',
    'Isha': 'Bismika Allahumma amutu wa ahya — In Your name, O Allah, I die and I live.'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prayer_times = None
    city = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        try:
            response = requests.get(
                f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=&method=2'
            )
            data = response.json()
            timings = data['data']['timings']
            prayer_times = {p: timings[p] for p in PRAYERS}
        except Exception:
            error = 'Could not fetch prayer times. Please check the city name and try again.'

    return render_template('index.html', prayer_times=prayer_times, city=city, duas=DUAS, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
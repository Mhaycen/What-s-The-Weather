import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap = Bootstrap(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    city="Casablanca"
    if request.method == 'POST':
        city = request.form.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4ef97242af122b6344856fbab46ef824'
    r = requests.get(url.format(city)).json()
    weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        
    return render_template('index.html',weather=weather)


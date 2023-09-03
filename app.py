from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
API_KEY = 'a2a7458d5c0647939f761323230309'

@app.route('/', methods=['GET', 'POST'])
def weather():
    city = ''
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        if city:
            weather_data = get_weather(city)

    return render_template('index.html', city=city, weather_data=weather_data)

def get_weather(city):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {'key': API_KEY, 'q': city}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['current']['condition']['text'],
            'temperature': data['current']['temp_c'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
        }
        return weather

    return None

if __name__ == '__main__':
    app.run(debug=True)

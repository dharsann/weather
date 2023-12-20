from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'YOUR_WEATHER_API_KEY'  # Replace with your actual weather API key

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
            'feels_like': data['current']['feelslike_c'],
            'visibility': data['current']['vis_km'],
            'pressure': data['current']['pressure_mb'],
            'uv_index': data['current']['uv'],
            'cloud': data['current']['cloud'],
            'precipitation': data['current'].get('precip_mm', 'N/A'),
        }
        return weather

    return None

if __name__ == '__main__':
    app.run(debug=True)

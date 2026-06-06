import requests

WEATHER_API_key='dc86dbde3e3ee0ad0949c31cea4884bd'
def get_weather(city):
    CITY_NAME=city

    LOC_API = f'https://geocoding-api.open-meteo.com/v1/search?name={CITY_NAME}&count=1&language=en&format=json'
    
    try:
        location = requests.get(LOC_API)

        if location.status_code == 200:
            loc_data = location.json()

            if 'results' not in loc_data:
                return {
                    'ERROR':'Enter a valid city name'
                }

            CITY_NAME=loc_data['results'][0]['name']
            lat = loc_data['results'][0]['latitude']
            lon = loc_data['results'][0]['longitude']
            
            WEATHER_API = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_key}&units=metric'

            weather = requests.get(WEATHER_API)

            if weather.status_code==200:
                w_data = weather.json()
                temp = w_data['main']['temp']
                humidity = w_data['main']['humidity']
                condition = w_data['weather'][0]['main']

                return {
                'CITY': CITY_NAME,
                'TEMPERATURE': temp,
                'HUMIDITY': humidity,
                'CONDITION':condition,
                }

            else:
                return {
                    'ERROR':'Weather data not available'
                }

        else:
            return {
                'ERROR':'Location API failed'
            }

    except:
        return {
            'ERROR':'Something went wrong'
        }
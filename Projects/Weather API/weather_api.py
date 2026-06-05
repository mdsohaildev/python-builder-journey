import requests

WEATHER_API_key='YOUR_API_KEY'
CITY_NAME=input("Enter City Name:" )

LOC_API = f'https://geocoding-api.open-meteo.com/v1/search?name={CITY_NAME}&count=1&language=en&format=json'
location = requests.get(LOC_API)

if location.status_code == 200:
    loc_data = location.json()
    if 'results' not in loc_data :
        print("Enter a valid city name")
        exit()
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
        print('--------WEATHER REPORT----------')
        print('CITY: ',CITY_NAME)
        print('TEMPERATURE: ',temp,'celsius')
        print('HUMIDITY: ',humidity,'%')
        print('CONDITION: ',condition)

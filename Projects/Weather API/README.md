# Weather App using Python

A simple Python weather application that fetches real-time weather information for any city using APIs.

## Features

* Get weather by city name
* Displays:

  * Temperature
  * Humidity
  * Weather condition
  
* Handles invalid city names
* Uses real-time API data

## Technologies Used

* Python
* Requests Library
* Open-Meteo Geocoding API
* OpenWeatherMap API

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
```

2. Navigate into the project folder

```bash
cd weather-app
```

3. Install dependencies

```bash
pip install requests
```

## Setup

Replace your API key in the code:

```python
WEATHER_API_KEY = "YOUR_API_KEY"
```

You can get a free API key from OpenWeatherMap.

## Run the Project

```bash
python weather.py
```

## Example Output

```text
Enter City Name: Warangal

-------- WEATHER REPORT --------
CITY         : Warangal
TEMPERATURE  : 31 Celsius
HUMIDITY     : 70 %
CONDITION    : Clouds
```

## Future Improvements

* Add weather icons
* Add 5-day forecast
* Build GUI using Tkinter
* Create web version using Flask
* Add error handling for internet issues

## Author

Sohail Mohammed

# 🌦 Weather App using Python & Streamlit

A simple weather application built using Python and Streamlit that fetches real-time weather information for any city using APIs.

## Features

* Get weather details by city name
* Displays:

  * Temperature
  * Humidity
  * Weather condition
* Handles invalid city names
* Handles API/network errors
* Real-time weather data
* Simple and clean Streamlit UI

## Technologies Used

* Python
* Streamlit
* Requests Library
* Open-Meteo Geocoding API
* OpenWeatherMap API

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
```

### 2. Navigate into the project folder

```bash
cd weather-app
```

### 3. Install dependencies

```bash
pip install streamlit requests
```

## Setup

Replace your API key in `weather_api.py`

```python
WEATHER_API_key='YOUR_API_KEY'
```

Get your free API key from OpenWeatherMap.

## Run the Project

```bash
streamlit run app.py
```

## Project Structure

```text
weather-app/
│
├── app.py
├── weather_api.py
├── README.md
```

## Example Output

```text
City: Warangal
Temperature: 31 °C
Humidity: 70 %
Condition: Clouds
```

## Future Improvements

* Add weather icons
* Add 5-day weather forecast
* Add dark mode UI
* Show wind speed and pressure
* Deploy publicly using Streamlit Cloud

## Author

Sohail Mohammed


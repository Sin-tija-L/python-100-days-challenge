# 🌟 **Day 92 Challenge: Build Your Own Weather App!** 🌦️

Today’s challenge is all about **bringing the weather to life** by creating your very own weather app! 🌞🌧️ Whether you’re a sunny day lover or enjoy the sound of rain, this project will help you learn how to work with APIs and conditionals while building something truly practical.

---

## 🛠️ **What You'll Build**
By the end of this challenge, your app will:
- 🗺️ Fetch the weather forecast for your local area.
- 📅 Display today's forecast, including:
  - A **text description** of the weather (no cryptic codes here!).
  - 🌡️ The **maximum and minimum temperatures**.
- 🧠 Use **Boolean operators** to make decisions about multiple weather codes.

---

## 🚀 **Getting Started**
We’ve got your back with some starter code! Copy this and tweak it to make it yours:

```python
import requests, json

# 🌍 Define your location and timezone
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

# 🔗 Get weather data from the Open-Meteo API
result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}"
)

# 🛠️ Process and pretty-print the result
user = result.json()
print(json.dumps(user, indent=2))
```

## ✏️ **Customize Your App**
1. 🗺️ **Update the Latitude & Longitude**  
   Replace the values with coordinates for your nearest city or location. Not sure where to find them? A quick search like “latitude and longitude of [Your City]” will help. 🌎

2. 📋 **Interpret the Weather Code**  
   Add an **if...elif...else** block to convert the weather codes into human-readable descriptions. For example:
   ```python
   if code == 0:
       print("☀️ Clear sky")
   elif code == 1 or code == 2 or code == 3:
       print("🌤️ Partly cloudy")
   elif code == 45 or code == 48:
       print("🌫️ Foggy")
   # ...add more conditions for other codes
   ```

3. 🌡️ **Format the Forecast Output**  
   Make your app display the forecast in a **user-friendly format**:
   - Max Temperature: `🌡️ 18°C`
   - Min Temperature: `❄️ 8°C`
   - Description: `☀️ Clear sky`

---

## 🌟 **Your Challenge Goals**
- Use the **Open-Meteo API** to fetch the daily weather forecast.  
- **Display today’s forecast** with:
  - Weather description (decoded from the weather code).
  - Maximum and minimum temperatures.
- **Practice Boolean Operators**: Use `and`, `or`, and `not` to handle multiple conditions within your `if...elif` block.

---

## 🧠 **Tips & Tricks**
- 📚 **Documentation Is Your Friend**: Check out the [Open-Meteo API docs](https://open-meteo.com) for more weather codes and features you might want to include.
- 🖼️ **Make It Pretty**: Use emojis in your output to make the forecast fun and visually appealing.  
- 🔍 **Debugging Help**: Print intermediate values (like the weather code) to ensure your logic works as expected.

---

## 🎯 **Stretch Goals** (Optional but Fun!)
- 🌐 **Add a GUI**: Use a library like `tkinter` to create a simple graphical interface for your app.
- 🕐 **Hourly Forecast**: Modify the API request to fetch hourly weather data.
- 🌈 **Weather for Multiple Cities**: Let the user input a city name and fetch its weather automatically.

Good luck and have fun! 🍀 Don’t forget to share your creation with the community! 🚀

<img id="image" src="assets/day92_1.png" alt="day92 image" width="690">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import requests
from datetime import datetime

# 🌍 Define your location and timezone
timezone = "Europe/Riga"
latitude = 56.9496
longitude = 24.1052
location_name = "Riga, Latvia"  # Add your location name here

# 🔗 Fetch weather data from the Open-Meteo API
result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone}"
)

# Check if the API call was successful
if result.status_code == 200:
    weather_data = result.json()
    daily_forecast = weather_data['daily']

    # Get today's date in ISO format
    today = datetime.now().strftime('%Y-%m-%d')

    # Find the index of today's date in the forecast data
    if today in daily_forecast['time']:
        today_index = daily_forecast['time'].index(today)

        # Get the weather code, max temperature, and min temperature for today
        weather_code = daily_forecast['weathercode'][today_index]
        max_temperature = daily_forecast['temperature_2m_max'][today_index]
        min_temperature = daily_forecast['temperature_2m_min'][today_index]

        # Weather code meanings
        weather_codes = {
            0: "☀️ Clear sky",
            1: "🌤️ Mainly clear",
            2: "⛅ Partly cloudy",
            3: "☁️ Overcast",
            45: "🌫️ Foggy",
            48: "🌫️ Depositing rime fog",
            51: "🌦️ Drizzle: Light",
            53: "🌦️ Drizzle: Moderate",
            55: "🌦️ Drizzle: Dense intensity",
            61: "🌧️ Rain: Slight",
            63: "🌧️ Rain: Moderate",
            65: "🌧️ Rain: Heavy",
            71: "🌨️ Snow fall: Slight",
            73: "🌨️ Snow fall: Moderate",
            75: "🌨️ Snow fall: Heavy",
            80: "🌧️ Rain showers: Slight",
            81: "🌧️ Rain showers: Moderate",
            82: "🌧️ Rain showers: Violent",
            95: "⛈️ Thunderstorm: Slight or moderate",
            96: "⛈️ Thunderstorm with hail: Slight",
            99: "⛈️ Thunderstorm with hail: Heavy",
        }

        # Display the forecast for today
        print("🌟 Weather Forecast for Today 🌟")
        print(f"📍 Location: {location_name}")
        print(f"📅 Date: {today}")
        print(f"🌈 Weather: {weather_codes.get(weather_code, 'Unknown')}")
        print(f"🌡️ Max Temperature: {max_temperature}°C")
        print(f"❄️ Min Temperature: {min_temperature}°C")
    else:
        print("⚠️ Today's weather data is not available in the API response.")
else:
    print(f"❌ Failed to fetch weather data. HTTP Status Code: {result.status_code}")
```

</details>
import requests
import csv
from datetime import datetime

# Configuración
API_KEY = "c9deb6d2a679577e7bc6dcb3c1b2c0c1"  
LAT = "50.81"  # Latitud de Marburg, Alemania
LON = "8.77"   # Longitud de Marburg, Alemania
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
URL2 = f"http://api.openweathermap.org/data/2.5/weather?q={'Marburg'}&appid={API_KEY}&units=metric"
# Obtener datos
response = requests.get(URL)
data = response.json()

# Extraer información relevante
dt = datetime.fromtimestamp(data["dt"])  # Conversión de timestamp a datetime
temp = data["main"]["temp"]  # Temperatura en grados centígrados
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
wind = data["wind"]["speed"]
description = data["weather"][0]["description"]
rain_1h = data.get("rain", {}).get("1h", 0)  # Lluvia en 1h (0 si no hay datos)
snow_1h = data.get("snow", {}).get("1h", 0)  # Nieve en 1h (0 si no hay datos)


# Guardar en archivo CSV
with open("MarburgWeather/clima-marburg-hoy.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([dt, temp, humidity, pressure, wind, description, rain_1h, snow_1h])

print("Datos guardados en clima-marburg-hoy.csv")
print(data)
    

import pyowm
location=input("What is your location?")
owm = pyowm.OWM('a890f86bdf5ad37ff9800f966a10ac2f')
observation = owm.weather_at_place(location)
w = observation.get_weather()
t=w.get_temperature()
print(w)
print(t)

marie=w.get_wind()
print(marie["speed"])
print(w.get_humidity())

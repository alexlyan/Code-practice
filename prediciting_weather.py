import requests
from pprint import pprint
city =input("Enter your city: ")

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=49ca951308953479f7b479e1f6fd7ea0".format(city)

res = requests.get(url)

data = res.json()

temp=data["main"]["temp"]
temp=temp-273.15
print(f"Temperature: {temp} celcius degrees")
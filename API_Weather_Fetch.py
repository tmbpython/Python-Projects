import requests



API_KEY = "YourAPIKey"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("The current weather is", weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("The current temperature is", temperature, "Degrees Celcius")

else:
    print("An error occured.")

import requests

city_name = input("Enter city Name:")
API_key = 'f02446548cd8ea2e3777ef2d3fa49d60'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is ',data['weather'][0]['description'])
    print('Current Temperature  is ',data['main']['temp'])
    print('Current Temperature Feel Like is ',data['main']['feels_like'])
    print('Humidity is ',data['main']['humidity'])



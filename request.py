import requests

# url = (
  #  "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,"
  #  "wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

# r = requests.get(url)
# print(r.text)
# data = r.json()
# print(data['current_units']['interval '])

url = ("https://media.licdn.com/dms/image/D4D03AQHICkTubP3pnw/profile-displayphoto-shrink_200_200/0/1689166000889?e"
       "=2147483647&v=beta&t=RKUwrgIBCjfWSo51zf6HBrEiYcT1dDWjPwgJyr6KQog")

r = requests.get(url)

with open('susannah.png', mode='wb') as mf:
    mf.write(r.content)


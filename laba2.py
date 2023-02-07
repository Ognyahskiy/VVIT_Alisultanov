import requests
city="Moscow,RU"
appid="eb8ba5cb9a58e96e2289b7842f37e7b7"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print('Прогноз на день')
print("Видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])
print('__________________________')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nВидимость <", '{0:+3.0f}'.format(i['visibility']), "> \r\nСкорость ветра <", i['wind']['speed'], ">")
    print("____________________________")

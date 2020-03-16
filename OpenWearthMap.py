import requests

print(" TEMPO E TEMPERATURA EM MACAPÁ-AP")
url = 'http://api.openweathermap.org/data/2.5/weather?q=Macapa,br&appid=60051e79041e462339a7ebab19564464&units=metric'

search = requests.get(url)
resultado = search.json()

nome = resultado['name']
latitude = resultado['coord']['lat']
longitude = resultado['coord']['lon']
temperatura = resultado['main']['temp']
temp_min = resultado['main']['temp_min']
temp_max = resultado['main']['temp_max']
umidade = resultado['main']['humidity']
velocidade_vento = resultado['wind']['speed']
descricao = resultado['weather'][0]['description']

print("Nome da cidade: {}".format(nome))
print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))
print("Temperatura: {}° C".format(temperatura))
print("Temperatura minima: {}° C".format(temp_min))
print("Temperatura maxima: {}° C".format(temp_max))
print("Umidade do ar: {} %".format(umidade))
print("Velocidade do vento: {} Km/h".format(velocidade_vento))


if "light rain" in descricao:
    print("Descrição: Chuva leve")

elif "broken clouds" in descricao:
    print("Descrição: nebuloso")

elif "overcast clouds" in descricao:
    print("Descrição: Nublado")

elif "heavy intensity rain" in descricao:
    print("Chuva intensa")

elif "scattered clouds" in descricao:
    print("Descrição: Nuvens esparsa")

elif "few cloud" in descricao:
    print("Descrição: Poucas nuvens")
    
elif "overcast" in descricao:
    print("Descrição: Encoberto")

elif "clear sky" in descricao:
    print("Descrição: Ceu limpo")





    #print("Descrição: {}".format(descricao))
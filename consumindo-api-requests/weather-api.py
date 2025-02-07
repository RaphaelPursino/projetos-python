import requests

# Sua chave da API (substitua pelo valor correto)

#API_KEY = url_apikey

# Cidade que você deseja buscar o clima
cidade = "Guarapari"

# URL base da API

#url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt"

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    dados = response.json()
    
    # Extraindo informações principais
    cidade = dados["name"]
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]

    print(f"Clima em {cidade}:")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"🌧️ Condição: {descricao}")
    print(f"💧 Umidade: {umidade}%")
else:
    print(f"Erro ao obter os dados: {response.status_code}, {response.text}")

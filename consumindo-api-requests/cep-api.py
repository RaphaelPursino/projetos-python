import requests

url = "https://viacep.com.br/ws/"

cep = input("Digite o cep sem traço: ")

response = requests.get(f"{url}/{cep}/json")
if response.status_code == 200:
    adress = response.json()
    for c, v in adress.items():
        print(f"\n{c.upper()} : {v}")
else:
    print("Erro: ", response.status_code, response.text)
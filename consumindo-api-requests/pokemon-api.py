import requests

url = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Digite o nome do Pokemon: ")

response = requests.get(f"{url}/{pokemon}")

if response.status_code == 200:
    poke = response.json()
    print(f"\nID: {poke["id"]}")
    print(f"\nNome: {poke["name"]}")
    print(f"\nExperiência: {poke["base_experience"]}")
    print(f"\nAltura: {poke["height"]}")
    print(f"\nPeso: {poke["weight"]}")
else:
    print("Erro: ", response.status_code)
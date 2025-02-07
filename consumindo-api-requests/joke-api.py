import requests

url = "https://v2.jokeapi.dev/joke/Any?lang=pt"

api_key = "sua_api_aqui"

headers = {
    "X-api=key": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    joke_data = response.json()

    if joke_data["type"] == "twopart":
        print(f"{joke_data["setup"]}")
        print(f"{joke_data["delivery"]}")
    else:
        print(f"{joke_data["joke"]}")
else:
    print(f"Erro: {response.status_code}: {response.text}")

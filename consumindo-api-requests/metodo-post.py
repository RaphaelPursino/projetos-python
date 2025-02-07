import requests

url_base = "http://localhost:5000/posts"

def create_post():
    novo_post = {
        "title": "Criado com o método post",
        "body": "Praticando o método post"
    }
    response = requests.post(url_base, json=novo_post)
    if response.status_code == 201:
        post_criado = response.json()
        print("Post criado:\n", post_criado)
    else:
        print("Erro ao criar post: ", response.status_code)

if __name__ == "__main__":
    create_post()
import requests

url_base = "http://localhost:5000/posts"

def update_post(post_id):
    post_atualizado = {
        "id": post_id,
        "title": "Post atualizado",
        "body": "Conteúdo atualizado"
    }
    response = requests.put(f"{url_base}/{post_id}", json=post_atualizado)
    if response.status_code == 200:
        post_novo = response.json()
        print("Post atualizado: \n", post_novo)
    else:
        print("Erro ao atualizar post: ", response.status_code)
    
if __name__ == "__main__":
    update_post("f780")
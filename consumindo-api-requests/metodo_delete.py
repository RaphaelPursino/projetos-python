import requests

url_base = "http://localhost:5000/posts"

def delete_post(post_id):
    response = requests.delete(f"{url_base}/{post_id}")
    if response.status_code == 200:
        print(f"Post com o ID {post_id} foi excluído")
    else:
        print("Erro ao excluir post: ", response.status_code)

if __name__ == "__main__":
    delete_post("806d")
import requests

url_base = "http://localhost:5000/posts"

def get_posts():
    response = requests.get(url_base)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print("ID: ", post["id"])
            print("Title: ", post["title"])
            print("Body: ", post["body"], "\n")
    else:
        print("Erro na requisição: ", response.status_code)

if __name__ == "__main__":
    get_posts()
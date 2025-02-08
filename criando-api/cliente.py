import requests

BASE_URL = "http://127.0.0.1:8000/usuarios"

# --- 1️⃣ GET - Listar todos os usuários ---
def listar_usuarios():
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())

# --- 2️⃣ POST - Criar um novo usuário ---
def criar_usuario(usuario_id, nome, email):
    dados = {"id": usuario_id, "nome": nome, "email": email}
    response = requests.post(BASE_URL, json=dados)
    print(response.status_code, response.json())

# --- 3️⃣ PUT - Atualizar um usuário pelo ID ---
def atualizar_usuario(usuario_id, nome, email):
    url = f"{BASE_URL}/{usuario_id}"
    dados = {"id": usuario_id, "nome": nome, "email": email}
    response = requests.put(url, json=dados)
    print(response.status_code, response.json())

# --- 4️⃣ DELETE - Remover um usuário pelo ID ---
def deletar_usuario(usuario_id):
    url = f"{BASE_URL}/{usuario_id}"
    response = requests.delete(url)
    print(response.status_code, response.json())

# Testando as funções
if __name__ == "__main__":
    print("📌 Criando usuários...")
    criar_usuario(1, "João Silva", "joao@email.com")
    criar_usuario(2, "Maria Souza", "maria@email.com")

    print("\n📌 Listando usuários...")
    listar_usuarios()

    print("\n📌 Atualizando usuário 1...")
    atualizar_usuario(1, "João Pedro", "joao_pedro@email.com")

    print("\n📌 Listando usuários após atualização...")
    listar_usuarios()

    print("\n📌 Deletando usuário 2...")
    deletar_usuario(2)

    print("\n📌 Listando usuários após exclusão...")
    listar_usuarios()

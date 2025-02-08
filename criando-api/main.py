from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simulando um banco de dados na memória
usuarios = []

# Modelo para entrada de dados
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# --- Métodos CRUD ---

# 1️⃣ GET - Listar todos os usuários
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

# 2️⃣ POST - Criar um novo usuário
@app.post("/usuarios", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario

# 3️⃣ PUT - Atualizar um usuário pelo ID
@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[i] = usuario_atualizado
            return usuario_atualizado
    return {"erro": "Usuário não encontrado"}

# 4️⃣ DELETE - Remover um usuário pelo ID
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario.id != usuario_id]
    return {"mensagem": "Usuário removido com sucesso"}

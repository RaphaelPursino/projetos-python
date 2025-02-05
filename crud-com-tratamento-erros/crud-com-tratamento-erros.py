cadastro = {}

def adicionar():
    id = input("Digite o ID do usuário: ")
    if not id.isdigit():
        print("ID inválido. O ID deve conter apenas números.")
        return
    nome = input("Digite o nome do usuário: ")
    if not nome.replace(" ", "").isalpha():
        print("Nome inválido. O nome deve conter apenas letras.")
        return
    cadastro[id] = nome
    print(f"Usuário {nome} cadastrado com sucesso.")

def visualizar():
    if not cadastro:
        print("Nenhum usuário cadastrado.")
    else:
        for id, nome in cadastro.items():
            print(f"ID: {id} - Nome: {nome}")

def editar():
    id = input("Digite o ID do usuário que deseja editar: ")
    if not id.isdigit():
        print("ID inválido. O ID deve conter apenas números.")
        return
    if id not in cadastro:
        print("Usuário não encontrado.")
        return
    novo_nome = input("Digite o novo nome do usuário: ")
    if not novo_nome.replace(" ", "").isalpha():
        print("Nome inválido. O nome deve conter apenas letras.")
        return
    cadastro[id] = novo_nome
    print(f"Usuário atualizado para {novo_nome}.")

def excluir():
    id = input("Digite o ID do usuário que deseja excluir: ")
    if not id.isdigit():
        print("ID inválido. O ID deve conter apenas números.")
        return
    if id not in cadastro:
        print("Usuário não encontrado.")
        return
    del cadastro[id]
    print("Usuário excluído com sucesso.")

while True:
    print("\n1. Adicionar\n2. Visualizar\n3. Editar\n4. Excluir\n5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        visualizar()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
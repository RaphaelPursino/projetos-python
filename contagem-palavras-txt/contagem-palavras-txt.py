import re
from collections import Counter
import os

def contar_palavras(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            texto = file.read().lower()

        palavras = re.findall(r'\b\w+\b', texto)
        contagem = Counter(palavras)

        print("\nAs 5 palavrar mais frequentes são: ")
        for palavra, freq in contagem.most_common(5):
            print(f"{palavra}: {freq} vezes")

    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo_txt = input("Digite o caminho do arquivo .txt: ")

if os.path.exists(arquivo_txt):
    contar_palavras(arquivo_txt)
else:
    print("Erro: O arquivo não foi encontrado. Verifique o caminho.")
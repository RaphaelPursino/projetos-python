def contar_vogais(frase):
  vogais = "aeiouAEIOU"
  contador = sum(1 for letra in frase if letra in vogais)
  return contador

frase = input("Digite uma frase: ")
print(f"A frase contém {contar_vogais(frase)} vogais.")
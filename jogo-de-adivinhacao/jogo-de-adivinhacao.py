import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número de 1 a 100")

while True:
  tentativa = int(input("Digite seu palpite: "))
  tentativas += 1

  if tentativa < numero_secreto:
    print("O número é maior. Tente novamente.")
  elif tentativa > numero_secreto:
    print("O número é menor. Tente novamente.")
  else:
    print(f"Parabéns. Você acertou em {tentativas} tentativas.")
    break
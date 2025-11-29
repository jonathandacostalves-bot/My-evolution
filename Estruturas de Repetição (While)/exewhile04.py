resposta = "S"
soma = 0

while resposta.upper () != "N":
    numero = int(input("Digite vários números: "))
    soma += numero
    resposta = input("Você deseja continuar? (S/N): ")

print(f"A soma de todos os numeros digitados é {soma}!")


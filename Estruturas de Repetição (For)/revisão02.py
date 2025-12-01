soma = 0
contador = 1


while True:
    numero = int(input("Digite um número: "))
    soma += numero
    if numero == 0:
        break
print(f"A soma é {soma}")
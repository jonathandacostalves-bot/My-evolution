resposta = "S"
primeiro = True
maior_numero = 0

while resposta.upper() != "N":
    numero = int(input("Digite um número: "))

    if primeiro:
        maior_numero = numero
        primeiro = False
    else:
        if numero > maior_numero:
            maior_numero = numero
    
    resposta = input("Deseja continuar (S/N)? ")
    
print(f"O maior número digitado foi {maior_numero}")



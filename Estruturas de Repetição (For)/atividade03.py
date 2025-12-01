resultado = 1
numero = int(input("Digite um número: "))

for n in range (1,numero + 1):
    resultado = resultado * n
    
print(f"O fatorial de {numero} é {resultado}")

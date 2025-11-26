num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um outro numero: "))

if num1 > num2:
    print(f"O {num1} é maior que o {num2}")
elif num1 < num2:
    print(f"O {num2} é maior que o {num1}")
else:
    print("Os numeros são iguais")
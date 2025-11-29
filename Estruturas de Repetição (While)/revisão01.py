n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))

if n1 > n2 and n1 > n3:
    print(f"O numero {n1} é maior que o {n2} e o {n3}")
elif n2 > n1 and  n2 > n3:
    print(f"O número {n2} é maior que o {n1} e o {n3}")
elif n3 > n1 and n3 > n2:
    print(f"O número {n3} é maior todos os numeros {n1} e {n2}") 
else:
      print("Há números iguais, não existe um único maior.")


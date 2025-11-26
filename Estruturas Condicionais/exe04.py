nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
nota3 = float(input("Digite sua 3° nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Em Recuperação")
else:
    print("Reprovado")
    
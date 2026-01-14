alunos = int(input("Digite a quantidade de alunos: "))

for aluno in range(alunos):
    nome = input(f"Digite o nome do aluno {aluno + 1}: ")
    nota1 = float(input("Digite a 1° primeira nota: "))
    nota2 = float(input("Digite a 2° segunda nota: "))
    nota3 = float(input("Digite a 3° terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situação = "aprovado"

    else:
        situação = "reprovado"
    
    print("Nome:", nome)
    print("Notas:", nota1, nota2, nota3)
    print("Média:", media)
    print("Situação:", situação)
    print("---------------------------------------------------")

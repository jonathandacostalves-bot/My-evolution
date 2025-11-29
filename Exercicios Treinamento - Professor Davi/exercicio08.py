# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = float(input("Digite quantos reais você ganha por hora trabalhada: "))
horas = float(input("Digite quantas horas você trabalha no mês: "))

calculo = valor * horas

print("Você recebe", calculo, "por mês trabalhado")

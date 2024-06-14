"""Exercício 08.

Cálculo de Salário
Elabore um programa que calcule o salário mensal de uma pessoa, com base nas horas
trabalhadas por mês e no valor por hora.
"""

horas_mes = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor que você ganha por hora: "))

salario = horas_mes * valor_hora

print("Salário:", salario)
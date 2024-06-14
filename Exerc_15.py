"""Exercício 15.

Cálculo de Salário com Descontos
Escreva um programa que solicite ao usuário o valor que ele ganha por hora e o número
de horas trabalhadas no mês.
Calcule e mostre o salário bruto, os valores descontados para o Imposto de Renda (11%),
o INSS (8%) e o sindicato (5%), além do salário líquido (salário bruto - descontos).
Mostre os dados para o usuário conforme a tabela abaixo:
    (+) Salário bruto: R$
    (-) IR (11%): R$
    (-) INSS (8%): R$
    (-) Sindicato (5%): R$
    (-) Descontos: R$
    (=) Salário líquido: R$
"""

valor_hora_trabalhada = float(input("Informe o valor da hora trabalhada: "))
numero_hora_trabalhadas = float(input("Informe o número de horas trabalhadas: "))
ir = 0.11 
inss = 0.08
sindicado = 0.05
salario_bruto = valor_hora_trabalhada * numero_hora_trabalhadas
descontos = (salario_bruto*ir) + (salario_bruto*inss) + (salario_bruto*sindicado)
print(f"Salario bruto é: R$ {salario_bruto:.2f}".replace('.', ','))
print(f"O total de descontoe é: R$ {descontos:.2f}".replace('.', ','))
salario_liquido = '{:,.2f}'.format(salario_bruto - descontos).replace(',', ' ').replace('.', ',').replace(' ', '.')
print(f"O salário liquido é:R$ {salario_liquido}")

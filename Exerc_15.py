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
IR = 0.11 
inss = 0.08
sindicado = 0.05
salario_bruto = valor_hora_trabalhada * numero_hora_trabalhadas
salario_bruto_formatado = '{:,.2f}'.format(salario_bruto).replace(',', ' ').replace('.', ',').replace(' ', '.')
descontos = (salario_bruto*IR) + (salario_bruto*inss) + (salario_bruto*sindicado)
descontos_formatado = '{:,.2f}'.format(descontos).replace(',', ' ').replace('.', ',').replace(' ', '.')
print(f"Salario bruto é: R$ {salario_bruto_formatado}")
print(f"O total de desconto é: R$ {descontos_formatado}")
salario_liquido = '{:,.2f}'.format(salario_bruto - descontos).replace(',', ' ').replace('.', ',').replace(' ', '.')
print(f"O salário liquido é:R$ {salario_liquido}")



horas_mes = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor que você ganha por hora: "))
 
salario_bruto = horas_mes * valor_hora
 
TAXA_IR = 0.15
TAXA_INSS = 0.08
TAXA_SINDICATO = 0.05
 
valor_ir = salario_bruto * TAXA_IR
valor_inss = salario_bruto * TAXA_INSS
valor_sindicato = salario_bruto * TAXA_SINDICATO
 
descontos = valor_ir + valor_inss + valor_sindicato
salario_liquido = salario_bruto - descontos
 
print(f"(+) Salário bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR ({TAXA_IR * 100:.0f}%): R$ {valor_ir:.2f}")
print(f"(-) INSS ({TAXA_INSS * 100:.0f}%): R$ {valor_inss:.2f}")
print(f"(-) Sindicato ({TAXA_SINDICATO * 100:.0f}%): R$ {valor_sindicato:.2f}")
print(f"(-) Descontos: R$ {descontos:.2f}")
print(f"(=) Salário líquido: R$ {salario_liquido:.2f}")


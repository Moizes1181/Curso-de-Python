#Exercício 12
altura_em_cm= float(input("Digite sua altura em cm: "))
altura = altura_em_cm / 100
print(altura)
peso_ideal = (72.7 * altura) - 58
print(f"O seu peso ideal é: {peso_ideal:.2f}")

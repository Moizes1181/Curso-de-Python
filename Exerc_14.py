limite_captura_peixe_kg = 50
multa_kg_excendente = 4
kg_pescados = float(input("Quantidade total de peixes pescados (em quilos)"))
if kg_pescados <= 50:
   print(f"{kg_pescados}Kg de peixe capturados está dentro do limite de {limite_captura_peixe_kg}kg perimitidos ")
else:
   print(f"{kg_pescados}Kg de peixe capturados ultrapassouo limite de {limite_captura_peixe_kg}kg perimitidos em {kg_pescados - limite_captura_peixe_kg} kg")
   print(f"Gerando uma multa de R$ {(kg_pescados - limite_captura_peixe_kg) * multa_kg_excendente:.2f}".replace('.', ','))

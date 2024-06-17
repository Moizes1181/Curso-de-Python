limite_captura_peixe_kg = 50
multa_kg_excendente = 4
kg_pescados = float(input("Quantidade total de peixes pescados (em quilos)"))
if kg_pescados <= 50:
   print(f"{kg_pescados}Kg de peixe capturados está dentro do limite de {limite_captura_peixe_kg}kg perimitidos")
else:
   print(f"{kg_pescados}Kg de peixe capturados ultrapassouo limite de {limite_captura_peixe_kg}kg perimitidos em {kg_pescados - limite_captura_peixe_kg} kg")
   print(f"Gerando uma multa de R$ {(kg_pescados - limite_captura_peixe_kg) * multa_kg_excendente:.2f}".replace('.', ','))



peso_peixes = float(input("Peso dos peixes em kg: "))
 
PESO_LIMITE = 50
 
excesso = peso_peixes - PESO_LIMITE
excesso = max(excesso, 0)
 
MULTA_POR_KG_EXCESSO = 4
 
multa = excesso * MULTA_POR_KG_EXCESSO
 
print(f"Peso total: {peso_peixes} kg")
print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa:.2f}")


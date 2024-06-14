import io
import sys
captura = io.StringIO()
nome = (input("Digite seu nome: "))
sobrenome = (input("Digite seu sobrenome: "))
saida_original = sys.stdout
sys.stdout = captura
nome_completo = print(f'{nome}{sobrenome}')
sys.stdout = saida_original
conteudo_capturado = captura.getvalue()
captura.close()
conteudo_capturado_maiscuulas = conteudo_capturado.upper()
print('Conteúdo capturado', conteudo_capturado)
print(f'{conteudo_capturado_maiscuulas}')

numero_letras = len(conteudo_capturado.replace(" ", ""))
print(numero_letras)


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
 
# nome_completo = nome + " " + sobrenome
nome_completo = f"{nome} {sobrenome}"
print(nome_completo)
 
numero_letras = len(nome_completo.replace(" ", ""))
print(numero_letras)
 
print(nome_completo.upper())
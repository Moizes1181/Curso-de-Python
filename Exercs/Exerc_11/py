import io
import sys
captura = io.StringIO()
nome = (input("Digite seu nome: "))
sobrenome = (input("Digite seu sobrenome: "))
saida_original = sys.stdout
sys.stdout = captura
nome_completo = print(nome+' '+sobrenome)
sys.stdout = saida_original
conteudo_capturado = captura.getvalue()
captura.close()
print('Conteúdo capturado', conteudo_capturado)

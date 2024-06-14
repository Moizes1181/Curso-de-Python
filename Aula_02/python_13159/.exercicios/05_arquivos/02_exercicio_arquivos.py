"""Exercício 02.

Relatório de Uso do Espaço em Disco
Desenvolva um programa que gere um relatório ordenado do uso de espaço em disco por
usuário, a partir das informações contidas em um arquivo de texto.
O arquivo "usuarios.txt" possui o seguinte formato:
    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125
O programa deve criar um relatório "relatório.txt" no seguinte formato, ordenando os
usuários do que usa mais espaço para o que usa menos:
    ACME Inc.         Uso do espaço em disco pelos usuários
    -------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso

    1    anderson       1187,99 MB           46,02%
    2    rosemary       752,88 MB            29,16%
    3    alexandre      434,99 MB            16,85%
    4    antonio        117,73 MB            4,56%
    5    carlos         87,03 MB             3,37%
    6    cesar          0,94 MB              0,04%

    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB
O arquivo deve ser lido uma única vez.
Após processar os dados, eles devem ser ordenados por espaço utilizado antes de gerar o
relatório final.
"""

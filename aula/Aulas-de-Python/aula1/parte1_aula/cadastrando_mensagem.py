import os

caminho_arquivo = 'C:\\Users\\CARLAL\\OneDrive - Ternium\\Área de Trabalho\\treino\\AulaDevRapidoPython\\exemplo.txt'

with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

caminho_saida = 'C:\\Users\\CARLAL\\OneDrive - Ternium\\Área de Trabalho\\treino\\AulaDevRapidoPython\\exemplo.txt'

with open(caminho_saida, 'w')as arquivo:
    arquivo.write("Aula de python!")

with open(caminho_saida, 'a') as arquivo:
    arquivo.write("\n")
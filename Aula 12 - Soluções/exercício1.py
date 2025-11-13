# Exercício 01
# Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
# A primeira linha deve conter o maior número e a última linha o menor.
# Salve o resultado em outro arquivo (invertido.txt).

# Criando o arquivo pares.txt com números pares de 0 a 999. 
with open("pares.txt", "w") as arquivo_pares: # Abre o arquivo pares.txt para escrita como contexto
    for i in range(0, 1000, 2): # Gera números pares de 0 a 999
        arquivo_pares.write(f"{i}\n") # Grava cada número par no arquivo pares.txt. \n adiciona uma nova linha após cada número

# Resolução do exercício 01
arquivo_pares = open("pares.txt", "r") # Abre o arquivo pares.txt para leitura
# Lê todas as linhas do arquivo e armazena em uma lista
linhas = [] # Cria uma lista vazia para armazenar as linhas do arquivo
for linha in arquivo_pares: # Lê cada linha do arquivo pares.txt
    linhas.append(linha.strip()) # Adiciona a linha lida à lista, removendo espaços em branco no início e no final, inclusive a nova linha \n
# Fecha o arquivo
arquivo_pares.close() # Fecha o arquivo

# Inverte a lista de linhas
linhas.reverse() # Inverte a ordem das linhas na lista

# Abre o arquivo invertido.txt para escrita
arquivo_invertido = open("invertido.txt", "w") # Cria o arquivo invertido.txt para escrita
# Grava as linhas invertidas no arquivo
for linha in linhas: # Para cada linha na lista de linhas
    arquivo_invertido.write(linha + "\n") # Grava a linha no arquivo invertido.txt, adicionando uma nova linha
# Fecha o arquivo
arquivo_invertido.close() # Fecha o arquivo

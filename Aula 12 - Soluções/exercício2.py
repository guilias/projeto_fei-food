# Exercício 02
# Crie um arquivo: “numeros.txt” que contenha 100 números
# aleatórios;
# Todos os números do arquivo estão na mesma e única linha,
# separados por espaço;
# Escreva uma função em Python para retornar a somatória de
# todos os números que estão armazenados no arquivo
# “numeros.txt”.

# Importa a biblioteca random para gerar números aleatórios
import random

arquivo_numeros = open("numeros.txt", "w") # Cria o arquivo numeros.txt para escrita
# Gera 100 números aleatórios entre 0 e 1000
for i in range(100): # Para cada número de 0 a 99
    numero = random.randint(0, 1000) # Gera um número aleatório entre 0 e 1000
    arquivo_numeros.write(f"{numero} ") # Grava o número no arquivo, seguido de um espaço
# Fecha o arquivo
arquivo_numeros.close() # Fecha o arquivo

# Função para calcular a somatória dos números no arquivo numeros.txt
def somar_numeros(arquivo):
    """
    Função para somar os números contidos em um arquivo.
    :param arquivo: Nome do arquivo que contém os números.
    :return: Soma dos números contidos no arquivo.
    """
    # Abre o arquivo para leitura
    arquivo = open(arquivo, "r") # Abre o arquivo numeros.txt para leitura
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
    # Fecha o arquivo
    arquivo.close() # Fecha o arquivo
    # Converte o conteúdo em uma lista de números
    for i in conteudo.split(): # Divide o conteúdo em uma lista de números, separando por espaços
        i = int(i) # Converte cada número em inteiro, lembrando que o conteúdo é uma string
        
    # Calcula a soma dos números
    soma = 0 # Inicializa a variável soma com 0
    for i in conteudo.split(): # Para cada número na lista de números
        soma += int(i) # Adiciona o número à soma
    
    return soma # Retorna a soma dos números

# Chama a função somar_numeros e imprime o resultado
resultado = somar_numeros("numeros.txt") # Chama a função somar_numeros passando o nome do arquivo
print("A soma dos números no arquivo numeros.txt é:", resultado) # Imprime o resultado da soma
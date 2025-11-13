# Exercício 03
# Crie um arquivo: “numeros.txt” que contenha 100 números
# aleatórios;
# Escreva uma função que leia uma sequência numérica do arquivo
# “numeros.txt” e salva os números na lista num.
# Escreva outra função que recebe a lista num como parâmetro e
# retorna uma nova lista num_unicos, sem os elementos repetidos.
# Escreva uma terceira função que recebe a lista num_unicos e
# grava os números no arquivo “numeros_unicos.txt”.

# Importa a biblioteca random para gerar números aleatórios
import random

def main():
    """
    Função principal que chama as outras funções para gerar números, ler do arquivo,
    remover duplicados e gravar os números únicos em um novo arquivo.
    """
    gerar_numeros() # Chama a função gerar_numeros para criar o arquivo numeros.txt
    numeros = ler_numeros("numeros.txt") # Chama a função ler_numeros passando o nome do arquivo
    numeros_unicos = remover_duplicados(numeros) # Chama a função remover_duplicados passando a lista de números
    gravar_numeros_unicos(numeros_unicos, "numeros_unicos.txt") # Chama a função gravar_numeros_unicos passando a lista de números únicos e o nome do arquivo
    print("Os números únicos foram gravados no arquivo numeros_unicos.txt") # Imprime mensagem de sucesso

def gerar_numeros():
    """
    Função para gerar 100 números aleatórios entre 0 e 1000 e gravá-los em um arquivo.
    """
    # Abre o arquivo numeros.txt para escrita
    arquivo_numeros = open("numeros.txt", "w") # Cria o arquivo numeros.txt para escrita
    # Gera 100 números aleatórios entre 0 e 1000
    for i in range(100): # Para cada número de 0 a 99
        numero = random.randint(0, 1000) # Gera um número aleatório entre 0 e 1000
        arquivo_numeros.write(str(numero) + " ") # Grava o número no arquivo, seguido de um espaço
    # Fecha o arquivo
    arquivo_numeros.close() # Fecha o arquivo

# Função para ler os números do arquivo numeros.txt e armazená-los em uma lista
def ler_numeros(arquivo):
    """
    Função para ler os números contidos em um arquivo e armazená-los em uma lista.
    :param arquivo: Nome do arquivo que contém os números.
    :return: Lista de números contidos no arquivo.
    """
    # Abre o arquivo para leitura
    arquivo = open(arquivo, "r") # Abre o arquivo numeros.txt para leitura
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
    # Fecha o arquivo
    arquivo.close() # Fecha o arquivo
    # Converte o conteúdo em uma lista de números
    numeros = []
    for i in conteudo.split(): # Para cada número na lista de números
        numeros.append(int(i)) # Adiciona o número à lista
    
    return numeros # Retorna a lista de números

# Função para remover os números duplicados da lista
def remover_duplicados(numeros):
    """
    Função para remover os números duplicados de uma lista.
    :param numeros: Lista de números.
    :return: Lista de números únicos.
    """
    numeros_unicos = [] # Inicializa a lista de números únicos
    for numero in numeros: # Para cada número na lista de números
        if numero not in numeros_unicos: # Verifica se o número não está na lista de números únicos
            numeros_unicos.append(numero) # Adiciona o número à lista de números únicos
    
    return numeros_unicos # Retorna a lista de números únicos

# Função para gravar os números únicos no arquivo numeros_unicos.txt
def gravar_numeros_unicos(numeros_unicos, arquivo):
    """
    Função para gravar os números únicos em um arquivo.
    :param numeros_unicos: Lista de números únicos.
    :param arquivo: Nome do arquivo onde os números serão gravados.
    """
    # Abre o arquivo para escrita
    arquivo = open(arquivo, "w") # Cria o arquivo numeros_unicos.txt para escrita
    # Grava os números únicos no arquivo
    for numero in numeros_unicos: # Para cada número na lista de números únicos
        arquivo.write(str(numero) + " ") # Grava o número no arquivo, seguido de um espaço
    
    # Fecha o arquivo
    arquivo.close() # Fecha o arquivo

# Chama a função main para executar o programa
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main() # Chama a função main
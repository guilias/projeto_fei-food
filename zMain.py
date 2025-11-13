login = False
usuario = 0

# Menu principal
menu = {
    1: "Novo pedido",
    2: "Cardápio",
    3: "Avaliar",
    0: "Desconectar-se"
}

# Tela de login/cadastro
telaInicial = {
    1: "Iniciar sessão",
    2: "Cadastrar-se",
    0: "Sair"
}

# Cardápio do Fei-Food
cardapio = {
    1: ("Hambúrguer Artesanal", 100), #alimento, valor
    2: ("Coca Zero Plus", 50),
    3: ("Batata Frita Gourmet", 75)
}

# Menu que faz parte da função novoPedido()
novoPedidoMenu = {
    1: "Adicionar item ao carrinho",
    2: "Remover item do carrinho",
    3: "Ver carrinho",
    4: "Finalizar pedido",
    0: "Cancelar pedido"
}

# Função principal
def main():
    global login
    global usuario
    print("\nOlá! Boas vindas ao FEI-FOOD.\n")
    exibirTelaInicial()
    while login == True:
        escolha = exibirMenu()
        if escolha == 1:
            novoPedido()
        elif escolha == 2:
            verCardapio()
        elif escolha == 3:
            avaliar()
        elif escolha == 0:
            login = False
            usuario = 0
            print("\nTchau!\n")
            break
        else:
            print("\nERRO! Opção inválido. Tente novamente.\n")

# Exibe a tela de login/cadastro para usuário.
def exibirTelaInicial():
    global login
    while login == False:
        print("Boas vindas ao FEI-FOOD! Selecione uma opção:")
        for opcao, descricao in telaInicial.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("\nDigite a opção desejada: "))
        if escolha == 1:
            entrar()
        elif escolha == 2:
            cadastrar()
        else:
            print("\nERRO! Opção inválido. Tente novamente.\n")

# Conectar-se à uma conta existente
def entrar():
    global login, usuario

    print("\nOk! Vamos iniciar sessão com uma conta existente!")
    while login == False:
        entrarNome = (input("Usuário: "))

        with open("usuarios.txt", "r", encoding="utf-8") as usuarios:
            conteudo = usuarios.readlines()
            for linha in conteudo:
                nome, senha = linha.strip().split(",")

                if entrarNome.lower() == nome.lower():
                    for tentativas in range(3):
                        entrarSenha = (input("Senha: "))
                        if entrarSenha == senha:
                            login = True
                            usuario = nome
                            print("\nIniciando sessão...")
                            return
                        else:
                            print("Senha incorreta!!!\n")
                    print("\nVocê excedeu o número de tentativas. Retornando à tela inicial...\n")
                    break
            else:
                print("\nUsuário não encontrado. Tente novamente.\n")

# Criar um novo usuário
def cadastrar():
    with open("usuarios.txt", "a", encoding="utf-8") as usuarios:
        print("\nOk! Vamos criar um nome de usuário e senha para você.")
        cadastrar_nome = (input("\nDigite um nome de usuário: "))
        cadastrar_senha = (input("Crie uma senha: "))
        usuarios.write(f"{cadastrar_nome},{cadastrar_senha}\n")
        print("\nUsuário e senha criados com sucesso!\n")

# Função que exibe o menu principal
def exibirMenu():
    print(f"\nComo podemos te ajudar, {usuario}?")
    print("\nMENU:")
    while True:
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("\nDigite a opção desejada: "))
        if escolha < 0 or escolha > 4:
            print("\nERRO! Opção inválida. Tente novamente.\n")
        else:
            return escolha

# !!!
# !!!
# Abaixo, funções que fazem parte do MENU PRINCIPAL:

def novoPedido():
    print("\nNOVO PEDIDO:")
    for opcao, descricao in novoPedidoMenu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("\nDigite a opção desejada: "))
    if escolha == 1:
        pass
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    elif escolha == 4:
        pass
    elif escolha == 0:
        return
    else:
        print("\nERRO! Opção inválido. Tente novamente.\n")


    with open("pedidos.txt", "a", encoding="utf-8"):
    # escrevendo
        pass

def verCardapio():
    print("\nCARDÁPIO:")
    for id, (alimento, valor) in cardapio.items():
        print(f"{id}. {alimento} - R${valor}")
        input("\nDigite qualquer tecla para continuar: ")

def avaliar():
    pass

# !!!
# !!!
# Abaixo, funções que fazem parte do MENU PARA NOVOS PEDIDOS:

def adicionarItem():
    pass

def removerItem():
    pass

def verCarrinho():
    pass

def finalizarCompra():
    pass


# Chamada da função principal, que encadeia um chamado para todas as outras, a depender das entradas do usuário.
main()
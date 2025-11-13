login = False
usuario = 0

# Menu principal
menu = {
    1: "Novo pedido",
    2: "Cardápio",
    3: "Avaliar um pedido",
    4: "Ver avaliações",
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
        # Fazer novo pedido
        if escolha == 1:
            novoPedido()
        
        # Visualizar cardápio
        elif escolha == 2:
            verCardapio()
            input("\nDigite qualquer tecla para continuar: ")

        # Avaliar um pedido finalizado
        elif escolha == 3:
            avaliar()

        elif escolha == 4:
            verAvaliacoes()

        # Sair do "aplicativo"
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
        # Iniciar sessão
        if escolha == 1:
            entrar()
        # Criar novo usuário
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
    carrinho = [] # Define uma lista vazia. Os itens serão armazenados aqui!
    while True:
        print("\nNOVO PEDIDO:")
        for opcao, descricao in novoPedidoMenu.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("\nDigite a opção desejada: "))
        
        # Adiciona item ao pedido 
        if escolha == 1: 
            verCardapio()
            
            escolhaCardapio = int(input("\nEscolha o item que deseja adicionar ao carrinho: "))

            if escolhaCardapio in cardapio:
                alimento, valor = cardapio[escolhaCardapio]
                carrinho.append(f"{alimento};{valor}")
                print(f"\nItem {escolhaCardapio} adicionado ao carrinho!")
                print(carrinho)
            else:
                print("\nOpção inválida. Retornando ao menu de pedidos...")

        # Remove item do pedido
        elif escolha == 2:
            if not carrinho:
                print("\nO carrinho já está vazio! Não há o que remover.")
                continue
            else:
                print("\nSeu carrinho até agora:")
                for i in range(len(carrinho)):
                    alimento, valor = carrinho[i].split(';')
                    print(f"{i + 1}. {alimento} (R${valor})")
                removerItem = int(input("\nDigite o número do item que quer remover: "))

                # Primeiro, verifica se a entrada do usuário é PELO MENOS 1, depois, se essa entrada NÃO é maior que o número de itens
                if 1 <= removerItem <= len(carrinho):
                    itemRemovido = carrinho.pop(removerItem - 1) # Para a máquina, a lista começa em zero, por isso a subtração. 
                    print(f"\nO item '{itemRemovido.split(';')[0]}' foi removido do carrinho.")
                else:
                    print("\nNúmero inválido.")

        # Visualiza iteNS no carrinho
        elif escolha == 3:
            print("\nSeu carrinho até agora:")
            for i in range(len(carrinho)):
                alimento, valor = carrinho[i].split(';')
                print(f"{i + 1}. {alimento} (R${valor})")

        # Finaliza pedido e retorna ao menu principal
        elif escolha == 4:
            if not carrinho:
                print("\nO carrinho está vazio. Adicione itens à ele, ou cancele o pedido para continuar.")
                continue
            else:
                with open("pedidos.txt", "a", encoding="utf-8") as pedidos:
                    itensFormatados = ";".join(carrinho)
                    pedidos.write(f"\n{usuario},{itensFormatados}")
                print("\nPedido finalizado com sucesso!")
            return

        # Cancela pedido e retorna ao menu principal
        elif escolha == 0:
            return
        
        # Caso a opção desejada não esteja no menu:
        else:
            print("\nERRO! Opção inválido. Tente novamente.\n")


def verCardapio():
    print("\nCARDÁPIO:")
    for id, (alimento, valor) in cardapio.items():
        print(f"{id}. {alimento} - R${valor}")

def avaliar():
    temPedido = False
    with open("pedidos.txt", "r", encoding="utf-8") as pedidos:
        pedidos.seek(0)
        for linha in pedidos:
            partes = linha.strip().split(",")
            if partes and partes[0].lower() == usuario.lower():
                temPedido = True
                break

    if not temPedido:
        print("\nVocê não possui pedidos finalizados para avaliar.\n")
        return
    
    # Caso o usuário possua pedidos realizados, inicia a avaliação.
    print(f"\nCerto, {usuario}, vamos registrar a sua avaliação!")

    nota = 0
    while True:
        notaUsuario = int(input("Digite sua nota (de 1 à 5): "))
        if 1 <= notaUsuario <= 5:
            nota = notaUsuario
            break
        else:
            print("\nNota inválida. Tente novamente.")
    
    comentario = input("Digite seu comentário: ")
    if not comentario:
        comentario = "Nenhum comentário."
    
    # Salva a avaliação
    with open("avaliacoes.txt", "a", encoding="utf-8") as avaliacoes:
        # Formato: usuario,nota,comentario
        avaliacoes.write(f"{usuario},{nota},{comentario}\n")
    print("\nAvaliação registrada com sucesso!")

def verAvaliacoes():
    print("AVALIAÇÕES FEI-FOOD:")
    with open("avaliacoes.txt", "r", encoding="utf-8") as avaliacoes:
        avaliacoes.seek(0) # Vai para o início para ler
        linhas = avaliacoes.readlines()
        if not linhas:
            print("Ainda não há nenhuma avaliação registrada.")
        
        for linha in linhas:
            partes = linha.strip().split(",", 2)
            
            if len(partes) == 3:
                nome, nota, comentario = partes
                print(f"\nUsuário: {nome}")
                print(f"Nota: {nota}/5")
                print(f"Comentário: {comentario}\n")

# Chamada da função principal, que encadeia um chamado para todas as outras, a depender das entradas do usuário.
main()
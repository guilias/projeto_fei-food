menu = {
    1: "Novo pedido",
    2: "Cardápio",
    3: "Avaliar"
}

def main():
    while True:
        escolha = exibirMenu()
        if escolha == 1:
            a = a



def exibirMenu():
    print("Menu:")
    while True:
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("\nDigite o número da opção desejada: "))
        if escolha < 0 or escolha > 4:
            print("\nERRO: Número inválido. Digite uma opção novamente.\n")
        else:
            return escolha


print("Boas vindas ao FEI FOOD! Como podemos te ajudar hoje?\n")
main()
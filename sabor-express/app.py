import os

# listas
restaurantes = ["Pizza", "Sushi"]

def definir_nome_do_programa():
    print("""

    🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢

""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("clear")
    print("Aplicação finalizada\n")

def opcao_invalida():
    print("Opção Invalida\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def cadastrar_novo_restaurante():
    os.system("clear")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def listar_restaurantes():
    os.system("clear")
    print("Listando os restaurantes\n")
    for restaurante in restaurantes:
        print(f".{restaurante}")
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida: # match é o switch case
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                print("Opcao invalida")
    except:
        opcao_invalida()

def main():
    os.system("clear")
    definir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
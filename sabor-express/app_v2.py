import os

# listas
# restaurantes = ["Pizza", "Sushi"] -> Listas
restaurantes = [
    {"nome": "Sushizica", "categoria":"Japonesa", "ativo":False},
    {"nome": "PizzaDaVéia", "categoria":"Italiana", "ativo":True},
    {"nome": "Cafezin", "categoria":"Cafe", "ativo":False}
]


def definir_nome_do_programa():
    """
        Esta função tem o proposito de apresentar o titulo da aplicação de forma estilizada.
    """
    print("""

    🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢

""")

def exibir_opcoes():
    """
        Esta função tem o proposito de listar/exibir os tipos de entradas que aplicação utiliza como menu.
    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar estado do restaurante")
    print("4. Sair\n")

# funcoes default app
def voltar_ao_menu_principal():
    """
        Esta função tem o proposito de fornecer recursos basicos para outras funções como voltar ao menu.
    """
    input("\nDigite uma tecla para voltar ao menu: ")
    main()

def exibir_subtitulo(texto):
    """
        Esta função tem o proposito de fornecer de forma estilizada os subtitulos dos itens de menu quando são acessadas.
    """
    os.system("clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# funcoes do menu
def finalizar_app():
    exibir_subtitulo("Aplicação finalizada")

def opcao_invalida():
    print("Opção Invalida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | "Status"')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado" # ternario - adicionando Label
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"] # inverte o valor encontrado
            mensagem = (f"O restaurante {nome_restaurante} foi ativado com sucesso") if restaurante["ativo"] else (f"O restaurante {nome_restaurante} foi desativado com sucesso")
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida: # match é o switch case
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
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
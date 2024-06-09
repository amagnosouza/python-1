"""
# 1 - Solicite ao usuário que insira um número e, 
em seguida, use uma estrutura if else 
para determinar se o número é par ou ímpar.
"""
num = int(input("Digite um numero inteiro para saber se ele é impar ou par: "))
if num % 2 == 0:
    print(f"O numero {num} é par")
else:
    print(f"O numero {num} é impar")

"""
# 2 - Pergunte ao usuário sua idade e, com base nisso, 
use uma estrutura if elif else para classificar a idade
em categorias de acordo com as seguintes condições:
Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""
idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Você é uma criança")
elif 13 <= idade <= 18:
    print("Você é um(a) adolescente")
else:
    print("Você é um adulto")

"""
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else 
para verificar se o nome de usuário e a senha fornecidos 
correspondem aos valores esperados determinados por você.
"""
nome = input("Digite o nome: ")
senha = input("Digite a senha: ")
if nome == "joao" and senha == "asdf123":
    print("Login realizado com sucesso")
else:
    print("Voce errou")
"""
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e 
utilize uma estrutura if elif else para determinar em qual quadrante do plano 
cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""
x = int(input("Digite o valor do ponto X: "))
y = int(input("Digite o valor do ponto Y: "))
if x > 0 and y > 0:
    print("Primeiro Quadrante")
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif x < 0 and y < 0:
    print("Tereceiro Quadrante")
elif x > 0 and y < 0:
    print("Quarto Quadrante")
else:
    print("o ponto está localizado no eixo ou origem")

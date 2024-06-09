# 1 - Crie uma lista para cada informação a seguir:
"""
Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""
list_num = [1,2,3,4,5,6,7,8,9,10]
list_nome = ["João", "Pepa", "Maria", "Pedro"]
list_ano = [1992,2024]

# 2- Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for num in list_num:
    print(num)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
num_impar = []
for num in list_num:
    if num % 2 == 1:
        num_impar.append(num)
print(sum(num_impar))

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for num in reversed(list_num):
    print(num)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
valor = int(input("Digite um numero: "))
for num in range(1,11):
    print(f"{valor} X {num} eh: {valor*num}")
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista = [1,3,5, "teste"]
soma = 0
try:
    for num in lista:
        soma += num
    print(soma)
except Exception as e:
    print:(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista = [2,2,2, ""]
soma = 0
try:
    for num in lista:
        soma += num
    media = soma / len(lista)
    print(f"A média da lista eh: {media}")
except ZeroDivisionError:
    print("Lista vazia")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {
    "nome":"joao",
    "idade":20,
    "cidade":"Brasilia"
}

#2 - Utilizando o dicionário criado no item 1:
"""
Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""
pessoa.update({"idade":25})
print(pessoa)
pessoa.update({"profissao":"tecnologia"})
print(pessoa["profissao"])
pessoa.pop("profissao")
print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if "nome" in pessoa:
    print("Existe a chave")
else:
    print("não existe a chave")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada finibus sem, ac semper massa finibus eget. Nulla cursus mauris diam. Aliquam sodales metus at sapien faucibus, nec tempus nisl feugiat. Phasellus eget metus accumsan, congue lectus sed, malesuada neque. Proin ac sem nec orci fermentum fermentum. Pellentesque dictum pretium eros, id ullamcorper nulla dignissim eu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse quis consectetur turpis, sit amet dignissim urna. Proin ornare id tellus vitae gravida. Praesent vestibulum mi enim, vel viverra mi porttitor vel."
conta_palavra = {}
palavras = frase.split()
for palavra in palavras:
    conta_palavra[palavra] = conta_palavra.get(palavra, 0) + 1
print(conta_palavra)
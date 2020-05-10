# exemplo de lista de argumentos
def unir_palavras(*args):
    palavra = "".join(args)
    return palavra

lista = ["re", "na", "to"]
resultado = unir_palavras(*lista)
print(resultado)

lista2 = ["pa", "la", "vra", " ", "maior"]
resultado2 = unir_palavras(*lista2)
print(resultado2)

# exemplo de dicionario de argumentos
def despesas_mensais(**kwargs):
    despesa = 0
    grandes_despesas = []
    for nome,valor in kwargs.items():
        despesa += valor
        if valor > 500:
            grandes_despesas.append(nome)
    print("Sua despesa total mensal foi de {0} reais.".format(despesa))
    if grandes_despesas == []:
        print("E você não teve grandes despesas")
    else:
        print("Suas despesas maiores que 500 reais foram referentes à:")
        for despesas in grandes_despesas:
            print("\t{0}".format(despesas))

despesas_mensais(Carro = 500,Telefone = 50, Viagem = 550, Aluguel = 1000, Compras = 80)
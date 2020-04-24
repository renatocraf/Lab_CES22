def sum_list(lista):
    par = False
    cont = 0
    sum = 0
    # preferi utilizar o while para nao ter que usar o 'break'
    # quando encontrasse o par
    while (cont < len(lista) and par == False):
        if(lista[cont]%2 ==0):
            par = True
        else:
            sum = sum + lista[cont]
        cont = cont+1

    return (sum)

# printando na tela as respostas dos testes:

# resposta 25
lista1 = [1,3,5,7,9,10]
print(sum_list(lista1))

# resposta 4
lista2 = [1,3,4,5,7,9,10]
print(sum_list(lista2))

# resposta 16
lista3 = [1,3,5,7,8,9,10]
print(sum_list(lista3))

# resposta 25
# se não houver números pares, soma todos os números da lista
lista4 = [1,3,5,7,9]
print(sum_list(lista4))


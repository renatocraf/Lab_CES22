def contar_lista(lista):
    cont = 0
    sam = False
    while(cont < len(lista) and sam == False):
        if (lista[cont] == "sam"):
            sam = True;
        cont= cont +1
    return(cont)

# teste 1
lista = [ 1,"samara", "sam", 10, "setembro"]
# resposta deve ser 3
print(contar_lista(lista))

# teste 2(sem a ocorrência da palavra "sam"
lista2 = [ 1, "samara", 10, "setembro"]
#resposta deve ser 4
print(contar_lista(lista2))


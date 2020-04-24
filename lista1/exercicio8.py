#formatação da primeira linha
print("     ",end = "")
for i in range(1,13):
    print('{:>4}'.format(i), end = "")

#formatação da segunda linha    
print("\n    :",end="")
for i in range(1,4*12+1):
    print("-",end="")   
print("")

#formatação das linhas da tabela
for i in range(1,13):
    #printa o numero da linha
    print('{:>4}'.format(i)+":", end = "")
    #printa os valores da multiplicacao da linha pela respectiva coluna
    for k in range(1,13):
        print('{:>4}'.format(i*k),end = "")
    print("")

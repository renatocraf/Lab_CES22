def addition_complex(n1,n2):
    return(n1[0]+n2[0],n1[1]+n2[1])

# definindo a função teste
def test(bool):
    if bool:
        print("Teste OK")
    else:
        print("Teste falhou")

#numeros complexos
n1 = (1,2)
n2 = (3,4)
n3 = (5,7)
n4 = (1,-4)

#testes
test(addition_complex(n1,n2)==(4,6))
test(addition_complex(n1,n3)==(6,9))
test(addition_complex(n2,n3)==(8,11))
test(addition_complex(n3,n4)==(6,3))

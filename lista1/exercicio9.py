def is_palindrome(lista):
    #cria a variavel invertendo a lista
    lista_reversa = lista[::-1]
    pali = True
    #fazendo a verificação letra por letra
    for i in range(int(len(lista)/2)):
        if(lista[i] != lista_reversa[i]):
            pali = False
            # se a letra for diferente, da um 'break' para sair do for
            break

    return (pali)

# definindo a função teste
def test(bool):
    if bool:
        print("Teste OK")
    else:
        print("Teste falhou")

#listas usadas para o teste
lista = "renato"
lista1 = "abba"
lista2 = "abab"
lista3 = "tenet"
lista4 = "banana"
lista5 = "straw warts"
lista6 = "a"

#testes
test(not is_palindrome(lista))
test(is_palindrome(lista1))
test(not is_palindrome(lista2))
test(is_palindrome(lista3))
test(not is_palindrome(lista4))
test(is_palindrome(lista5))
test(is_palindrome(lista6))

'''
Após fazer um programa, pode ser que seja trabalhoso demais alterar o código.
Uma alternativa que ajuda a diminuir esse trabalho é o uso de decoradores.
Os decoradores permitem que sejam feitas modificações de outras funções a partir de uma função decoradora
'''

def hashtag_decorador(func):
    def add_hashtag(num1,num2):
        return "############# "+func(num1,num2)+" #############"
    return add_hashtag

@hashtag_decorador
def multiplicar(num1,num2):
    return "Resultado: %g"%(num1 *num2)

a = multiplicar(2,3)
print(a)


from math import sqrt
from math import ceil
from datetime import date,timedelta

def is_prime(n):
    primo = False
    if(n!=2):
        # a busca sera feita por divisores ate o proximo numero inteiro
        # da raiz quadrada do numero pedido
        for i in range(2,ceil(sqrt(n))):
            if(n%i == 0):
                primo = False
                break
            else:
                primo = True
    return (primo)

# definindo a função teste
def test(bool):
    if bool:
        print("Teste OK")
    else:
        print("Teste falhou")

#testes
test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
#eu nasci em 24/11/1990, que nao é um numero primo, como pode-se verificar no teste
test(not is_prime(19901124))

#eu sou o mais velho da turma e considerando que o mais novo nasceu antes de 2004, temos:
maisvelho = date(1990,11,24)
maisnovo = date(2004,1,1)
#diferença esta em timedelta
dif = maisnovo-maisvelho

#criando uma tupla com as datas entre o mais novo e o mais velho e se essa data eh primo ou nao
dia = maisvelho
lista = []
quant = 0
while (dia != maisnovo):
    numero = str(dia.year)+str(dia.month)+str(dia.day)
    primo = is_prime(int(numero))
    lista.append((numero,primo))
    #caso seja primo, vamos adicionar uma unidade na variavel quant
    if primo:
        quant +=1
    dia = dia +timedelta(days=1)

#vamos calcular a percentagem de dias primos em todos esse dias verificados
porcentagem = (quant/dif.days)
#multiplicando essa percentagem pela quantidade de alunos(100) e arredondando
alunos_dias_primos = 100* porcentagem
#verifica-se que o aproximadamente 7 alunos nascem em dias primos
print(round(alunos_dias_primos))


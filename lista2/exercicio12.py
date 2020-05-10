

'''
No Duck Typing o tipo ou a classe de um objeto é menos importante que os métodos que o define.
Ao invés de checar a classe ou o tipo de dado, é checada a presença ou não de métodos ou atributos específicos.

'''
'''
Para mostrar o Polimorfismo, foi aperfeiçoado o exemplo criado no exercício 8.

'''
class Conta():
    numero = 0
    @classmethod
    def quantidade_contas(cls):
        return cls.numero

    @staticmethod
    def boas_vindas():
        print("Bem Vindo à sua conta")

    def __init__(self, saldoinicial):
        self.saldo = saldoinicial
        
        self.__numeroconta = Conta.numero+1
        Conta.numero = self.__numeroconta
    
    def depositar(self,valor):
        self.saldo += valor
    
    def mostrarsaldo(self):
        return self.saldo

    def render(self,juros):
        #raise NotImplementedError("Utilização Apenas em Investimentos")
        pass

class Poupanca(Conta):
    def render(self,juros):
        self.saldo = self.saldo + juros*(self.saldo)

class ContaCorrente(Conta):
    def depositar(self,valor):
        custo_deposito = 10
        self.saldo = self.saldo + valor - custo_deposito

''' nessa função foi utilizado um nome generico (conta), nao sendo definido se era poupanca ou conta corrente
    e mesmo assim foram utilizados os metodos depositar e render, constantes na classe Conta.
    O Duck Typing entra em ação quando a função é rodada, descobrindo qual a tipagem/classe da variável conta
'''
def debitoautomatico(conta,valor,tempo):
    for mes in range(tempo):
        conta.depositar(valor)
        conta.render(0.0048)
        #saldo = conta.mostrarsaldo()
        print('O valor depositado no mes {0} foi de R${1:.2f}'.format(mes+1,valor))
    print('O valor ao final do período é de R${:.2f}\n' .format(conta.mostrarsaldo()))




conta1 = Poupanca(200)
conta2 = ContaCorrente(100)
conta2.depositar(50)
conta1.render(0.0048)
valor1 = conta1.mostrarsaldo()
valor2 = conta2.mostrarsaldo()

print(valor1)
print(valor2)

conta3 = Poupanca(200)
conta4 = ContaCorrente(200)

debitoautomatico(conta3,100,12)
debitoautomatico(conta4,100,12)
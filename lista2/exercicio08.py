class Conta():
    numero = 0
    
    # método de classe: é o metodo específico da classe(não é ligado a instâncias), ele mexe com os atributos da classe
    # vantagem: podemos verificar algumas características de como está aquela classe durante a execução do programa
    #           no exemplo abaixo podemos perceber quantas contas já foram criadas no momento
    @classmethod
    def quantidade_contas(cls):
        return cls.numero

    # método estáticos: é o método que não precisa de uma referência.
    # vantagem : simplicidade
    @staticmethod
    def boas_vindas():
        print("Bem Vindo à sua conta")

    def __init__(self, saldoinicial):
        self.__saldo = saldoinicial
        
        self.__numeroconta = Conta.numero+1
        Conta.numero = self.__numeroconta
    
    
    def depositar(self,valor):
        self.__saldo += valor
    
    
    def mostrarsaldo(self):
        return self.__saldo

    # método abstrato: é um método que será implementado em suas classes filhas
    def render(juros):
        raise NotImplementedError("Utilização Apenas em Investimentos")

conta1 = Conta(250)
Conta.boas_vindas()
print("Contas Existentes: {0}".format(Conta.quantidade_contas()))
a = conta1.mostrarsaldo()
print("Saldo da Conta: {0}" .format(a))
conta1.depositar(100)
print("Novo saldo: {0}".format(conta1.mostrarsaldo()))


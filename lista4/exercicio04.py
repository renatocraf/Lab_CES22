'''
Uma aplicação para um Banco executa operações tais como verificar saldos, extratos, 
realizar transferências, etc. Utilize o Design Pattern Command para modelar o processamento 
de solicitações do cliente para a aplicação do Banco. Implemente um programa em Python para 
simular a interação entre a aplicação cliente e a aplicação do Banco (Crie uma interface gráfica 
com botões para ativar os comandos. Utilize o pacote TKinter https://docs.python.org/3/library/tkinter.html). 
A aplicação cliente deverá implementar um histórico de comandos realizados.
'''
import tkinter as tk
from abc import abstractmethod

# Essa classe seria a receiver
class Conta():
    def __init__(self, nome,valorinicial = 0):
        self.valor = valorinicial
        self.nome = nome
    
    def saldo(self):
        return(self.valor)

    def depositar(self, valor):
        self.valor += valor
        
    def retirar(self,valor):
        if (valor< self.valor):
            self.valor -= valor
            return True
        else:
            return False

#classe comando

class Command():

    @abstractmethod
    def trocarusuario(self,user,usersubstituto):
        pass

    @abstractmethod
    def verificarsaldo(self,user):
        pass

    @abstractmethod
    def depositarvalor(self,user,valor):
        pass

    @abstractmethod
    def retirarvalor(self,user,valor):
        pass

    @abstractmethod
    def transferirvalor(self,userenvia,userrecebe,listausers,valor):
        pass

class VerificaSaldo(Command):
    def __init__(self):
        self.frase = str("Seu saldo é ")

    def verificarsaldo(self,user):
        return str(f"{self.frase}" f"{user.saldo()}" f".")    

class DepositaValor(Command):
    def __init__(self):
        self.frase = str("Você depositou ")

    def depositarvalor(self,user,valor):
        user.depositar(valor)
        return str(f"{self.frase}" f"{valor}" f".")

class TrocarUsuario(Command): 
    def __init_(self):
        self.erro = str("Usuario nao cadastrado")

    def trocarusuario(self,user,usersubstituto):
        if(usersubstituto != 0):
            return usersubstituto
        else:
            return user
    
class RetirarValor(Command):
    def __init__(self):
        self.frase = str("Você retirou ")
        self.erro = str("Seu saldo não é suficiente.")

    def retirarvalor(self,user,valor):
        self.saldopositivo = user.retirar(valor)
        if (self.saldopositivo):
            return str(f"{self.frase}" f"{valor}")
        else:
            return self.erro

class TransferirValor(Command):
    def __init__(self):
        self.frase = str("Você transferiu ")
        self.erro = str("Seu saldo não é suficiente.")

    def transferirvalor(self,userenvia,userrecebe,valor):
        self.saldopositivo = userenvia.retirar(valor)
        if (self.saldopositivo):
            userrecebe.depositar(valor)
            return str(f"{self.frase}" f"{valor}")
        else:
            return self.erro
               

#invoker
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Banco do CES-22")
        self.pack()

        #criando usuarios
        self.user1 = Conta("Renato",300)
        self.user2 = Conta("Samara",400)
        self.user3 = Conta("Nickolas",0)
        self.listausuario = [self.user1, self.user2, self.user3]
        # setando usuario que estara logado no sistema 
        self.userlogado = self.user1  
        
        self.historico = "Histórico:"
        self.criar_e_posicionarpacker()
        self.logarusuario()
               
        
    def logarusuario(self):
        self.label_usuariologado['text']= str(f"Usuário logado: " f"{self.userlogado.nome}")

    def att_historico(self,frase):
        self.historico +="\n"+frase
        self.label_transacaoexecutada['text'] = self.historico

    def criar_e_posicionarpacker(self):
        #setando botoes
        self.botao_trocauser = tk.Button(self,text = "Trocar Usuario", command = self.trocauser)
        self.botao_verificasaldo = tk.Button(self,text = "Consultar Saldo",command = self.verificasaldo)
        self.botao_depositavalor = tk.Button(self,text = "Depositar Valor",command = self.depositavalor)
        self.botao_retirarvalor = tk.Button(self,text = "Realizar Saque",command = self.retiravalor)
        self.botao_transferirvalor = tk.Button(self,text = "Transferir Valor", command = self.transferevalor)

        #setando labels
        self.label_usuariologado = tk.Label(self,text = "Usuario logado: fulano")
        self.label_transacaoexecutada = tk.Label(self,text = self.historico)
        self.label_valor_deposito = tk.Label(self,text = "Valor")
        self.label_usuario = tk.Label(self,text = "Usuario")
        
        #setando entry
        self.entrada_novousuario = tk.Entry(self)
        self.entrada_valor_deposito = tk.Entry(self)
        self.entrada_valor_saque = tk.Entry(self)
        self.entrada_valor_transf = tk.Entry(self)
        self.entrada_usuario = tk.Entry(self)

        #setando disposicao dos botoes na tela
        self.label_usuariologado.grid(row=0,column=0)

        self.botao_trocauser.grid(row=2,column=0)
        self.entrada_novousuario.grid(row=2,column=1)
        
        self.botao_verificasaldo.grid(row=4,column=0)

        self.botao_depositavalor.grid(row=6,column=0)
        self.label_valor_deposito.grid(row=5,column=1)
        self.entrada_valor_deposito.grid(row=6,column=1)

        self.botao_retirarvalor.grid(row=8,column=0)
        self.entrada_valor_saque.grid(row=8,column=1)

        self.botao_transferirvalor.grid(row=10,column=0)
        self.entrada_valor_transf.grid(row=10,column=1)
        self.label_usuario.grid(row=9,column=2)
        self.entrada_usuario.grid(row=10,column=2)

        self.label_transacaoexecutada.grid(row=12,column=1)

    def trocauser(self):
        entrada = self.entrada_novousuario.get()
        user = self.buscarusuario(entrada)
        print(entrada)
        comando = TrocarUsuario()
        troca = comando.trocarusuario(self.userlogado,user)
        if (troca == self.userlogado):
            frase = str("Erro: Troca não executada.")
        else:
            self.userlogado = user
            frase = str("Usuário substituído")
        self.logarusuario()
        #self.label_transacaoexecutada['text'] = frase
        self.att_historico(frase)
    
    def verificasaldo(self):
        comando = VerificaSaldo()
        frase = comando.verificarsaldo(self.userlogado)
        self.att_historico(frase)

    def depositavalor(self):
        comando = DepositaValor()
        entrada = float(self.entrada_valor_deposito.get())
        frase = comando.depositarvalor(self.userlogado,entrada)
        self.att_historico(frase)

    def retiravalor(self):
        comando = RetirarValor()
        entrada = float(self.entrada_valor_saque.get())
        frase = comando.retirarvalor(self.userlogado,entrada)
        self.att_historico(frase)

    def buscarusuario(self,entrada):
        for user in self.listausuario:
            if(entrada == user.nome):
                return user
        return 0

    def transferevalor(self):
        entrada = self.entrada_usuario.get()
        user = self.buscarusuario(entrada)
        if(user == 0):
            frase = str("Usuario Invalido. Não foi possível realizar transferencia.")
        else:
            entrada2 = float(self.entrada_valor_transf.get())
            comando = TransferirValor()
            frase = comando.transferirvalor(self.userlogado,user,entrada2)
        self.att_historico(frase)
        
    
    

root = tk.Tk()
app = Application(master=root)

app.mainloop()
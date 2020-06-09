'''
Utilize o Design Pattern State para modelar o exemplo de revisão de documento apresentado nos slides.
O documento pode estar no estado Draft, Moderation e Published. Implemente a máquina de estado da figura.
'''
'''
Documento compoe:
        State:
            <- Draft
            <- Moderation
            <- Publish

'''


from abc import abstractmethod

class User():
    def __init__(self,name):
        self.isAdmin = False
        self.name = name
    def setAdmin(self):
        self.isAdmin = True

class Document():
    def __init__(self,initial_state,user):
        self.changeState(initial_state)
        self.autor = user
    def changeState(self,state):
        self._state = state
        self._state.document = self
        print("Mudou para o estado " + state.__name__)

    def render(self,user):
        self._state.render(user)

    def publish(self,user):
        self._state.publish(user)

    def failreview(self,user):
        self._state.failreview(user)

    def expirar(self):
        self._state.expirar()


class State():
    @property
    def document(self) -> Document:
        return self._document
    @document.setter
    def document(self, document: Document) -> None:
        self._document = document
    @abstractmethod
    def render(self,user):
        pass
    @abstractmethod
    def publish (self,user):
        pass
    @abstractmethod
    def failreview(self,user):
        pass
    @abstractmethod
    def expirar(self):
        pass
    
class Draft(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__

    def render(self,user):
        if(user.isAdmin or user == self._document.autor):
            print("É possível mostrar esse documento.")
        else:
            print(user.name + ", você não possui credenciais para ver esse documento")
    
    def publish(self,user):
        if(user == self.document.autor):
            self.document.changeState(Moderation())
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print(user.name + ", você não possui credenciais para publicar esse documento")

class Moderation(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__

    def render(self,user):
        if(user == self._document.autor):
            print("Seu Documento está sobre moderação. Aguarde Resposta.")
        elif(user.isAdmin):
            print("Você pode ver esse documento")
        else:
            print("Você não possui credenciais para ver esse documento")
    
    def failreview(self,user):
        if(user.isAdmin):
            print("O documento de "+self.document.autor.name+" não foi aceito para publicação.")
            self.document.changeState(Draft())
        else:
            print("Você não possui credenciais para essa operação")
    
    def publish(self,user):
        if(user == self.document.autor):
            print("Seu Documento está sobre moderação. Aguarde Resposta.")
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print("Você não possui credenciais para publicar esse documento")

class Published(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__

    def render(self,user):
        if(user.isAdmin or user == self._document.autor):
            print("É possível mostrar esse documento.")
        else:
            print(user.name+" não possui credenciais para ver esse documento")
    
    def publish(self,user):
        if(user == self.document.autor):
            self.document.changeState(Moderation())
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print("Você não possui credenciais para publicar esse documento")
    
    def expirar(self):
        print("Documento Expirado")
        self.document.changeState(Draft())


#renato sera o autor
renato = User("Renato")
#nickolas nao possuira credenciais para ver o documento
nickolas = User("Nickolas")
samara = User("Samara")
#samara sera administradora
samara.setAdmin()

initial_state = Draft()

documento = Document(initial_state,renato)

documento.render(nickolas)
documento.render(renato)
documento.render(samara)

documento.publish(nickolas)
documento.publish(renato)

documento.failreview(samara)
documento.publish(samara)

documento.expirar()

''' 
Como parte de um simulador de estradas, será necessário o desenvolvimento de uma classe de veículos, 
com subclasses para diferentes tipos de veículos (Caminhões, automóveis, etc). Cada veículo poderá ter motorização 
elétrica, híbrida e motor de combustão. Utilize o Design Pattern Bridge para modelar estas classes. 
Implemente este modelo de classes em Python. 

'''

'''
class veiculo compoe:
    <<interface>> engine 
                    <- CombustionEngine
                    <- HybridEngine
                    <- EletricEngine
    <<interface>> type
                    <- Truck
                    <- Car
                    <- Motocycle

'''
from abc import abstractmethod


class Engine():
    @abstractmethod
    def getPoluicao(self) ->str:
        pass

class CombustionEngine(Engine):
    def __init__(self):
        self.poluicao = True
        self.name = __class__.__name__
    def getPoluicao(self) -> str:
        return (f"{self.name}"  f" é muito poluente.")

class HybridEngine(Engine):
    def __init__(self):
        self.poluicao = False
        self.name = __class__.__name__
    def getPoluicao(self) -> str:
        return (f"{self.name}"  f" é poluente.")

class EletricEngine(Engine):
    def __init__(self):
        self.poluicao = False
        self.name = __class__.__name__
    def getPoluicao(self) -> str:
        return (f"{self.name}"  f" é pouco poluente.")

class Type():
    @abstractmethod
    def getName(self) ->str:
        pass

class Truck(Type):
    def __init__(self):
        self.name = "Caminhão"
    def getName(self) -> str:
        return f"{self.name}"

class Car(Type):
    def __init__(self):
        self.name = "Carro"
    def getName(self) -> str:
        return f"{self.name}"

class Motocycle(Type):
    def __init__(self):
        self.name = "Moto"
    def getName(self) -> str:
        return f"{self.name}"

class Veiculo():
    def __init__(self,engine:Engine,type2:Type):
        self.motor = engine
        self.tipo = type2
    def getVeiculo(self):
        print (f"{self.tipo.getName()}",f"com motor",f"{self.motor.getPoluicao()}")

def client_code(abstraction):
    abstraction.getVeiculo()

if __name__ == "__main__":
    print("\n")

    implementation = CombustionEngine()
    implementation2 = Truck()
    abstraction = Veiculo(implementation,implementation2)    
    client_code(abstraction)

    implementation = EletricEngine()
    implementation2 = Car()
    abstraction = Veiculo(implementation,implementation2)    
    client_code(abstraction)

    implementation = HybridEngine()
    implementation2 = Motocycle()
    abstraction = Veiculo(implementation,implementation2)    
    client_code(abstraction)
    
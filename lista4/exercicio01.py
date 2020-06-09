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
from abc import ABC, abstractmethod


class Engine():
    @abstractmethod
    def getPoluicao(self) ->str:
        pass

class CombustionEngine(Engine):
    def __init__(self):
        self.poluicao = True
        self.name = __class__.__name__
    def getPoluicao(self) -> str:
        return (self + " É muito poluente.")

class HybridEngine(Engine):
    pass

class EletricEngine(Engine):
    pass


class Type():
    pass

class Truck(Type):
    pass

class Car(Type):
    pass

class Motocycle(Type):
    pass

class Veiculo():
    def __init__(self,engine:Engine,type2:Type) -> None:
        self.motor = engine
        self.tipo = type2
    def getVeiculo() -> str:
        return ("Veiculo "+"com motor"+self.motor.getPoluicao())


def client_code(abstraction: Veiculo) -> None:
    print(abstraction.getVeiculo(), end="")


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
     """
    print("#############TESTE##############")

    implementation = CombustionEngine()
    abstraction = Engine(implementation)

    implementation2 = Truck()
    abstraction2 = Type(implementation)

    client_code(abstraction,abstraction2)



    print("\n")

    '''implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)'''
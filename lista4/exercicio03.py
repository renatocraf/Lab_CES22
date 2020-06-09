''' 
Na questão 1, utilize o Design Pattern Fábrica para instanciar diferentes tipos de veículos.

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

<<interface>> Criador:
                    <- CriarTruck()
                            Cria um veiculo do tipo caminhao com motor hibrido
                    <- CriarCarro()
                            Cria um veiculo do tipo carro com motor eletrico
                    <- CriarMoto()
                            Cria um veiculo do tipo moto com motor a combustao



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

class Criador():
    @abstractmethod
    def criarVeiculo(self):
        pass

class CriarCarro(Criador):
    def criarVeiculo(self):
        implementation = EletricEngine()
        implementation2 = Car()
        abstraction = Veiculo(implementation,implementation2)
        return abstraction

class CriarTruck(Criador):
    def criarVeiculo(self):
        implementation = EletricEngine()
        implementation2 = Truck()
        abstraction = Veiculo(implementation,implementation2)
        return abstraction

class CriarMoto(Criador):
    def criarVeiculo(self):
        implementation = CombustionEngine()
        implementation2 = Motocycle()
        abstraction = Veiculo(implementation,implementation2)
        return abstraction

def client_code(criador):
    return criador.criarVeiculo()

if __name__ == "__main__":
    print("\n")

    moto = client_code(CriarMoto())
    moto.getVeiculo()

    carro = client_code(CriarCarro())
    carro.getVeiculo()

    caminhao = client_code(CriarTruck())
    caminhao.getVeiculo()


    
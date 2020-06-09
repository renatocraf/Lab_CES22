'''
Utilizando o exemplo do CoffeShop com padrão decorator. Crie um exemplo que construa Pizzas. 
Ao invés de itens para um café, usar ingredientes de pizza.
'''

class PizzaComponent:
    def getDescricao(self):
        return self.__class__.__name__
    def getCustoTotal(self):
        return self.__class__.valor

class Massa(PizzaComponent):
    valor = 10.0

class Decorador(PizzaComponent):
    def __init__(self,PizzaComponent):
        self.component = PizzaComponent
    def getCustoTotal(self):
        return self.component.getCustoTotal()+PizzaComponent.getCustoTotal(self)
    def getDescricao(self):
        return self.component.getDescricao() + ' ' + PizzaComponent.getDescricao(self)

class Mussarela(Decorador):
    valor = 2.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Calabresa(Decorador):
    valor = 3.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Tomate(Decorador):
    valor = 0.5
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Presunto(Decorador):
    valor = 3.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Azeitona(Decorador):
    valor = 0.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Ovo(Decorador):
    valor = 2.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)

class Manjericao(Decorador):
    valor = 2.0
    def __init__(self,PizzaComponent):
        Decorador.__init__(self,PizzaComponent)


marguerita = Mussarela(Tomate(Manjericao(Massa())))
print("Pizza Marguerita: " + marguerita.getDescricao()+ "\nValor: R$"+str(marguerita.getCustoTotal()))

calabresa = Mussarela(Azeitona(Calabresa(Massa())))
print("Pizza Calabresa: " + calabresa.getDescricao()+ "\nValor: R$"+str(calabresa.getCustoTotal()))

portuguesa = Mussarela(Presunto(Ovo(Massa())))
print("Pizza Calabresa: " + portuguesa.getDescricao()+ "\nValor: R$"+str(portuguesa.getCustoTotal()))

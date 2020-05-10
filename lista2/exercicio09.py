import math

class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {0}, ratio {1}'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5*(3**0.5*self.side**2)

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side*self.side

class Triangulo(Polygon):
    geometric_type: 'Triangulo'


class TrianguloEquilatero(RegularPolygon,Triangulo):
    geometric_type =  'Triangulo Equilatero'

    def area(self):
        return self.side*self.side*math.sqrt(3)/4

'''
O MRO significa Method Resolution Order, que é a ordem no qual o método é resolvido.
No nosso exemplo foi adicionado mais duas classes, Triangulo e TrianguloEquilatero.

A classe Triangulo está logo abaixo da Classe Polygon enquanto a classe TrianguloEquilatero tem como pais a Classe RegularPolygon e a Classe Triangulo

Caso eu crie um objeto de classe TrianguloEquilatero e solicite alguma informação, ele vai procurar primeiro na classe TrianguloEquilatero,
se nao encontrar, procura na Classe RegularPolygon e seus pais. Mais uma vez, se não encontra passa a procurar na Classe Triangulo


'''

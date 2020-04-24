#importando a biblioteca turtle
import turtle
#criando a função que vai desenhar o poligono
def draw_poli(t,n,sz):
    ang = 180-((n-2)*180/n)

    for i in range(n):        
        t.forward(sz)
        t.left(ang)  

#criando a tela que vai suportar a tartaruga
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 1")
#criando a tartaruga
tess = turtle.Turtle()
tess.color("pink","pink")

#desenhando o poligono
draw_poli(tess,8,50)

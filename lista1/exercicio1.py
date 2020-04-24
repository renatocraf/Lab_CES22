#importando a biblioteca turtle
import turtle
#criando a função que vai desenhar um retangulo por vez
def draw_rect(t,lado):
    for i in range(4):        
        t.forward(lado)
        t.left(90)
    t.penup()
    (x,y) = t.pos()
    t.goto(x-10,y-10)
    t.pendown()
#criando a tela que vai suportar a tartaruga
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 1")
#definindo quantidade de retangulos que serao desenhados na tela
quant = 5
#criando a tartaruga
t = turtle.Turtle()
t.color("pink","pink")
#fazendo o desenho
for i in range(quant):
    draw_rect(t,40+i*20)
wn.mainloop()

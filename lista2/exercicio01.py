import turtle

tela_width = 400
tela_heigth = 500

turtle.setup(tela_width,tela_heigth)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
tess.width(1)                        # Colocando tamanho 1 no pensize  

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():                           # Mudando a cor para vermelho
    tess.color("red")

def h6():                           # Mudando a cor para verde
    tess.color("green")

def h7():                           # Mudando a cor para azul
    tess.color("blue")

def h8():                           # Caso o tamanho do lapis seja menor que 20, incrementa em 1
    if tess.pensize()<20:
        tess.width(tess.pensize()+1)

def h9():                           # Caso o tamanho do lapis seja maior que 2, decrementa em 1
    if tess.pensize()>2:
        tess.width(tess.pensize()-1)
    
def h10():                          # Caso a largura da tela seja menor do que 700, incrementa a altura e largura em 100      
    tamanho =  [turtle.window_width(),turtle.window_height()]
    print(tamanho[0])                         
    if tamanho[0] < 700:            
        turtle.setup(tamanho[0]+100,tamanho[1]+100)

def h11():                           # Caso a largura da tela seja maior do que 300, decrementa a altura e largura em 100
    tamanho =  [turtle.window_width(),turtle.window_height()]
    print(tamanho[0])                         
    if tamanho[0] > 300:            
        turtle.setup(tamanho[0]-100,tamanho[1]-100)



# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5,"r")
wn.onkey(h6,"g")
wn.onkey(h7,"b")
wn.onkey(h8,"+")
wn.onkey(h9,"-")
wn.onkey(h10,"o")
wn.onkey(h11,"p")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

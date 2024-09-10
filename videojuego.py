from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
#Dibuja un cuadrado en el que la longitud de los lados es igual a la diferencia en la coordenada x 
#entre el punto de inicio (start) y el punto final (end). El cuadrado se dibuja comenzando en el punto de inicio.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
     forward(end.x - start.x)
     left(90)

    end_fill()

def circle(start, end):
    import math
    "Draw circle from start to end."
#Dibuja un círculo aproximado basado en la distancia entre el punto de inicio (start) y el punto final (end).
#El radio del círculo se calcula utilizando la distancia euclidiana entre estos puntos.
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range(360):
     fd(math.sin(math.radians(1))*(math.sqrt((end.x - start.x)**2+(end.y - start.y)**2)))
     lt(1)

    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
#Dibuja un rectángulo con ancho y altura calculados a partir de la diferencia 
#entre los puntos de inicio y final. La altura tiene un ajuste adicional de 30 unidades.
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if count%2== 0:
            forward(end.x - start.x)
            left(90)
        else:
            forward(end.x+30 - start.x+30)
            left(90)
    end_fill()

def triangle(start, end):
#Dibuja un triángulo equilátero con lados de longitud igual a la diferencia en la coordenada x
#entre el punto de inicio (start) y el punto final (end).    
 "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
#Maneja el evento de clic en la pantalla. Dibuja la forma seleccionada desde el punto de inicio
#hasta el punto final y luego borra el punto de inicio.
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()





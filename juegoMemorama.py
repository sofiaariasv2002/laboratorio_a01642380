from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2 # lista de números del 0 al 31, 2 veces
state = {'mark': None}
# indica si un tile está oculto (True) o revelado (False)
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y) # Obtiene el índice del tile que fue clicado
    mark = state['mark'] # Obtiene el índice del tile actualmente marcado

	# Si no hay un tile marcado o el tile marcado es el mismo que el clicado,
    	# o los tiles no coinciden, marca el nuevo tile.
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False #revela el tile clicado
        hide[mark] = False #revela el tile previamente marcado
        state['mark'] = None #reinicia el marcador

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car) #cambia la forma del cursor a la iamgen del carro
    stamp() #estampa la forma del cursor en la pamtalla

	# Dibuja los tiles
    for count in range(64):
        if hide[count]:
            x, y = xy(count) #obtiene las coordenadas (x,y) del tile
            square(x, y) #dibuja el cuadrado para el tile

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark) # Obtiene las coordenadas del tile marcado
        up()
        goto(x +27, y-3)
        color('black')
<<<<<<< HEAD
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))
=======
        write(tiles[mark], font=('Arial', 30, 'normal')) #escribe valor tile
>>>>>>> 6378566 (comentar codigo para documentacion)

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

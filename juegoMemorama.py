from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2  # Lista de números del 0 al 31, 2 veces
state = {'mark': None}
hide = [True] * 64
taps = 0

# Lista de colores
tile_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta'] * 4

# Asignar un color a cada número del 0 al 31
color_map = {}
for number in set(tiles):
    color_map[number] = tile_colors[number % len(tile_colors)]

def square(x, y, tile_color):
    "Draw a square with the given color at (x, y)."
    up()
    goto(x, y)
    down()
    fillcolor(tile_color)  # Use fillcolor to specify the fill color of the square
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tile index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tile count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def get_tile_color(tile_value):
    "Return the color associated with the tile value."
    return color_map[tile_value]

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps
    taps += 1  # Increment counter   
    spot = index(x, y)  # Get the index of the clicked tile
    mark = state['mark']  # Get the index of the currently marked tile   

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
       state['mark'] = spot
    else:
        hide[spot] = False  # Reveal the clicked tile
        hide[mark] = False  # Reveal the previously marked tile
        state['mark'] = None  # Reset the mark 

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)  # Change the cursor shape to the car image
    stamp()  # Stamp the cursor shape on the screen

    # Draw the tiles
    for count in range(64):
        if hide[count]:
            x, y = xy(count)  # Get (x, y) coordinates of the tile
            square(x, y, 'white')  # Draw the square for the tile
    
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)  # Get the coordinates of the marked tile
        tile_color = get_tile_color(tiles[mark])
        square(x, y, tile_color)  # Draw the tile with the associated color
        up()
        goto(x + 27, y - 3)
        color('black')  # Color of the text
        write(tiles[mark], align="center", font=('Arial', 20, 'normal'))
    
    # Detect whe all tiles are revealed
    if all(not hidden for hidden in hide):
       color('white')
       write("Game Over :)", align = "center", font= ('Arial', 40, 'bold'))

    up()
    goto(-190, 210)
    write(f'Número de taps: {taps}', font = ('Arial', 16, 'bold'))
   
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



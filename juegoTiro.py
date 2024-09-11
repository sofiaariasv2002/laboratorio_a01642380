from random import randrange
from turtle import *
from freegames import vector

# Inicialización de variables
ball = vector(-200, -200) # posicion inicial de la pelota
speed = vector(0, 0) # Velocidad inicial de la pelota
targets = [] # Lista para almacenar los objetivos

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball): # Verifica si la pelota está dentro del área visible
        ball.x = -199  # Posición inicial de la pelota fuera del área visible
        ball.y = -199
<<<<<<< HEAD
        speed.x = (x + 200) / 25 # Calcula la velocidad en función de la posición del toque
        speed.y = (y + 200) / 25
=======
        speed.x = (x + 200) / 10 # Calcula la velocidad en función de la posición del toque
        speed.y = (y + 200) / 10
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

	# Dibuja el marco alrededor de la pantalla
    penup()
    goto(-210, 210)
    pendown()
    color('black')
    width(3)
    for _ in range(4):
        forward(420)
        right(90)
    penup()

	# Dibuja los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

	# Dibuja la pelota si está dentro del área visible
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
	 # Añade un nuevo objetivo aleatorio
<<<<<<< HEAD
    if randrange(40) == 0:
=======
    if randrange(30) == 0:
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

	# Mueve los objetivos hacia la izquierda
    for target in targets:
<<<<<<< HEAD
        target.x -= 0.5
=======
        target.x -= 2

>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
		# Si un objetivo sale de la pantalla, reposiciónalo en el lado derecho
        if target.x < -200:
            target.x = 200
            target.y = randrange(-150, 150)

	 # Mueve la pelota si está dentro del área visible
    if inside(ball):
        speed.y -= 0.35 # respeta la gravedad
        ball.move(speed) 

    dupe = targets.copy() 
    targets.clear() 

	# añade los objetivos a la lista targets si la distancia entre el objetivo y ball es mayor a 13.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw() 

	# Verifica si cada objetivo está dentro de la pantalla. Si algún objetivo no está dentro, la función retorna y detiene la ejecución
    for target in targets:
        if not inside(target):
            # Reposiciona el objetivo en el lado derecho si sale de la pantalla
            target.x = 200
            target.y = randrange(-150, 150)

    ontimer(move, 50) # 

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

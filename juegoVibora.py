from turtle import *
from random import randrange, choice
from freegames import square, vector

# Inicialización de variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
move_count = 0
speed = 80
move_count = 0

# list of available colors
colors = ["blue", "green", "yellow", "purple", "orange"]

# define snake colors and food
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    global move_count
    global speed
    head = snake[-1].copy()
    head.move(aim)

    # Termina el juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Si la serpiente alcanza la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10         
        speed = max(30, speed - 5)
    else:
        snake.pop(0)

    clear()

    move_count += 1
    if move_count % 5 == 0: 
       direction = [vector(10,0),vector(-10,0),vector(0,10),vector(-10,0)]
       move_direction = choice(direction)

       new_pos = food + move_direction

       if inside(new_pos):
          food.move(move_direction)

    
    # Dibuja la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)
 
    # Dibuja la comida
    square(food.x, food.y, 9, food_color)
    update()

    ontimer(move, speed)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
<<<<<<< HEAD
<<<<<<< HEAD
=======
move_count = 0
speed = 80
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
=======
move_count = 0
>>>>>>> 258d83b (Increase food speed)

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
<<<<<<< HEAD
<<<<<<< HEAD
=======
    global move_count
    global speed
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
=======
    global move_count
>>>>>>> 258d83b (Increase food speed)
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
<<<<<<< HEAD
        food.y = randrange(-15, 15) * 10
=======
        food.y = randrange(-15, 15) * 10         
        speed = max(30, speed - 5)
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
    else:
        snake.pop(0)

    clear()

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 258d83b (Increase food speed)
    move_count += 1
    if move_count % 5 == 0: 
       direction = [vector(10,0),vector(-10,0),vector(0,10),vector(-10,0)]
       move_direction = choice(direction)

       new_pos = food + move_direction

       if inside(new_pos):
          food.move(move_direction)

<<<<<<< HEAD
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415
=======
>>>>>>> 258d83b (Increase food speed)
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
<<<<<<< HEAD
    ontimer(move, 100)
=======
    ontimer(move, speed)
>>>>>>> 2dcdef64ee1899808ccfa751532c3a599b52f415

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

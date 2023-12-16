from random import *
from turtle import *

from freegames import vector

# Register the image for the bird
register_shape("C:/Users/hewaw/OneDrive/Desktop/bird.gif")
bird = Turtle(shape="bird.gif")
bird.penup()
bird.speed(0)
balls=[]

def tap(x,y): #move bird upwards
    up = vector(0,30)
    bird.sety(bird.ycor() + up.y)

def inside(point): #return true if point on screen
    return -200<point.x<200 and -200<point.y<200

def draw(alive): #draw screen objects
    bird.setheading(90 if alive else 270)
    bird.stamp()

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

    

def move():
    #update object position

    bird.sety(bird.ycor() - 5)

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)
        
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird.position()):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird.position()) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

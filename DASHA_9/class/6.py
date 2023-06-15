from turtle import *

m = 15

tracer(5)
lt(90)
down()

for i in range(4):
    forward(10 * m)
    rt(270)

up()
fd(3 * m)
rt(270)
fd(5 * m)
rt(90)

down()

for i in range(2):
    forward(10 * m)
    rt(270)
    forward(12 * m)
    rt(270)

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3, 'red')
mainloop()
import turtle

v = 100
pen = turtle.Turtle()
for i in range(v):
    pen.forward(i*5)
    #in Clockwise
    pen.right(144)
turtle.done()
'''

'''import turtle
t = turtle.Turtle()
for i in range(64):
    t.forward(i*5)
    t.right(90)
turtle.done()'''

'''import turtle as t

t.bgcolor('black')
t.pensize(3)
t.speed(300)
for i in range(350):
    t.fd(i*4)
    t.right(91)
    t.color('aqua')
t.mainloop()'''

'''import turtle

v = 58

pen = turtle.Turtle()
for i in range(v):
    pen.forward(i*10)
    #in clockwise
    pen.right(144)
turtle.done()'''

'''import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('#7C909C')
t.speed(25)
col = ('#ED7864', '#6E544F',
       '#592F2F', '#6E382E')
for n in range(10):
    for x in range(8):
        t.speed(x + 10)
        for i in range(2):
            t.pensize(2)
            t.circle(80 + n * 20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n % 4])
s.exitonclick()'''

'''import turtle as t

t.bgcolor("black")
t.pensize(1)
t.speed(1000000*10000)
for i in range(35000):
    t.fd(i*2)
    t.right(91)
    t.color('aqua')
t.mainloop()'''

'''import turtle as t

t.bgcolor("green")
t.pensize(5)
t.speed(500)
for i in range(1000):
    t.bk(i/7)
    t.left(91)
    t.color("red")
t.mainloop()

'''


'''import turtle as t

t.bgcolor('black')
t.pensize(2)
t.speed(500)
for i in range(350):
    t.fd(i*4)
    t.right(91)
    t.color('aqua')
t.mainloop()
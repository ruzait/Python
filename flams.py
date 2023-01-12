name_1 = input("Enter Your Name: ")
name_2 = input("Enter Your crash Name: ")
a = list(name_1.lower().replace(" ", ''))
b = list(name_2.lower().replace(" ", ''))
c = []


for i in a:
    for j in b:
        if i == j:
            c += i
        else:
            continue

for i in range(len(c)):
    try:
        a.remove(c[i])
        b.remove(c[i])
    except ValueError:
        pass


d = len(a) + len(b)

flames = ['F', 'L', 'A', 'M', 'E', 'S']

while len(flames) > 1:
    formula = d % len(flames) - 1
    if formula >= 0:
        left = flames[formula + 1:]
        right = flames[:formula]
        flames = left + right
    else:
        flames = flames[:len(flames)-1]

def f():
    print("you are friends")

def l():
    print("you are lovers")

def a():
    print("you have affection on eachother")

def m():
    print("you will get married")

def e():
    print("you are enemies")

def s():
    print("you are siblings")

if flames == ['F']:
    f()
if flames == ['L']:
    l()
if flames == ['A']:
    a()
if flames == ['M']:
    m()
if flames == ['E']:
    e()
if flames == ['S']:
    s()
'''

# caransy change
'''from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("350x300+250+200")
root.title("GUI")

menubar = Menu(root)
root.config(menu=menubar)
fil_menu = Menu(menubar, tearoff=False)

fil_menu.add_command(label="Exit",
                     command=root.destroy)
menubar.add_cascade(label="Setting",
                    menu=fil_menu)


def pri():
    global m
    ch = a.get()

    try:
        m = float(Rs_E.get())
    except ValueError:
        messagebox.showerror \
            (title='ValueError',
                message='Plz. Enter numbers only:)')

    if ch == 1:
        global a1
        t = m * 50
        a1 = Label(root, text=str(t)+"   ",
                   font=18)
        a1.place(x=140, y=150)
    elif ch == 2:
        global a2
        s = m * 45
        a2 = Label(root, text=str(s)+"   ",
                   font=18)
        a2.place(x=140, y=150)
    elif ch == 3:
        global a3
        d = m * 200.2
        a3 = Label(root, text=str(d)+"   ",
                   font=18)
        a3.place(x=140, y=150)

def qui():
    global a1, a2, a3
    a1.destroy()
    a2.destroy()
    a3.destroy()

Rs_E = Entry(root, bd=2)
Rs_E.place(x=120, y=10)

# ans = Label(root, text=" ")
# ans.place(x=130, y=30)

E_na = Label(root, text="LKR", font=15)\
    .place(x=80, y=10)

a = IntVar()
b1 = Radiobutton(root, text="SR", variable=a,
                 value=1, command=pri, font=10)\
    .place(x=50, y=70)
b2 = Radiobutton(root, text="QR", variable=a,
                 value=2, command=pri, font=10)\
    .place(x=120, y=70)
b3 = Radiobutton(root, text="USD", variable=a,
                 value=3, command=pri, font=10)\
    .place(x=190, y=70)

Button(root, text="CALCULATE", bd=-1, font=10
       , fg="red", command=pri).place(x=120, y=120)
Button(root, text="Clear", command=qui,
       bg="red", font=20).place(x=280, y=200)

root.mainloop()'''

# turtle game
'''import turtle
wn = turtle.Screen()
wn.title("1st turtle game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=20, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=20, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(10, 0)
Ball.dx = 2
Ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0            Player B: 0",
          align="center", font=("courier",
                                24, "normal"))


# func
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    wn.update()

    # move tha ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}            Player B: {}"
                  .format(score_a, score_b),
                  align="center", font=("courier",
                                        24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}            Player B: {}"
                  .format(score_a, score_b),
                  align="center", font=("courier",
                                        24, "normal"))


    # paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_b.ycor() + 40 and Ball.ycor() > paddle_b.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1'''
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry("300x200+500+250")


def log():
    s_bu.destroy()
    l_bu.destroy()

    name_lab = Label(root, text="UserName: ", font=12)
    name_lab.place(x=31, y=10)

    PASSWORD_lab = Label(root, text="Password: ", font=12)
    PASSWORD_lab.place(x=32, y=40)

    C_PASSWORD_lab = Label(root, text="Conf. password: ", font=12)
    C_PASSWORD_lab.place(x=16, y=70)

    name_E = Entry(root, bd=3)
    name_E.place(x=140, y=10)

    PASSWORD_E = Entry(root, bd=3)
    PASSWORD_E.place(x=140, y=40)
    PASSWORD_E.config(show="*")

    C_PASSWORD_E = Entry(root,bd=3)
    C_PASSWORD_E.place(x=140, y=70)

    def prin():
        x = name_E.get()
        y = C_PASSWORD_E.get()
        z = PASSWORD_E.get()

        if (x == "" and y == "" and z == ""):
            print("status --Blank--\n")
            messagebox.showinfo(title="login status", message="some thing is Blank!")


        elif (y == z):
            print("status --Success--")
            messagebox.showinfo(title="login status", message="Login Success")
            print("name:--" + name_E.get() + "--")
            print("PASSWORD:--" + PASSWORD_E.get() + "--")
            # p_name = Label(root, text="Hello, " + name_E.get().upper(), font=1)
            # p_name.place(x=20, y=125)
            # En_mar = Label(root, text=" --Enter your marks--", font=1)
            # En_mar.place(x=20, y=150)

        else:
            print("status --some thing is wrong!--\n")
            messagebox.showinfo(title="login status", message="some thing is wrong!")





    but = Button(root, text="login", width=28, command=prin, bg="green", font=10)
    but.place(x=18, y=100)
    ex = Button(root, text="Exit", command=exit, bg="red", font=10, bd=-3, width=5)
    ex.place(x=220, y=150)

def si():
    s_bu.destroy()
    l_bu.destroy()

    name_lab = Label(root, text="UserName: ", font=12)
    name_lab.place(x=18, y=10)

    PASSWORD_lab = Label(root, text="Password: ", font=12)
    PASSWORD_lab.place(x=18, y=40)

    name_E = Entry(root, bd=3)
    name_E.place(x=140, y=10)

    PASSWORD_E = Entry(root, bd=3)
    PASSWORD_E.place(x=140, y=40)
    PASSWORD_E.config(show="*")

    def prin():
        a = name_E.get()
        b = PASSWORD_E.get()

        if (a == "" and b == ""):
            print("status --Blank--\n")
            messagebox.showinfo(title="sigin status", message="Blank Not allowed")

        elif (a == "Ruzait" and b == "11983"):
            print("status --Success--")
            messagebox.showinfo(title="login status", message="sigin Success")
            # p_name = Label(root, text="Hello, " + name_E.get().upper(), font=1)
            # p_name.place(x=20, y=125)
            # En_mar = Label(root, text=" --Enter your marks--", font=1)
            # En_mar.place(x=20, y=150)

        else:
            print("status --Incorrect Username and password--\n")
            messagebox.showinfo(title="sigin status", message="Incorrect Username and password")

        print(name_E.get())
        print(PASSWORD_E.get())



    but = Button(root, text="sigin", width=28, command=prin, bg="green", font=10)
    but.place(x=18, y=100)
    ex = Button(root, text="Exit", command=exit, bg="red", font=10, bd=-3, width=5)
    ex.place(x=220, y=150)


s_bu = Button(root, text="sigin", command=si, bd=5, bg="yellow", font=("Ink Free", 20), width=15)
s_bu.place(x=27, y=100)

l_bu = Button(root, text="login", command=log, bd=5, bg="pink", font=("Ink Free", 20), width=15)
l_bu.place(x=27, y=30)

root.mainloop()
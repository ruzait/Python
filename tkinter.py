from tkinter import *

root = Tk()
root.title("RuzaiT")
root.geometry('200x200')

input = Entry(root)
input.pack()

def onclick():
    lab=Label(root,text=input.get())
    lab.pack(padx=10,pady=10)

but=Button(root,text="c t button",command=onclick).place(x=50, y=100)

root.mainloop()'''

'''from tkinter import *


def submit():
    input = text.get("1.0",END)
    print(input)

root=Tk()
text=Text(root,bg="light yellow",
          font=("Ink Free",25),
          height=8,
          width=20,
          padx=20,
          pady=20,
          fg="purple")
text.pack()

but=Button(root,text="submit",command=submit)
but.pack()

root.mainloop()
'''

'''from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename()
    print(filepath)

root = Tk()
but = Button(text="Open",command=openfile)
but.pack()
root.mainloop()
'''

'''from tkinter import *
root = Tk()

frame=Frame(root)
frame.pack()

buttonframe = Frame(root)
buttonframe.pack(side = BOTTOM)
red_button = Button (frame,text="RED",fg="red")
red_button.pack(side = LEFT)

green_button = Button (frame,text="GREEN",fg="green")
green_button.pack(side = LEFT)

blue_button = Button (frame,text="BLUE",fg="blue")
blue_button.pack(side = LEFT)

black_button = Button(frame,text="BLACK",fg="black")
black_button.pack(side = BOTTOM)

root.mainloop()'''

'''from tkinter import *

def openfile():
    print("File has been opened! ")

def savefile():
    print("File has been saved! ")

def cut():
    print("You cut some text! ")

def copy():
    print("You copied some text! ")

def paste():
    print("You pasted some text! ")

window = Tk()

        #openImage = PhotoImage(file="file.png")
        #saveImage = PhotoImage(file="file.png")
        #exitImage = PhotoImage(file="file.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openfile )   #,image=openImage,compound='left'
fileMenu.add_command(label="Save",command=savefile)    #,image=saveImage,compound='left'
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)    #,image=exitImage,compound='left'

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()'''

'''from tkinter import *

root = Tk()


frame = Frame(root,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=200, y=200)

but = Button(frame, text="W", font=("consolas",25),width=3).pack(side=TOP)
but = Button(frame, text="A", font=("consolas",25),width=3).pack(side=LEFT)
but = Button(frame, text="S", font=("consolas",25),width=3).pack(side=LEFT)
but = Button(frame, text="D", font=("consolas",25),width=3).pack(side=LEFT)


root.mainloop()'''

'''from tkinter import *

def N_win():
    N_win = Tk()
    Ol_window.destroy()

Ol_window = Tk()
Button(Ol_window, text="New window", command=N_win).pack()
Ol_window.mainloop()'''

'''from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is Tab #1", width=50,height=25).pack()
Label(tab2, text="GooooooD ByE, tHiS Is TaB #2", width=50,height=25).pack()

root.mainloop()'''

"""from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info messagebox',message='You are wrong!')
    #messagebox.showwarning(title='WARNING', message='You have A VIRUS!!!!!!')
    #messagebox.showerror(title='ERROR', message='something went wrong:(')

    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        #print('you did a thing!')
    #else:
        #print('you canceled a thing! :(')

    #if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to do the thing?'):
     #   print('you cetried a thing!')
    #else:
     #   print('you canceled a thing! :(')

    if messagebox.askyesno(title='ask yes or no',message='Do U like cake?'):
        print("his like cake too:)" )
    else:
        print("Why do U not like cake?:(")

root = Tk()

but = Button(root, command=click, text= "click me")
but.pack()

root.mainloop()
"""

# Listbox
'''from tkinter import*

top =Tk()

LB = Listbox(top)

LB.insert(1,'PYTHON')
LB.insert(2,'JAVA')
LB.insert(3,'C++')
LB.insert(4,'Any other')
LB.pack()

top.mainloop()'''

'''from tkinter import *
root = Tk()
root.title("Menu Demo")

menubar = Menu(root)
root.config(menu=menubar)

fil_menu = Menu(menubar)

fil_menu.add_command(
    label="Exit",
    command = root.destroy)

menubar.add_cascade(
    label = "File",
    menu = fil_menu)
root.mainloop()
'''

'''from tkinter import *
root = Tk()
root.title("Menu Demo")

menubar = Menu(root)
root.config(menu=menubar)

fil_menu = Menu(menubar, tearoff = False)

fil_menu.add_command(
    label="Exit",
    command = root.destroy)

menubar.add_cascade(
    label = "File",
    menu = fil_menu)
root.mainloop()'''

'''from tkinter import Tk, Frame, Menu

root = Tk()
root.geometry("320x150")
root.title("fgfgf")

menubar = Menu(root)
root.config(menu = menubar)

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label="ru")
sub_menu.add_command(label="ri")

file_menu.add_cascade(label="Pre", menu = sub_menu)

file_menu.add_command(label='Exit', command=root.destroy)

menubar.add_cascade(label="File", menu = file_menu)

root.mainloop()'''

'''from tkinter import *
from tkinter import messagebox

root = Tk()

def prn():
    messagebox.askyesno(title=T,message=m)


button = Button(root,
            text="Test",
            command=prn).pack()

root.mainloop()'''

'''from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while (download<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+'/'+str(GB)+" GB completed")
        root.update_idletasks()

root = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(root, orient=VERTICAL, length=300)
bar.pack(pady=10)

percentLabel = Label(root, textvariable=percent).pack()
taskLabel = Label(root, textvariable=text).pack()

button = Button(root, text="download", command=start).pack()

root.mainloop()'''

'''from tkinter import *

root = Tk()

canvas = Canvas(root,height=500,width=500)
canvas.create_rectangle(100,300,300,100) #,fill="silver",outline="black")
canvas.pack()

l = Label(root,text="I is the rectangle")
l.place(x=150,y=180)

root.mainloop()'''

'''from tkinter import *

root = Tk()

canvas = Canvas(root,height=500,width=500)
canvas.create_arc(0,0,500,500,style=PIESLICE,start=90,extent=180)
canvas.pack()

root.mainloop()'''

'''from tkinter import *

def doSomething(event):
    #print("you pressed:" + event.keysym)
    label.config(text=event.keysym)
    print("you enterd :" + event.keysym)

root = Tk()

root.bind("<Key>",doSomething)
label = Label(root,font=("Helvetica",100))
label.pack()

root.mainloop()'''

'''from tkinter import *

def doSomething(event):
    print("Mouse coordinates" + str(event.x)+","+str(event.y))

root = Tk()

root.bind("<Button-1>",doSomething) #left mouse
#root.bind("<Button-2>",doSomething) #scroll mouse
#root.bind("<Button-3>",doSomething) #right mouse
#root.bind("<ButtonRelease>",doSomething) #X,Y place in mouse
#root.bind("<Enter>",doSomething)  #enter window
#root.bind("<Leave>",doSomething) #leave window
#root.bind("<Motion>",doSomething) # where the mouse moved

root.mainloop()'''

'''from tkinter import *

root = Tk()

frame = LabelFrame(root, text="This is my frame...", padx=105, pady=105)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Click Hear")
b.grid(row=0, column=0)
root.mainloop()'''

'''from tkinter import *
root = Tk()
root.geometry("500x300+-500+100")
root.title("iugfsgsf  yfhfydf")

#remove title bar
root.overrideredirect(True)

# Create Fake Title Bar
title_Bar = Frame(root, bg="red", relief="raised",  bd=1)
title_Bar.pack(expand=0, fill=X)

title_lab = Label(title_Bar, text="MY CREATE APP", bg="red", fg="white")
title_lab.pack(side=LEFT, pady=4)

my_Bu = Button(root, text="close!", command=quit)
my_Bu.pack(pady=50)


root.mainloop()'''

'''from tkinter import *

root = Tk()
root.title("BACKGRUOND_IMG")
root.geometry("900x506+200+100")
root.resizable(width=False, height=False)

bg = PhotoImage(file="IMG.png")


# _________________Whith out Canvas_____________________________________________________________________________________
my_lab = Label(root, image = bg)
my_lab.place(x=0, y=0, relwidth=1, relheight=1)

my_te = Label(root, text="WelCome!", font=("Helvetica", 50), fg="black")
my_te.pack(pady=50)

my_fra = Frame(root)
my_fra.pack(pady=20)

my_but1 = Button(my_fra, text="Exit", command=quit)
my_but1.grid(row=0, column=0, padx=20)

my_but2 = Button(my_fra, text="Start", command=root)
my_but2.grid(row=0, column=1, padx=20)

my_but3 = Button(my_fra, text="Reset")
my_but3.grid(row=0, column=2, padx=20)
# ______________________________________________________________________________________________________________________

my_can = Canvas(root, width=900, height=506)
my_can.pack(fill="both", expand=True)

my_can.create_image(0, 0, image=bg, anchor="nw")

my_can.create_text(450, 50, text="Welcome!", font=("Helvetica", 50), fill="blue")

but1 = Button(root, text="Start", bg="green", bd=-1)
but2 = Button(root, text="Reset", bg="yellow", bd=-1)
but3 = Button(root, text="Exit", bg="red", command=quit, bd=-1)

but1_win = my_can.create_window(770, 470, anchor="nw", window=but1)
but2_win = my_can.create_window(813, 470, anchor="nw", window=but2)
but3_win = my_can.create_window(860, 470, anchor="nw", window=but3)

root.mainloop()'''

# scrollbar
'''from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number:  ' + str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()
'''

# Spinbox
'''from tkinter import*
root = Tk()

w = Spinbox(root, from_=0, to=10)
w.pack()

mainloop()'''

# Radiobutton
'''from tkinter import*

m = Tk()

v = IntVar()
Radiobutton(m,text="A/l",variable=v,value=1).pack(anchor=W)

Radiobutton(m,text="O/l",variable=v,value=2).pack(anchor=W)

mainloop()'''

# Scale
'''from tkinter import*
m =Tk()

w = Scale(m, from_=0, to=200,orient=VERTICAL)
w.pack()

w = Scale(m, from_=0, to=200, orient=HORIZONTAL)
w.pack()

mainloop()'''

#customtkinter
'''import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CustomTkinter",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor" ,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="CTkSwitch")
        self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="CTkSwitch")
        self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="CTkButton",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        self.button_3.configure(state="disabled", text="Disabled CTkButton")
        self.combobox_1.set("CTkCombobox")
        self.radio_button_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        self.switch_2.select()
        self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()'''

'''
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green, sweetkind

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="Press...", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
'''

'''


import tkinter
import customtkinter  # <- import the CustomTkinter module

root = tkinter.Tk()  # create the Tk window like you normally do
root.geometry("400x240")
root.title("CustomTkinter Test")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
'''

'''import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import customtkinter


def add():
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        c = a + b
        result.configure(text=str(c))
    except:
        tkinter.messagebox.showwarning(title="warning message", message="Enter a number")


def subtract():
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        c = a - b
        result.configure(text=str(c))
    except:
        tkinter.messagebox.showwarning(title="warning message", message="Enter a number")


def multipy():
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        c = a * b
        result.configure(text=str(c))
    except:
        tkinter.messagebox.showwarning(title="warning message", message="Enter a number")


def divide():
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        c = a / b
        result.configure(text=str(c))
    except:
        tkinter.messagebox.showwarning(title="warning message", message="Enter a number")


customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")
window = customtkinter.CTk()
window.geometry("550x500")
window.title("Calculator")
window.resizable(False, False)


f1 = customtkinter.CTkFrame(window, bg="#f1faee")
f1.pack(expand=True, fill=BOTH)

# -------Input Label--------#
la1 = customtkinter.CTkLabel(f1, bg="#f1faee", text_color="white", text="First Number:", text_font=("", 25))
la1.place(x=20, y=20)

la2 = customtkinter.CTkLabel(f1, bg="#f1faee", text_color="white", text="Second Number:", text_font=("", 25))
la2.place(x=20, y=98)
# --------Input Box---------#
ent1 = customtkinter.CTkEntry(f1, bg="#f1faee", text_color="silver", placeholder_text="Enter a number", width=220)
ent1.place(x=300, y=26)

ent2 = customtkinter.CTkEntry(f1, bg="#f1faee", text_color="silver", placeholder_text="Enter a number", width=220,
                              text_font=("", 12))
ent2.place(x=300, y=110)


# ---------------------------- Buttons ---------------------------#
btn1 = customtkinter.CTkButton(f1, bg="#f1faee", text_color="white", text="Add",
                               text_font=("", 27), command=add, corner_radius=4, fg_color="#2a9d8f")
btn1.place(x=340, y=220)

btn2 = customtkinter.CTkButton(f1, bg="#f1faee", text_color="white", text="Subtract",
                               text_font=("", 27), command=subtract, corner_radius=4, fg_color="#2a9d8f")
btn2.place(x=340, y=320)

btn3 = customtkinter.CTkButton(f1, bg="#f1faee", text_color="white", text="Multipy",
                               text_font=("", 27), command=multipy, corner_radius=4, fg_color="#2a9d8f")
btn3.place(x=70, y=220)

btn4 = customtkinter.CTkButton(f1, bg="#f1faee", text_color="white", text="Divide",
                               text_font=("", 27), command=divide, corner_radius=4, fg_color="#2a9d8f")
btn4.place(x=70, y=320)


# ------------------------------- Result Label -------------------------#
Result = customtkinter.CTkLabel(f1, bg="#f1faee", text_color="orange", text="Result:", text_font=("", 29))
Result.place(x=100, y=400)

# ------------------------------- Result Label OUTPUT -------------------------#
result = customtkinter.CTkLabel(f1, bg="#f1faee", text_color="orange", text="", text_font=("", 29))
result.place(x=300, y=400)


window.mainloop()
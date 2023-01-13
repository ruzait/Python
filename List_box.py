from tkinter import *
import tkinter.messagebox
import pickle

root = Tk()
root.title("My_List")
#root.geometry('330x400')


def add():
    task = entry.get()

    if task !='':
        listbox.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)

    else:
        tkinter.messagebox.showwarning(title="Warning", message='You must enter a task:)')

def dele():
    try:
        task_in = listbox.curselection()[0]
        listbox.delete(task_in)
    except:
        tkinter.messagebox.showwarning(title='WARNING', message='You must selsct a task:)')

def load():
    try:
        task = pickle.load(open("task.dat", "rb"))  # rb=read in binary
        listbox.delete(0, tkinter.END)
        for task in task:
            listbox.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title='WARNING', message='Cannot find task.dat.:)')



def save():
    task = listbox.get(0, listbox.size())
    #print(task)
    pickle.dump(task, open("task.dat", "wb"))     #wb=write in binary


frame = tkinter.Frame(root)
frame.pack()


#Create list_Box
listbox = tkinter.Listbox(frame, height=10, width=50)
listbox.pack(side=tkinter.LEFT)

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)



entry = tkinter.Entry(root, width=47)
entry.pack()

add_B = tkinter.Button(root, text="ADD NEW", width=48, command=add)
add_B.pack()

dele_B = tkinter.Button(root, text="DELETE", width=48, command=dele)
dele_B.pack()

load_b = tkinter.Button(root, text="LOAD", width=48, command=load)
load_b.pack()

save = tkinter.Button(root, text="SAVE", width=48, command=save)
save.pack()


root.mainloop()
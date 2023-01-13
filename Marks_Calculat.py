from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='TAMIL MARKS')                #TAMIL NAME BORT
        self.lbl2=Label(win, text='MATHS MARKS')                #MATHS NAME BORT
        # T-BOXS (T1,T2...) , #bd- Thadippam
        self.t1=Entry(bd=2)     #TAMIL marks box
        self.t2=Entry(bd=2)     #maths marks box
        self.t3=Entry(bd=3)     #total marks box
        self.t4=Entry(bd=3)     #AVERAGE marks box
        self.btn1 = Button(win, text='TOTAL')                             #Total Button
        self.btn2 = Button(win, text='AVERAGE')                           #AVERAGE Button
        self.lbl1.place(x=100, y=50)            #TAMIL NAME BORT X-y scal
        self.t1.place(x=200, y=50)              #TAMIL marks box X-y scal
        self.lbl2.place(x=100, y=100)           #MATHS NAME BORT X-y scal
        self.t2.place(x=200, y=100)             #maths marks box X-y scal
        self.b1=Button(win, text='TOTAL', command=self.add)                 #TOTAL Button
        self.b2=Button(win, text='AVERAGE',command=self.AVERAGE)                                 #AVERAGE Button
        self.b2.bind('<Button-1>', self.AVERAGE)
        self.b1.place(x=100, y=200)             #TOTAL Button X-y scal
        self.b2.place(x=100, y=250)             #avg Button X-y scal
        self.t3.place(x=200, y=200)       #tot entr box
        self.t4.place(x=200, y=250)       #avg entr box

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def AVERAGE(self, event):
        self.t4.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=(num1+num2)/2
        self.t4.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('welcome to Total Marks')
window.geometry("400x300+500+200")
window.mainloop()
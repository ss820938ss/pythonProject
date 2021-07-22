from tkinter import *

root = Tk()
root.title("SiSO")
root.geometry("500x500+100+100")
root.resizable(False, False)

bx = 60
by = 60


def selectV(event):
    value = "값 : " + str(scaleV.get())
    label.config(text=value)
    bx = scaleV.get()
#    by = scaleH.get()
    buttonRight.place(x=bx, y=by)


def selectH(event):
    value = "값 : " + str(scaleH.get())
    label.config(text=value)
#    bx = scaleV.get()
    by = scaleH.get()
    buttonRight.place(x=bx, y=by)


var1 = IntVar()
ver2 = IntVar()


scaleV = Scale(root, variable=var1, orient="vertical", showvalue=True, tickinterval=10, to=300, length=300, command=selectV)
scaleV.pack()

scaleH = Scale(root, variable=var1, orient="horizontal", showvalue=True, tickinterval=10, to=300, length=300, command=selectH)
scaleH.pack()

label = Label(root, text='0')
label.pack()


buttonRight = Button(root, text="-----------------", overrelief="solid")
buttonRight.place(x=bx, y=by)

root.mainloop()

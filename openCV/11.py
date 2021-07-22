from tkinter import *

root = Tk()
root.title("SiSO")
root.geometry("500x500+100+100")
root.resizable(True, True)

frame1 = Frame(root, relief="ridge", bd=2)
frame1.pack(side="left", fill="both", expand=False)

frame2 = Frame(root, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

frame3 = Frame(root, relief="ridge", bd=2)
frame3.pack(side="right", fill="both", expand=True)

label1 = Label(frame1, text='Hello')
label1.pack()

label2 = Label(frame2, text='World!')
label2.pack()

buttonRight = Button(frame2, text="-------------", overrelief="solid")
buttonRight.pack()

root.mainloop()
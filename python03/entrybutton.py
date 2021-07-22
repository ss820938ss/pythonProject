import tkinter

window = tkinter.Tk()
window.title("계산기")
window.geometry("640x400+100+100")
window.resizable(False, False)


entry=tkinter.Entry(window)
entry.bind()
entry.pack()

entry=tkinter.Entry(window)
entry.bind()
entry.pack()

entry=tkinter.Entry(window)
entry.bind()
entry.pack()

button = tkinter.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()

from tkinter import *

root = Tk()
root.title("SiSO")
root.geometry("500x500+100+100")
root.resizable(True, True)

canvas = Canvas(root, width=200, height=150, bg="white", bd=2)
canvas.pack(fill="both", expand=True)   # 캔버스를 창 너비에 맞춰 동적으로 크기를 조정하게 한다

canvas.create_line(0, int(200/2), 100, int(200/2), fill="blue")

root.mainloop()
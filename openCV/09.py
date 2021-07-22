# tkinter로 메뉴 만들기
# filename : tk_menu1.py
# coding : utf-8

from tkinter import *

root = Tk()
root.title("SiSO")
root.geometry("300x200+100+100")
root.resizable(False, False)

def close():
    root.quit()
    root.destroy()

# 메뉴바를 만든다
menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New File")
menu1.add_command(label="Open...")
menu1.add_separator()
menu1.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=True, selectcolor="red")
menu2.add_radiobutton(label="Undo", state="disable")
menu2.add_radiobutton(label="Redo")
menu2.add_radiobutton(label="Cut")
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_checkbutton(label="Python Shell")
menu3.add_checkbutton(label="Check Module")
menu3.add_checkbutton(label="Run Module")
menubar.add_cascade(label="Run", menu=menu3)

root.config(menu=menubar)   # 윈도우창에 메뉴를 등록한다

root.mainloop()

# =============================

root = Tk()
root.title("SiSO")
root.geometry("300x200+100+100")
root.resizable(False, False)

def close():
    root.quit()
    root.destroy()

# 메뉴바를 만든다
menubutton = Menubutton(root,text="메뉴 메뉴버튼", relief="raised", direction="right")
menubutton.pack()

menu = Menu(menubutton, tearoff=0)
menu.add_command(label="New File")
menu.add_command(label="Open...")
menu.add_separator()
menu.add_command(label="Exit", command=close)

menubutton["menu"] = menu   # 메뉴버튼과 메뉴를 연결

root.mainloop()
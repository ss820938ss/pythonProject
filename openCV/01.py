# import tkinter
# from math import *
#
# window=tkinter.Tk()
# window.title("YUN DAE HEE")
# window.geometry("640x480+100+100")
# window.resizable(False, False)
#
# def calc(event):
#     label.config(text="결과="+str(eval(entry.get())))
#
# entry=tkinter.Entry(window)
# entry.bind("<Return>", calc)
# entry.pack()
#
# label=tkinter.Label(window)
# label.pack()
#
# window.mainloop()
# button = tkinter.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
# button.pack()
#
# window.mainloop()




import cv2
import numpy as np

# image = np.zeros((300, 400), np.uint8)
# image.fill(100)
#
# cv2.imshow("aaaaaaaaaa", image)
# cv2.imshow('bbbbb', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

image = np.zeros((200, 300), np.uint8)
# image[:] = 200
image.fill(255)
print(image)


title1, title2 = 'autosize', 'nomal'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.moveWindow(title1, 300, 400)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destroyAllWindows()



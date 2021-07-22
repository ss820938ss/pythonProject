# import tkinter
# from math import *
#
# window = tkinter.Tk()
# window.title("test")
# window.geometry("640x480+100+100")
# window.resizable(False, False)
#
#
# def entryTo_textbox(event):
#     # textbox.config(text="")
#     print(ontxt.get())
#     # textbox.config(wrap=tkinter.WORD)
#     textbox.insert(tkinter.END, ontxt.get())
#     ontxt.delete(0, tkinter.END)
#
#
# ontxt = tkinter.Entry(window)
# ontxt.bind('<Return>', entryTo_textbox)
# ontxt.pack()
#
# textbox = tkinter.Text(window, width=30, height=10)
# textbox.pack()
#
# listbox = tkinter.Listbox(window, selectmode="extended", height=0)  # 여러개선택
# # listbox = tkinter.Listbox(window, selectmode="single", height=0)  # 하나선택
# listbox.insert(0, '대한민국')
# listbox.insert(1, '만만세')
# listbox.insert(2, '동해물과')
# listbox.pack()
# # listbox.delete(1)
#
#
# def btncmd():
#     # listbox.delete(tkinter.END)  # 순서대로 밑에서부터 지우기
#     # print(listbox.get(0, 2))  # 튜플로 가져오기
#     # print(listbox.curselection())  # 선택된것만 가져오기(순서로)
#     print(listbox.get(listbox.curselection()[0]))  # 선택된것만 가져오기(내용으로)
#     ontxt.insert(0, listbox.get(listbox.curselection()[0]))  # 밑칸에서 쓴 내용 윗칸으로 올림
#
#
# button = tkinter.Button(window, text="지우세요", command=btncmd, width=15)
# button.pack()
#
# window.mainloop()

#
#
# def calc(event):
#     label.config(text="결과=" + str(eval(entry.get())))
#
#
# entry = tkinter.Entry(window)
# entry.bind("<Return>", calc)
# entry.pack()
#
# label = tkinter.Label(window)
# label.pack()
#
# button = tkinter.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
# button.pack()
#
# # photo = tkinter.PhotoImage(file="c:\pythonProject/openCV/fire-cracker.png")
# # button = tkinter.Button(window, image=photo, overrelief="solid")
# # button.pack()
#
# textbox = tkinter.Text()
#
# window.mainloop()


#  ================================================

import numpy as np
import cv2


# # 콜백 함수 : event값에 따른 마우스 버튼 종류 구분
# def onMouse(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("마우스 왼쪽 버튼 누르기")
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         print("마우스 오른쪽 버튼 누르기")
#     elif event == cv2.EVENT_RBUTTONUP:
#         print("마우스 오른쪽 버튼 떼기")
#     elif event == cv2.EVENT_LBUTTONDBLCLK:
#         print("마우스 왼쪽 버튼 더블클릭")
#
# image = np.full((200, 300), 255, np.uint8)          # 영상 생성
#
# title1, title2 = "Mouse Event1", "Mouse Event2"     # 윈도우 이름
# cv2.imshow(title1, image) # 영상 보기
# cv2.imshow(title2, image)
#
# cv2.setMouseCallback('Mouse Event1', onMouse)     	# 마우스 콜백 함수
# cv2.waitKey(0)                                      # 키 이벤트 대기
# cv2.destroyAllWindows()                             # 열린 모든 윈도우 제거

def onChange(value):
    global image, title  # 전역 변수 참조

    add_value = value - int(image[0][0])  # 트렉바 값과 영상화소값 차분
    image = image + add_value
    cv2.imshow(title, image)


def onMouse(event, x, y, flags, param):  # 마우스 콜백 함수
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 246): image = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])  # 트랙바 위치 변경
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >= 10): image = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])  # 트랙바 위치 변경
        cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = "Trackbar & Mouse Event"  # 윈도우 이름
bar_name = "Brightness"  # 트랙바 이름
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)  # 트랙바 콜백 함수
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()  # 모든 윈도우 닫기

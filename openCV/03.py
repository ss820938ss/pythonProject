# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title("test")
# root.geometry("640x480+100+100")
# root.resizable(False, False)
#
#
# def show():
#     print("item1: %d,\nitem2: %d,\nitem3: %d\n" % (variety1.get(), variety2.get(), variety3.get()))
#     messagebox.showinfo("Button Clicked",
#                         "item1: {0},\nitem2: {1},\nitem3: {2}\n".format(variety1.get(), variety2.get(), variety3.get()))
#
#
# def selectall():
#     bt1.select()
#     bt2.select()
#     bt3.select()
#
#
# def deselectall():
#     bt1.deselect()
#     bt2.deselect()
#     bt3.deselect()
#
#
# variety1 = IntVar()
# variety2 = IntVar()
# variety3 = IntVar()
#
# bt1 = Checkbutton(root, text="item1", variable=variety1)
# bt2 = Checkbutton(root, text="item2", variable=variety2)
# bt3 = Checkbutton(root, text="item3", variable=variety3)
#
# bt1.pack()
# bt2.pack()
# bt3.pack()
#
# buttonSelectAll = Button(root, width=10, text="전체선택", overrelief="solid", command=selectall)
# buttonSelectAll.pack()
#
# buttonDeSelectAll = Button(root, width=10, text="전체취소", overrelief="solid", command=deselectall)
# buttonDeSelectAll.pack()
#
# button = Button(root, width=10, text="Show", overrelief="solid", command=show)
# button.pack()
#
# root.mainloop()

# import cv2
#
#
# def put_string(frame, text, pt, value, color=(120, 200, 90)):             # 문자열 출력 함수 - 그림자 효과
#     text += str(value)
#     shade = (pt[0] + 2, pt[1] + 2)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
#     cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기
#
#
# capture = cv2.VideoCapture(0)  # 0번 카메라 연결
# if capture.isOpened() == False:
#     raise Exception("카메라 연결 안됨")
#
#
# # 카메라 속성 획득 및 출력
# print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
# print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))
#
# while True:  # 무한 반복
#     ret, frame = capture.read()  # 카메라 영상 받기
#     if not ret: break
#     if cv2.waitKey(30) >= 0: break
#
#     exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
#     put_string(frame, "EXPOS: ", (10, 40), exposure)
#     title = "View Frame from Camera"
#     cv2.imshow(title, frame)  # 윈도우에 영상 띄우기
# capture.release()



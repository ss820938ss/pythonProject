import time
from PIL import Image, ImageTk

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkCamera import *
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from MyVideoCapture import *

class tkCamera(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.window = parent
        self.repeat = controller.repeat
        self.video_source = controller.sources
        self.vid = MyVideoCapture(self.window, controller.sources, controller.width, controller.height)
        self.canvas = tk.Canvas(self, width=controller.width*2, height=controller.height)
        self.canvas.pack()
        self.btn_snapshot = tk.Button(self, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor='center', expand=True)
        self.delay = 15
        self.update_widget()
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update_widget(self):
        ret, frame = self.vid.get_frame()
        if self.repeat == 1 :
            rep_image = cv2.repeat(frame, 1, 2)  # 가로 반복 복사
        else:
            rep_image = cv2.repeat(frame, 1, 1)  # 가로 반복 복사
        rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
        rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)  # 가우시안 블러링
        rep_edge = cv2.Canny(rep_edge, 50, 50 * 2, 5)  # 캐니 에지 검출
        h, w = frame.shape[:2]
        cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1)  # 흰색 사각형 그리기
        color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)

        if ret:
            self.image = Image.fromarray(color_edge)
            self.photo = ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_widget)

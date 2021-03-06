import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import time

from partd.utils import frame

from Tkinter_window_04.MyVideoCapture import *


class tkCamera(tkinter.Frame):

    def __init__(self, window, text="", video_source=0, width=None, height=None, repeat=0):
        super().__init__(window)

        self._frame = None

        self.window = window
        self.repeat = repeat

        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source, width, height)

        self.label = tkinter.Label(self, text=text)
        self.label.pack()

        if self.repeat == 1:

            self.canvas = tkinter.Canvas(self, width=self.vid.width * 2, height=self.vid.height * 2)
        else:
            self.canvas = tkinter.Canvas(self, width=self.vid.width, height=self.vid.height)

        self.canvas.pack()

        self.btn_snapshot = tkinter.Button(self, text="Start", command=self.start)
        self.btn_snapshot.pack(anchor='center', side='left')

        self.btn_snapshot = tkinter.Button(self, text="Stop", command=self.stop)
        self.btn_snapshot.pack(anchor='center', side='left')

        self.btn_snapshot = tkinter.Button(self, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(anchor='center', side='left')

        self.btn_switch = tkinter.Button(self, text="Switch", command=lambda: self.switch(PageOne))
        self.btn_switch.pack(anchor='center', side='left')

        self.delay = int(1000 / self.vid.fps)

        print('[tkCamera] source:', self.video_source)
        print('[tkCamera] fps:', self.vid.fps, 'delay:', self.delay)

        self.image = None

        self.running = True
        self.update_frame()

    def start(self):
        if not self.running:
            self.running = True
            self.update_frame()

    def stop(self):
        if self.running:
            self.running = False

    def snapshot(self):
        if self.image:
            self.image.save(time.strftime("frame-%d-%m-%Y-%H-%M-%S.jpg"))

    def update_frame(self):
        ret, frame = self.vid.get_frame()

        if ret:
            if self.repeat == 1:
                frame = cv2.repeat(frame, 2, 2)  # ?????? ?????? ??????
                # rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)  # ????????? ?????? ??????
                # rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)  # ???????????? ?????????
                # rep_edge = cv2.Canny(rep_edge, 50, 50 * 2, 5)  # ?????? ?????? ??????
                h, w = frame.shape[:2]
                # cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1)  # ?????? ????????? ?????????
                # frame = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)

            self.image = PIL.Image.fromarray(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

        if self.running:
            self.window.after(self.delay, self.update_frame)


class StartPage(tk.Frame):
    def __init__(self, master, text="", video_source=0, width=None, height=None, repeat=0):
        tk.Frame.__init__(self, master)
        self.text = text
        self.video_source = video_source
        self.width = width
        self.height = height
        self.repeat = repeat

        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(self, self.text, self.video_source, self.width, self.height, self.repeat)).pack()


class SampleApp(tk.Frame):
    def __init__(self, window, text="", video_source=0, width=None, height=None, repeat=0):
        self._frame = None
        self.text = text
        self.window = window
        self.video_source = video_source
        self.width = width
        self.height = height
        self.repeat = repeat
        if repeat == 1 :
            self.switch_frame(StartPage)
        else:
            self.switch_frame(tkCamera)

    def switch_frame(self, frame_class, text="", video_source=0, width=None, height=None, repeat=0):
        self._frame = None
        self.text = text
        self.video_source = video_source
        self.width = width
        self.height = height
        self.repeat = repeat
        new_frame = frame_class(self.window,self.text, self.video_source, self.width, self.height, self.repeat)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

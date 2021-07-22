import threading
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time


class MyVideoCapture:

    def __init__(self, video_source=0, width=None, height=None, fps=None):

        self.video_source = video_source
        self.width = width
        self.height = height
        self.fps = fps

        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("[MyVideoCapture] Unable to open video source", video_source)

        if not self.width:
            self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        if not self.height:
            self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if not self.fps:
            self.fps = int(self.vid.get(cv2.CAP_PROP_FPS))

        self.ret = False
        self.frame = None

        self.running = True
        self.thread = threading.Thread(target=self.process)
        self.thread.start()

    def process(self):
        while self.running:
            ret, frame = self.vid.read()

            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # frame = cv2.Laplacian(frame, cv2.CV_16S, 1)
                #     # cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)  # YUV 컬러 공간 변환
                #     # cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) # YCbCr 컬러 공간 변환
                #     # cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 명암도 영상 변환
                #     # cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)  # La*b* 컬러 공간 변환
            else:
                print('[MyVideoCapture] stream end:', self.video_source)
                # TODO: reopen stream
                self.running = False
                break

            self.ret = ret
            self.frame = frame

            time.sleep(1 / self.fps)

    def get_frame(self):
        return self.ret, self.frame

    def __del__(self):
        # stop thread
        if self.running:
            self.running = False
            self.thread.join()

        if self.vid.isOpened():
            self.vid.release()

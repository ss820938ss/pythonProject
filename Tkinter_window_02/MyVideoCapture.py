import tkinter
import cv2


class MyVideoCapture:
    def __init__(self, window, video_source, width=None, height=None):
        self.window = window
        self.source = video_source

        self.width = width
        self.height = height

        self.vid = cv2.VideoCapture(self.source)

        if not self.vid.isOpened():
            raise ValueError("영상을 열 수 없습니다.", video_source)

        if not self.width:
            self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        if not self.height:
            self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.ret = False
        self.frame = None

    def process(self):
        ret = False
        frame = None

        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.ret = ret
        self.frame = frame

    def get_frame(self):
        self.process()
        return self.ret, self.frame

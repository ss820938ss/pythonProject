import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from tkCamera import *
class App:
    def __init__(self, window, window_title, video_sources):
        self.window = window
        self.window.title(window_title)

        self.vids = []

        for source in video_sources:
            vid = tkCamera(window, source, 400, 300, 1)
            vid.pack()
            self.vids.append(vid)

        self.window.mainloop()


if __name__ == '__main__':

    # Create a window and pass it to the Application object
    App(tkinter.Tk(), "Tkinter and OpenCV", sources)
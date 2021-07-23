try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkCamera import *
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2


class App:

    def __init__(self, window, window_title, video_sources):
        self.window = window
        self.window.title(window_title)
        self.vids = []

        columns = 2

        for number, source in enumerate(video_sources):
            text, stream = source
            vid = tkCamera(self.window, text, stream, 300, 200, 1)
            x = number % columns
            y = number // columns
            vid.grid(row=y, column=x)
            self.vids.append(vid)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self, event=None):
        print('[App] stoping threads')
        for source in self.vids:
            source.vid.running = False
        print('[App] exit')
        self.window.destroy()
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="화면 분할", font=controller.title_font)
        label.pack(side="left", fill="x", pady=10)
        
        button1 = tk.Button(self, text="에지 검출", width=20, command=lambda: controller.show_frame("PageOne"))
        button1.pack(anchor='center', side='left')
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", width=20,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(anchor='center', side='left')

        button2 = tk.Button(self, text="tkCamera", width=20,
                           command=lambda: controller.show_frame("tkCamera"))
        button2.pack(anchor='center', side='left')

        self.btn_snapshot = tk.Button(self, text="Snapshot", width=20, command=self.snapshot)
        self.btn_snapshot.pack(anchor='center', side='left', expand=True)


if __name__ == '__main__':
    sources = [
        ('me', 0),
        ('Zakopane, Poland', 'https://imageserver.webcamera.pl/rec/krupowki-srodek/latest.mp4'),
        ('Kraków, Poland', 'https://imageserver.webcamera.pl/rec/krakow4/latest.mp4'),
        ('Warszawa, Poland', 'https://imageserver.webcamera.pl/rec/warszawa/latest.mp4'),
        # ('Baltic See, Poland', 'https://imageserver.webcamera.pl/rec/chlopy/latest.mp4'),
        # ('Mountains, Poland', 'https://imageserver.webcamera.pl/rec/skolnity/latest.mp4'),
    ]

    App(tkinter.Tk(), "Tkinter and OpenCV", sources)

import tkinter as tk
from tkinter.constants import BOTTOM

from widgets.screen_viewer.widget import Screen_Viewer_Widget

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, height= 1000, width=500)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.e1 = Screen_Viewer_Widget(parent=self)
        self.e1.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side=tk.BOTTOM)

    def say_hi(self):
        print("hi there, everyone!")



root = tk.Tk()
root.geometry("1000x500")
app = Application(master=root)
app.mainloop()
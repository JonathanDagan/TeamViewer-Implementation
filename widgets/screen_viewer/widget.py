import tkinter as tk

from cursor_handler import cursor


from PIL import ImageTk, Image  


class Screen_Viewer_Widget(tk.Frame):
    def __init__(self, parent, label, default=""):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text=label, anchor="w")
        self.entry = tk.Entry(self)
        self.entry.insert(0, default)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="bottom", fill="x", padx=4)


        image1 = Image.open('widgets\\screen_viewer\\test-img.png')
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)

        self.bind('<Motion>', cursor().motion)

    def get(self):
        return self.entry.get()


# from cursor_handler import cursor

# root = tk.Tk()
# root.geometry("500x200")
# root.bind('<Motion>', cursor().motion)
# # app = Application(master=root)
# # app.mainloop()
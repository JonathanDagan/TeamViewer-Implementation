import tkinter as tk


from .cursor_handler import cursor


from PIL import ImageTk, Image  


class Screen_Viewer_Widget(tk.Widget):
    def __init__(self, parent):
        tk.Frame.__init__(
            self,parent,
            height=400,
            width=150,
            background='red',
            border=5
            )
        

        # image1 = Image.open('widgets/screen_viewer/test-img.png')
        # test = ImageTk.PhotoImage(image1)
        # label1 = tk.Label(image=test)
        # label1.image = test
        # label1.place(x=0,y=0)

        self.bind('<Button-1>', cursor.right_click)
        self.bind('<Button-3>', print('right click'))
        # self.bind('<Motion>', cursor().motion)

    def get(self):
        return self.entry.get()


# from cursor_handler import cursor

# root = tk.Tk()
# root.geometry("500x200")
# root.bind('<Motion>', cursor().motion)
# # app = Application(master=root)
# # app.mainloop()
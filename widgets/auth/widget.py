import tkinter as tk
from random import randint


class Auth_Widget(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self,parent,border=5)
        
        self.token = tk.StringVar(value=self.__rand_token())
        self.input = tk.StringVar()
        self.input.trace("w", lambda name, index, node, sv=self.input, callback=(self.input.get()))


        self.key = tk.Label(parent, text=self.token.get())
        self.key.place(x=3,y=3)

        self.input = tk.Entry(parent, bd=5, textvariable=self.input)
        self.input.pack()

        self.input_button = tk.Button(parent, text="submit", bd=5, command=self.test)
        self.input_button.pack()

    def test(self):
        print(self.__do_tokens_match())

        print("the test method has been called")

    def __do_tokens_match(self) -> bool:
        if self.token == self.input:
            return True
        return False

    def __rand_token(self) -> str:
        return str(randint(100000,999999))
from tkinter import Tk, Canvas, Frame, BOTH, Menu, Toplevel, Button

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graphics(Frame):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        self.color ="#000"
        self.fill_color = "#ff0"
        self.background_color = "#fff"

    def clear(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.rectangle(Point(0,0), Point(width-1, height-1), fill_color=self.background_color)

    def set_color(self, color):
        self.color = color

    def set_fill_color(self, color):
        self.fill_color = color

    def line(self, p1, p2, color=None):
        if(not color): color = self.color
        self.canvas.create_line(p1.x, p1.y, p2.x, p2.y,
                                 fill=color)
        self.canvas.pack(fill=BOTH, expand=1)

    def rectangle(self, p1, p2, fill_color=None, color=None):
        if(not fill_color): fill_color = self.fill_color
        if(not color): color = self.color
        self.canvas.create_rectangle(p1.x, p1.y, p2.x, p2.y, outline=color, fill=fill_color)
        self.canvas.pack(fill=BOTH, expand=1)
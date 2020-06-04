from tkinter import Tk, Canvas, Frame, BOTH, Menu, Toplevel, Button
from tkcolorpicker import askcolor
from mygraphics import Point, Graphics


def line(root, graphics):
    def _line():
        graphics.line(Point(0, 0), Point(100, 100))
    return _line

def select_color(root, graphics):
    def _select_color():
        color = askcolor((255, 255, 0), root)
        graphics.set_color(color[1])
    return _select_color


def select_fill_color(root, graphics):
    def _select_color():
        color=  askcolor((255, 255, 0), root)
        graphics.set_fill_color(color[1])
    return _select_color


def square(root, graphics):
    def _square():
        graphics.rectangle(Point(10, 10), Point(100, 100))
    return _square


def donothing(root, graphics):
    def _donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()
    return _donothing

def quit(root=None, graphics=None):
    def _quit():
        root.destroy()
    return _quit

def create_menu(root, graphics):


    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=quit)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=quit(root, graphics))
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_command(label="Line", command=line(root, graphics))
    editmenu.add_command(label="Square", command=square(root, graphics))
    editmenu.add_command(label="Select Color", command=select_color(root, graphics))
    editmenu.add_command(label="Select Fill Color", command=select_fill_color(root, graphics))


    menubar.add_cascade(label="Shapes", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


def main():

    root = Tk()
    root.geometry("400x300+00+00")

    graphics = Graphics()
    create_menu(root, graphics)
    root.mainloop()



if __name__ == '__main__':
    main()
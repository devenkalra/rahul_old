from tkinter import Tk, Canvas, Frame, BOTH, Menu, Toplevel, Button
from tkcolorpicker import askcolor
from mygraphics import Point, Graphics

class MenuFunctions:
    def __init__(self, root, graphics):
        self.root = root
        self.graphics = graphics

    def line(self):
        def _line():
            self.graphics.line(Point(0, 0), Point(100, 100))
        return _line

    def select_color(self):
        def _select_color():
            color = askcolor((255, 255, 0), self.root)
            self.graphics.set_color(color[1])
        return _select_color


    def select_fill_color(self):
        def _select_color():
            color=  askcolor((255, 255, 0), self.root)
            self.graphics.set_fill_color(color[1])
        return _select_color


    def square(self):
        def _square():
            self.graphics.rectangle(Point(10, 10), Point(100, 100))
        return _square


    def donothing(self):
        def _donothing():
            filewin = Toplevel(self.root)
            button = Button(filewin, text="Do nothing button")
            button.pack()
        return _donothing

    def point_line(self):
        def _point_line():
            self.first_point = None
            self.second_point = None

            def motion2(event):
                print("Mouse position: (%s %s)" % (event.x, event.y))
                self.second_point = Point(event.x, event.y)
                self.graphics.line(self.first_point, self.second_point)
                return

            def motion1(event):
                global first_point
                print("Mouse position: (%s %s)" % (event.x, event.y))
                self.first_point = Point(event.x, event.y)
                self.root.bind('<Button-1>', motion2)
                return

            self.root.bind('<Button-1>', motion1)
        return _point_line;




    def quit(self):
        def _quit():
            self.root.destroy()
        return _quit

def create_menu(root, graphics):

    menu = MenuFunctions(root, graphics)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=menu.donothing())
    filemenu.add_command(label="Open", command=menu.donothing())
    filemenu.add_command(label="Save", command=menu.donothing())
    filemenu.add_command(label="Save as...", command=menu.donothing())
    filemenu.add_command(label="Close", command=quit)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=menu.quit())
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_command(label="Line", command=menu.line())
    editmenu.add_command(label="Point Line", command=menu.point_line())
    editmenu.add_command(label="Square", command=menu.square())
    editmenu.add_command(label="Select Color", command=menu.select_color())
    editmenu.add_command(label="Select Fill Color", command=menu.select_fill_color())


    menubar.add_cascade(label="Shapes", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=menu.donothing())
    helpmenu.add_command(label="About...", command=menu.donothing())
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
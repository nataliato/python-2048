from view import *


class Main:
    def __init__(self, view):
        self.view = view
        self.view.title('← ↑ → ↓')
        self.create()
        self.play()
        self.frame.pack_forget()
        self.table = View(self.view, 4, 4)
        self.table.pack()
        self.table.show()

    def create(self):
        self.frame = Frame(self.view)
        f1 = Frame(self.frame)
        f1.pack()

    def play(self):
        self.frame.pack()


if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()

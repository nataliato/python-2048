from tkinter import messagebox, Frame, Label, Tk
from array import *
import tkinter.messagebox


class View(Frame):
    def __init__(self, view, row, col, *args, **kwargs):
        Frame.__init__(self, view, *args, **kwargs)

        self.view = view
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.empty = ''
        self.win = 2048

        self.view.bind('<Key>', self.move)

        self.gridFrame = Frame(self)
        self.gridFrame.pack()

        self.array = Array(row, col, self.empty)
        self.array.addDigit()

    def show(self):
        for child in self.winfo_children():
            child.grid_forget()

        for i in range(self.row):
            for j in range(self.col):
                Label(self.gridFrame, text=self.array[i][j], bg='grey', fg='white', font=('', 30),
                      width=2, height=1).grid(row=i, column=j, padx=2, pady=2)

    def move(self, event):
        key = event.keysym

        oldArray = self.array
        if key == 'Right':
            self.array.sum()
            self.array.move(1)
        elif key == 'Left':
            self.array.sum()
            self.array.move(-1)
        elif key == 'Down':
            self.array.shift()
            self.array.sum()
            self.array.move(1)
            self.array.shift()
        elif key == 'Up':
            self.array.shift()
            self.array.sum()
            self.array.move(-1)
            self.array.shift()
        else:
            tkinter.messagebox.showinfo("", "use ← ↑ → ↓")
            return

        if oldArray != self.array.get():

            if self.array.contains(element=self.win):
                self.show()
                tkinter.messagebox.showinfo("", "You won!")
                exit(0)

            self.array.addDigit()

            if not self.array.contains(element=self.empty):
                self.show()
                tkinter.messagebox.showinfo("", "Game over")
                exit(0)

            self.show()

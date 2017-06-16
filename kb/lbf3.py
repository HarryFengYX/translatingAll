from tkinter import *

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class talkinter():
    def __init__(self, root):
        self.ety = Entry(root)
        self.ety.bind('<Key-Return>', self.upd)
        self.ety.pack()
        self.ety.focus_force()
        self.lb = Label(text="How can I help?")
        self.lb.pack()

    def upd(self, event):
        self.lb['text'] = 'you said '+ self.ety.get()

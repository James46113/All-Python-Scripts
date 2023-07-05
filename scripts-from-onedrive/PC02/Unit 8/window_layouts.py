from tkinter import *

class EventWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.minsize(300, 200)
        self.tk.bind("<Key>", self.key)
        self.tk.bind("<Button-1>", self.click)
        self.tk.bind("<Motion>", self.pos)
        self.mouse_pos = StringVar()
        self.mouse_press = StringVar()
        self.key_press = StringVar()
        self.f1 = Frame(self.tk)
        Label(self.f1, text="Mouse pos:").pack(side=LEFT, ipadx=20, ipady=20)
        Label(self.f1, textvariable=self.mouse_pos, bg="#364253").pack(side=LEFT, ipadx=20, ipady=20)
        self.f1.pack(side=LEFT)
        self.f2 = Frame(self.tk)
        Label(self.f2, text="Mouse last pressed:").pack(side=LEFT, ipadx=20, ipady=20)
        Label(self.f2, textvariable=self.mouse_press, bg="#8351f7").pack(side=LEFT, ipadx=20, ipady=20)
        self.f2.pack(side=LEFT)
        self.f3 = Frame(self.tk)
        Label(self.f3, text="Last button pressed:").pack(side=LEFT, ipadx=20, ipady=20)
        Label(self.f3, textvariable=self.key_press, bg="#2748ac").pack(side=LEFT, ipadx=20, ipady=20)
        self.f3.pack(side=LEFT)
    
    def key(self, event):
        self.key_press.set(event.keysym)
    
    def pos(self, event):
        self.mouse_pos.set(f"{event.x}, {event.y}")
        
    def click(self, event):
        self.mouse_press.set(f"{event.x}, {event.y}")
        
    def start(self):
        self.tk.mainloop()
        
        
window = EventWindow()
window.start()
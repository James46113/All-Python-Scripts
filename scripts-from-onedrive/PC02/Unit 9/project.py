from math import sqrt
from tkinter import *
from time import sleep
from random import choice


class Shape2D:
    def perim(self):
        pass
    
    def area(self):
        pass
    
    
class Rectangle2D(Shape2D):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        print(self.width * self.height)
        
    def perim(self):
        print(self.width * 2 + self.height * 2)
        
    def type(self):
        return "rect"
    
    def __str__(self):
        return f"Rectangle: width: {self.width}, height: {self.height}"
    
    
class Triangle2D(Shape2D):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        self.__hippo = sqrt(base**2+height**2)
    
    def area(self):
        print(0.5*self.__base*self.__height)
    
    def perim(self):
        print(self.__base+self.__height+self.__hippo)
        
    def type(self):
        return "tri"
        
    def __str__(self):
        return f"Triangle: base: {self.__base}, height: {self.__height}"


class Circle2D(Shape2D):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(3.14 * self.radius ** 2)
        
    def type(self):
        return "circle"
        
    def perim(self):
        print(2 * 3.14 * self.radius)
        
    def __str__(self):
        return f"Circle: radius: {self.radius}"


class ShapeWindow:
    def __init__(self):
        self.object_list = []
        self.tk = Tk()
        self.cir_f = Frame(self.tk)
        self.cir_l = Label(self.cir_f, text="Circle")
        self.cir_e = Entry(self.cir_f)
        self.cir_b = Button(self.cir_f, text="Go", command=self.cir)
        self.cir_l.pack(side=LEFT)
        self.cir_e.pack(side=LEFT)
        self.cir_b.pack(side=LEFT)
        self.cir_f.pack()
        
        self.rect_f = Frame(self.tk)
        self.rect_l = Label(self.rect_f, text="Rectangle")
        self.rect_e = Entry(self.rect_f)
        self.rect_b = Button(self.rect_f, text="Go", command=self.rect)
        self.rect_l.pack(side=LEFT)
        self.rect_e.pack(side=LEFT)
        self.rect_b.pack(side=LEFT)
        self.rect_f.pack()
        
        self.tri_f = Frame(self.tk)
        self.tri_l = Label(self.tri_f, text="Triangle")
        self.tri_e = Entry(self.tri_f)
        self.tri_b = Button(self.tri_f, text="Go", command=self.tri)
        self.tri_l.pack(side=LEFT)
        self.tri_e.pack(side=LEFT)
        self.tri_b.pack(side=LEFT)
        self.tri_f.pack()
        
        Button(text="Print list", command=self.list_print).pack()
        Button(text="Show all", command=self.show_all).pack()
        
        self.show_frame = Frame(self.tk)
        self.canvas = Canvas(self.show_frame)
        self.canvas.pack()
        self.show_frame.pack()
        
    def show_all(self):
        choi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        for obj in self.object_list:
            colour = "#"
            for x in range(6):
                colour += choice(choi)
            
            self.canvas.delete("all")
            if obj.type() == "circle":
                self.canvas.create_oval(50, 50, obj.radius, obj.radius, fill=colour)
            elif obj.type() == "rect":
                self.canvas.create_rectangle(0, 0, obj.width, obj.height, fill=colour)
            self.canvas.update()
            sleep(0.5)

    def list_print(self):
        for ob in self.object_list:
            print(ob)
    
    def cir(self):
        self.canvas.delete("all")
        self.object_list.append(Circle2D(int(self.cir_e.get())))
        self.canvas.create_oval(50, 50, int(self.cir_e.get()), int(self.cir_e.get()), fill="black")
        self.cir_e.delete(0, "end")
    
    def tri(self):
        temp1, temp2 = self.tri_e.get().split(",")
        self.object_list.append(Triangle2D(int(temp1), int(temp2)))
        self.tri_e.delete(0, "end")
    
    def rect(self):
        self.canvas.delete("all")
        temp1, temp2 = self.rect_e.get().split(",")
        self.object_list.append(Rectangle2D(int(temp1), int(temp2)))
        self.rect_e.delete(0, "end")
        self.canvas.create_rectangle(0, 0, temp1, temp2, fill="black")
    
    def start(self):
        self.tk.mainloop()


x = ShapeWindow()
x.start()
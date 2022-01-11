import tkinter as tk
import math

class App:
    def __init__(self):
        self.flag_init = False
        self.flag_final = False
        self.pos = []
        self.coords = {"x":0,"y":0,"x2":0,"y2":0}
        self.final=[]
        self.lines = []
        self.line = 0
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1, width=600, height=600, background='gainsboro')
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind('<Motion>', self.mover_mouse)
        self.canvas1.bind('<Button-3>', self.click_mouse)
        #self.canvas1.bind('<Button-3>',self.click_line)
        self.canvas1.bind("<ButtonPress-1>", self.click_line)
        self.canvas1.bind("<B1-Motion>", self.drag) 
        self.canvas1.bind('<ButtonRelease-1>', self.release)   
        self.ventana1.mainloop()

    def dist(self, x1, y1, x2, y2):
        d = math.sqrt((abs(x2-x1)**2)+(abs(y2-y1)**2))
        #self.canvas1.create_line(x1, y1, x2, y2)
        return d

    def largo(self, x1, y1, x2, y2):
        l = math.sqrt((abs(x2-x1)**2)+(abs(y2-y1)**2))
        #self.canvas1.create_line(x1, y1, x2, y2)
        return l

    def mover_mouse(self, evento):
        self.ventana1.title(str(evento.x)+'-'+str(evento.y))
    
    def click_mouse(self, evento):
        l = len(self.pos)
        rg = True
        for i in range(l):
            if (self.dist(evento.x, evento.y, self.pos[i][0], self.pos[i][1])) < 50:
                rg = False
        if rg:    
            self.canvas1.create_oval(evento.x-8, evento.y-8, evento.x+8, evento.y+8, fill = 'lightblue1')
            self.canvas1.create_text(evento.x,evento.y, fill="black", font=("Arial", 8), text=str(len(self.pos)))
            var = [evento.x, evento.y]
            self.pos.append(var)
    
    def click_line(self, e):
        self.coords["x"] = e.x
        self.coords["y"] = e.y
        l = len(self.pos)
        i = 0
        salir = False
        while  i < l and not salir and l>1:
            d = self.dist(self.pos[i][0], self.pos[i][1], e.x, e.y)
            #print(d)
            if (d < 50):
                self.coords["x"]=self.pos[i][0]
                self.coords["y"]=self.pos[i][1]
                salir = True
                i = 0
                self.flag_init = True
            else:
                i = i+1
        if salir and l>1:
            self.line = self.canvas1.create_line(self.coords["x"],self.coords["y"],self.coords["x"],self.coords["y"])
            self.lines.append(self.line)
            self.canvas1.tag_lower(self.line)
        else:
            self.flag_init = False
        

    def release(self , l):
        lis=[]
        lis.append(self.coords["x"]);lis.append(self.coords["y"]);lis.append(self.coords["x2"]);lis.append(self.coords["y2"])
        if self.coords["x"] != self.coords["x2"] and self.coords["y"] != self.coords["y2"] and self.flag_final:
            #if 
            self.final.append(lis)
        elif self.flag_init:
            #print('?', self.flag_final)
            self.canvas1.delete(self.line)
        
        #print('coords: ', self.coords)
        #print('final: ', self.final)
        #print('lis: ', lis)

    def drag(self, e):
        self.coords["x2"] = e.x
        self.coords["y2"] = e.y
        l = len(self.pos)
        i = 0
        salir = False
        d = 100
        while l>0 and i < l and not salir and l>1:
            d = self.dist(self.pos[i][0], self.pos[i][1], e.x, e.y)
            #print(d)
            if (d < 50):
                self.coords["x2"]=self.pos[i][0]
                self.coords["y2"]=self.pos[i][1]
                salir = True
                i = 0
                self.flag_final = True
            else:
                i = i+1
                self.flag_final = False
        #if self.coords["x"] == self.coords["x2"] and self.coords["y"] == self.coords["y2"]:

        if l>1 and self.flag_init:
            self.canvas1.coords(self.lines[-1], self.coords["x"],self.coords["y"],self.coords["x2"],self.coords["y2"])
        #else:
            #self.flag_final = False

app1 = App()
import mtxp
import tkinter as tk
import math
from os import system

class App:
    def __init__(self):
        self.release_click = 0
        self.flag_init = False
        self.flag_final = False
        #self.pos = [] #node coords array
        self.coords = {"x1":0,"y1":0,"x2":0,"y2":0} #line coords
        self.final=[] #coords aristas (x1,y1,x2,y2)
        self.line = 0
        self.weighing = 0
        self.temp_weight= 0
        self.graph = []

        self.window = tk.Tk()

        self.menubar = tk.Menu(self.window)
        self.window.config(menu = self.menubar)

        self.actmenu = tk.Menu(self.menubar, tearoff=0)
        self.algmenu = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="Acciones", menu = self.actmenu)
        self.menubar.add_cascade(label="Algoritmos", menu = self.algmenu)

        self.actmenu.add_command(label="Borrar nodo")
        self.actmenu.add_command(label="Borrar arista")

        self.algmenu.add_command(label="Ford Fulkerson")

        self.canvas1 = tk.Canvas(self.window, width=600, height=600, background='gainsboro')
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind('<Motion>', self.move_mouse)
        self.canvas1.bind('<Button-3>', self.click_mouse)
        self.canvas1.bind("<ButtonPress-1>", self.click_line)
        self.canvas1.bind("<B1-Motion>", self.drag) 
        self.canvas1.bind('<ButtonRelease-1>', self.release)
        self.window.bind('<Key>', self.keys)  
        self.window.mainloop()

    def dist(self, x1, y1, x2, y2):
        d = math.sqrt((abs(x2-x1)**2)+(abs(y2-y1)**2))
        return d
    
    def midpoint (self, x1, y1, x2, y2):
        return [(x1+x2)/2, (y1+y2)/2]

    def keys(self, envent):
        key = envent.char
        if key == 'i':
            mtxp.imprimir_graph(self.graph)
        elif key == 'c':
            self.canvas1.delete("all")
            self.release_click = 0
            self.flag_init = False
            self.flag_final = False
            self.coords = {"x1":0,"y1":0,"x2":0,"y2":0}
            self.final=[]
            self.line = 0
            self.weighing = 0
            self.temp_weight= 0
            self.graph = []
        elif key == 'q':
            quit()

    def move_mouse(self, envent):
        self.window.title(str(envent.x)+'-'+str(envent.y))
    
    def click_mouse(self, envent): #right click to create node
        # l = len(self.pos)
        l = len(self.graph)
        rg = True
        for i in range(l): #new node does not superpose all other nodes created
            # if (self.dist(envent.x, envent.y, self.pos[i][0], self.pos[i][1])) < 50:
            if (self.dist(envent.x, envent.y, self.graph[i].coords[0], self.graph[i].coords[1])) < 50:
                rg = False
        if rg:    
            node_canvas = self.canvas1.create_oval(envent.x-8, envent.y-8, envent.x+8, envent.y+8, fill = 'lightblue1')
            # self.canvas1.create_text(envent.x,envent.y, fill="black", font=("Arial", 8), text=str(len(self.pos)))
            self.canvas1.create_text(envent.x,envent.y, fill="black", font=("Arial", 8), text=str(l))
            var = [envent.x, envent.y]
            #self.pos.append(var)
            #node = mtxp.node(len(self.pos)-1, var)
            node = mtxp.node(len(self.graph)-1, var)
            self.graph.append(node)
    
    def click_line(self, e): #left click to create line
        self.coords["x1"] = e.x
        self.coords["y1"] = e.y
        l = len(self.graph)
        i = 0
        salir = False
        while  i < l and not salir and l>1:
            #d = self.dist(self.pos[i][0], self.pos[i][1], e.x, e.y)
            d = self.dist(self.graph[i].coords[0], self.graph[i].coords[1], e.x, e.y)
            if (d < 50):
                # self.coords["x1"]=self.pos[i][0]
                # self.coords["y1"]=self.pos[i][1]
                self.coords["x1"]=self.graph[i].coords[0]
                self.coords["y1"]=self.graph[i].coords[1]
                salir = True
                i = 0
                self.flag_init = True
            else:
                i = i+1
        if salir and l>1:
            self.line = self.canvas1.create_line(self.coords["x1"],self.coords["y1"],self.coords["x1"],self.coords["y1"])
            self.canvas1.tag_lower(self.line)
            self.weighing = self.canvas1.create_text(0, 0, fill="red", font=("Arial", 8), text=str(0))
            self.canvas1.tag_bind(self.weighing)
        else:
            self.flag_init = False
        

    def release(self, l): #l in needed by tkinter
        self.release_click = 0
        lis=[]
        lis.append(self.coords["x1"]);lis.append(self.coords["y1"]);lis.append(self.coords["x2"]);lis.append(self.coords["y2"])
        if self.coords["x1"] != self.coords["x2"] and self.coords["y1"] != self.coords["y2"] and self.flag_final:
            self.final.append(lis)
            node1 = None
            for i in range(len(self.graph)):
                if self.graph[i].coords[0] == self.coords["x1"] and self.graph[i].coords[1] == self.coords["y1"]:
                    node1 = mtxp.node(i, [self.coords["x1"], self.coords["y1"]])
                elif self.graph[i].coords[0] == self.coords["x2"] and self.graph[i].coords[1] == self.coords["y2"]:
                    node2 = mtxp.node(i, [self.coords["x2"], self.coords["y2"]])
            find = False
            if node1 is not None:
                for i in range(len(self.graph)):
                    if self.graph[i].name == node2.name:
                        find = True
                if not find:
                    #mtxp.arista(self.temp_weight, node1.coords[0], node1.coords[1], node2.coords[0], node2.coords[1], [node1, node2])
                    # self.graph[node1.name].append(node2)
                    # self.graph[node2.name].append(node1)
                    self.graph[node1.name].add_adj(node2)
                    self.graph[node2.name].add_adj(node1)
        elif self.flag_init: #TODO if line exists delete it
            self.canvas1.delete(self.line)
            self.canvas1.delete(self.weighing)

    def drag(self, e):
        self.coords["x2"] = e.x
        self.coords["y2"] = e.y
        # l = len(self.pos)
        l = len(self.graph)
        i = 0
        salir = False
        d = 100
        while l>0 and i < l and not salir and l>1:
            # d = self.dist(self.pos[i][0], self.pos[i][1], e.x, e.y)
            d = self.dist(self.graph[i].coords[0], self.graph[i].coords[1], e.x, e.y)
            if (d < 50):
                # self.coords["x2"]=self.pos[i][0]
                # self.coords["y2"]=self.pos[i][1]
                self.coords["x2"]=self.graph[i].coords[0]
                self.coords["y2"]=self.graph[i].coords[1]
                salir = True
                i = 0
                self.flag_final = True
            else:
                i = i+1
                self.flag_final = False
        if l>1 and self.flag_init:
            self.canvas1.coords(self.line, self.coords["x1"],self.coords["y1"],self.coords["x2"],self.coords["y2"])
            mid = self.midpoint(self.coords["x1"],self.coords["y1"],self.coords["x2"],self.coords["y2"])
            d = int(self.dist(self.coords["x1"],self.coords["y1"],self.coords["x2"],self.coords["y2"]))
            self.canvas1.coords(self.weighing, mid[0], mid[1])
            self.canvas1.itemconfig(self.weighing, text=str(d))
            self.temp_weight = d

system("cls")
app1 = App()
system("cls")
import os
import sys
import mtxp
import tkinter as tk
import math
from os import system

class App:
    def __init__(self):
        self.release_click = 0
        self.flag_init = False
        self.flag_final = False
        self.coords = {"x1":0,"y1":0,"x2":0,"y2":0} #line coords
        self.line = 0
        self.weighing = 0
        self.temp_weight= 0
        self.graph = []
        self.incremental_id = 0

        self.window = tk.Tk()

        self.menubar = tk.Menu(self.window)
        self.window.config(menu = self.menubar)

        self.actmenu = tk.Menu(self.menubar, tearoff=0)
        self.algmenu = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="Acciones", menu = self.actmenu)
        self.menubar.add_cascade(label="Algoritmos", menu = self.algmenu)

        self.actmenu.add_command(label="Borrar arista")

        self.algmenu.add_command(label="Ford Fulkerson")

        self.canvas1 = tk.Canvas(self.window, width=600, height=600, background='gainsboro')
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind('<Motion>', self.move_mouse)
        self.canvas1.bind('<Button-3>', self.click_mouse)
        self.canvas1.bind("<Double-1>", self.deleteNodeOrEdge)
        self.canvas1.bind("<ButtonPress-1>", self.click_line)
        self.canvas1.bind("<B1-Motion>", self.drag) 
        self.canvas1.bind('<ButtonRelease-1>', self.release)
        self.window.bind('<Key>', self.keys)  
        self.window.mainloop()

    
    def deleteNodeOrEdge(self, event): #tkinter ask for 2 arguements
        for i in range(len(self.graph)):
            if self.dist(event.x, event.y, self.graph[i].coords[0], self.graph[i].coords[1]) < 10:
                node_target = self.graph.pop(i)
                for g in node_target.edges:
                    #delete actual node edges
                    self.canvas1.delete(g["key_line"])
                    self.canvas1.delete(g["key_weight"])
                    #delete adjacent nodes and common edges
                    for adj in node_target.adjacents:
                        for j in range(len(adj["node"].edges)):
                            if adj["node"].edges[j] == g:
                                adj["node"].edges.pop(j)
                                break
                    for adj in node_target.adjacents:
                        for k in range(len(adj["node"].adjacents)):
                            if adj["node"].adjacents[k]["node"].key == node_target.key:
                                adj["node"].adjacents.pop(k)
                                break
                #delete node
                oval_target = node_target.canvas["key_oval"]
                text_target = node_target.canvas["key_text"]
                self.canvas1.delete(oval_target)
                self.canvas1.delete(text_target)
                break
        #TODO eliminar las aristas tamb en el else

    def pendient(self, x1, y1, x2, y2):
        if x1 == x2:
            return None
        return int(((y2-y1)/(x2-x1)))

    def dist(self, x1, y1, x2, y2):
        d = math.sqrt((abs(x2-x1)**2)+(abs(y2-y1)**2))
        return d

    def dist_point_rect(self):
        return 0
    
    def midpoint (self, x1, y1, x2, y2):
        return [(x1+x2)/2, (y1+y2)/2]

    def keys(self, envent):
        key = envent.char
        if key == 'i':
            system("cls")
            print("self")
            print("self.release_click: ", self.release_click)
            print("self.flag_init: ", self.flag_init)
            print("self.flag_final: ", self.flag_final)
            print("self.coords: ", self.coords)
            print("self.line: ", self.line)
            print("self.weighing: ", self.weighing)
            print("self.temp_weight: ", self.temp_weight)
            print("self.incremental_id: ", self.incremental_id)
            print("self.graph: ")
            mtxp.print_graph(self.graph)
            print(mtxp.graph_mtx_simplified(self.graph))
            #print(mtxp.graph_to_mtx(self.graph))
        elif key == 'c':
            self.canvas1.delete("all")
            self.release_click = 0
            self.flag_init = False
            self.flag_final = False
            self.coords = {"x1":0,"y1":0,"x2":0,"y2":0}
            self.line = 0
            self.weighing = 0
            self.temp_weight= 0
            self.incremental_id = 0
            self.graph = []
            system("cls")
        elif key == 'q':
            quit()
        elif key == 'r':
            os.execv(sys.executable, ['python'] + sys.argv)


    def move_mouse(self, envent):
        self.window.title(str(envent.x)+'-'+str(envent.y))
    
    def click_mouse(self, envent): #right click to create node
        l = self.incremental_id
        rg = True
        for i in range(len(self.graph)): #new node does not overlap any of the other created nodes
            if (self.dist(envent.x, envent.y, self.graph[i].coords[0], self.graph[i].coords[1])) < 50:
                rg = False
                break
        if rg:    
            node_canvas = self.canvas1.create_oval(envent.x-8, envent.y-8, envent.x+8, envent.y+8, fill = 'lightblue1', tag = str(l))
            text_canvas = self.canvas1.create_text(envent.x,envent.y, fill="black", font=("Arial", 8), text=str(l))
            var = [envent.x, envent.y]
            node = mtxp.node(self.incremental_id,{"key_oval": node_canvas, "key_text": text_canvas}, [], var, [])
            self.graph.append(node)
            self.incremental_id +=1
    
    def click_line(self, e): #left click to create line
        self.coords["x1"] = e.x
        self.coords["y1"] = e.y
        l = len(self.graph)
        i = 0
        salir = False
        while  i < l and not salir and l>1:
            d = self.dist(self.graph[i].coords[0], self.graph[i].coords[1], e.x, e.y)
            if (d < 50):
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
            node1 = None
            node2 = None
            for i in range(len(self.graph)): #search the adjacent nodes
                if self.graph[i].coords[0] == self.coords["x1"] and self.graph[i].coords[1] == self.coords["y1"]:
                    node1 = mtxp.node(self.graph[i].key, self.graph[i].canvas, self.graph[i].edges, [self.coords["x1"], self.coords["y1"]],self.graph[i].adjacents)
                elif self.graph[i].coords[0] == self.coords["x2"] and self.graph[i].coords[1] == self.coords["y2"]:
                    node2 = mtxp.node(self.graph[i].key, self.graph[i].canvas, self.graph[i].edges, [self.coords["x2"], self.coords["y2"]],self.graph[i].adjacents)
            find = False
            if node1 is not None:
                for i in range(len(self.graph)):
                    if node2 is not None:
                        if self.graph[i].key == node2.key:
                            find = True
                            break
                if find:
                    for node in self.graph:
                        if node.key == node1.key:
                            node.add_adj_node({"node": node2, "weight":self.temp_weight})
                            node.add_adj_edge({"key_line":self.line, "key_weight": self.weighing})
                        elif node.key == node2.key:
                            node.add_adj_node({"node":node1, "weight":self.temp_weight})
                            node.add_adj_edge({"key_line":self.line, "key_weight": self.weighing})
        elif self.flag_init: #TODO if line exists delete it
            self.canvas1.delete(self.line)
            self.canvas1.delete(self.weighing)

    def drag(self, e):
        self.coords["x2"] = e.x
        self.coords["y2"] = e.y
        l = len(self.graph)
        i = 0
        salir = False
        d = 100
        while l>0 and i < l and not salir and l>1:
            d = self.dist(self.graph[i].coords[0], self.graph[i].coords[1], e.x, e.y)
            if (d < 50):
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
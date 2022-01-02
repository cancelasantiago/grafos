import tkinter as tk

class App:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1, width=600, height=600, background='grey')
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind('<Motion>', self.mover_mouse)
        self.canvas1.bind('<Button-1>', self.click_mouse)
        self.ventana1.mainloop()

    def mover_mouse(self, evento):
        self.ventana1.title(str(evento.x)+'-'+str(evento.y))
    
    def click_mouse(self, evento):
        self.canvas1.create_oval(evento.x-5, evento.y-5, evento.x+5, evento.y+5, fill = 'blue')

app1 = App()
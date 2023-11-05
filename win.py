import tkinter as tk

class Win:
    def __init__(self,Name,Size) -> None:
        
        self.win=tk.Tk()
        self.win.title(Name)
        self.win.geometry(Size)
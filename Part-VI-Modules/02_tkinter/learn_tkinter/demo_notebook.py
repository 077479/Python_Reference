import tkinter as tk
from tkinter import ttk

class DemoNotebook:
    def __init__(self, parent):
        self.noteb = ttk.Notebook(parent)
        self.noteb.pack(fill="both", expand=True)
        self.items = dict()
    
    def tab_add(self, name):
        nb_tab_frame = ttk.Frame(self.noteb)
        self.noteb.add(nb_tab_frame, text=name, sticky="nsew")
        self.items[name] = nb_tab_frame
    
def create_demo_nb(parent):
    notebook = DemoNotebook(parent)
    notebook.tab_add(name="misc")
    notebook.tab_add(name="Text w/scroll")
    notebook.tab_add(name="Paned Window")
    notebook.tab_add(name="Treeview")
    notebook.tab_add(name="MenuButton")
    notebook.tab_add(name="Listbox")
    notebook.tab_add(name="inactive")
    
    notebook.noteb.tab(notebook.noteb.tabs()[6], state="disabled")

    return notebook
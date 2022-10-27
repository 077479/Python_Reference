import tkinter as tk
from tkinter import ttk

lorem = """
Lorem ipsum
dolor sit amet,
consetetur sadipscing
elitr,
sed diam nonumy
eirmod tempor
invidunt ut labore
et dolore
magna aliquyam
erat,
sed diam
voluptua.
At vero eos
et accusam et justo
duo dolores
et ea rebum.
Stet clita
kasd gubergren,
no sea takimata
sanctus est
Lorem ipsum
dolor sit amet.
Lorem ipsum
dolor sit amet,
consetetur sadipscing
elitr, sed diam
nonumy eirmod
tempor invidunt
ut labore
et dolore
magna aliquyam
erat,
sed diam voluptua.
At vero eos et accusam et
justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea
takimata sanctus est Lorem ipsum
dolor sit amet.
"""

def create_text(parent):
    scroller = ttk.Scrollbar(parent)
    scroller.pack(side="right", fill="y")

    text_widget = tk.Text(parent, font=("times", 14), yscrollcommand=scroller.set)
    text_widget.pack(fill="both", expand=True, side="left")

    text_widget.insert(index=tk.INSERT, chars=lorem)

    scroller.configure(command=text_widget.yview)

def create_paned(parent):
    paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
    paned.add(tk.Frame(paned, background="#3a6"), weight=1)
    fr = tk.Frame(paned)
    paned.add(fr, weight=1)
    paned_fr = ttk.PanedWindow(fr, orient=tk.VERTICAL)
    paned_fr.pack(fill="both", expand=True)
    paned_fr.add(tk.Frame(paned, background="#836"), weight=1)
    paned_fr.add(tk.Frame(paned, background="#347"), weight=1)
    paned.pack(fill="both", expand=True)

def create_treeview(parent):
    tree = ttk.Treeview(parent, columns=("#1", "#2", "#3"), displaycolumns="#all")
    tree.pack(fill="both", expand=True)

    tree.heading("#0", text="this")
    tree.heading("#1", text="is a")
    tree.heading("#2", text="treeview")
    tree.column("#3", width=20)

    tree.insert(parent="", index=tk.END, iid="ToDo", text="ToDo")
    tree.insert(parent="ToDo", index=tk.END, iid="vacate", text="vacate")
    tree.insert(parent="ToDo", index=tk.END, iid="go for a walk", text="walk")
    tree.insert(parent="", index=tk.END, iid="Cook", text="Cook")
    tree.insert(parent="Cook", index=tk.END, iid="Meal_1", text="Salad")
    tree.insert(parent="Cook", index=tk.END, iid="Meal_2", text="Pizza")

def create_menubtn(parent):
    frame = tk.Frame(parent, background="white")
    frame.pack(fill="both", expand=True)

    def set_clr():
        frame.configure(background=color_var.get())
    mnbtn = ttk.Menubutton(frame, text="select a color")
    colors = (("blue", "#226688"), ("yellow", "#b9a922"), ("red", "#663344"), ("white", "#999999"), ("black", "#333333"))
    menu = tk.Menu(mnbtn, tearoff=0)
    color_var = tk.StringVar(value="white")
    for color in colors:
        menu.add_radiobutton(label=color[0], value=color[1], variable=color_var, command=set_clr)
    mnbtn["menu"] = menu
    mnbtn.pack(anchor=tk.CENTER)

def create_listbox(parent):
    lb = tk.Listbox(parent, activestyle="underline", font=("times", 14), selectmode=tk.MULTIPLE)
    for i in range(12):
        lb.insert(i, f"line: {i}")
    lb.pack(fill="both", expand=True)
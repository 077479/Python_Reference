import tkinter as tk

class Menubar:
    def __init__(self, parent:tk.Tk):
        self.menubar = tk.Menu(parent, tearoff=False)
        parent.config(menu=self.menubar)
        self.items = dict()

    def customize(self):
        pass
    
    def cascade_add(self, parent=None, name=""):
        if not parent: parent = self.menubar
        cascade = tk.Menu(parent)
        parent.add_cascade(label=name, menu=cascade)
        self.items[name] = cascade
    
    def command_add(self, parent=None, name="", var=None, fct=None):
        if not parent: parent = self.menubar
        parent.add_command(label=name, command=fct)

    def radiobutton_add(self, parent=None, name="", var=None, fct=None):
        if not parent: parent = self.menubar
        parent.add_radiobutton(label=name, value=name, variable=var, command=fct)
    
    def checkbutton_add(self, parent=None, name="", var=None, fct=None):
        if not parent: parent = self.menubar
        parent.add_checkbutton(label=name, value=name, variable=var, command=fct)

def create_menu(parent, exit_program, theme_ctl, theme_handler):
    menubar = Menubar(parent)
    menubar.command_add(parent=menubar.menubar, name="exit", fct=exit_program)
    menubar.cascade_add(parent=menubar.menubar, name="theme")
    menubar.radiobutton_add(parent=menubar.items["theme"], name="breeze", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="breeze-dark", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="awdark", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="default", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="clam", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="azure-dark", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="azure-light", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="sun-valley-light", var=theme_ctl, fct=theme_handler)
    menubar.radiobutton_add(parent=menubar.items["theme"], name="sun-valley-dark", var=theme_ctl, fct=theme_handler)

    return menubar
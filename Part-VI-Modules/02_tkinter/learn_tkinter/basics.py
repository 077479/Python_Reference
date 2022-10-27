import tkinter as tk
from tkinter import ttk
import sys, pathlib, subprocess

import demo_menu, demo_notebook, demo_misc, demo_tabs
"""
menu
notebook
    text w/scroll
    paned window
    treeview
    menubutton
    listbox
    inactive

"""

def exit_program():
    subprocess.run("clear", shell=True)
    sys.exit(0)

def set_themes(parent):
    theme_file_dark = pathlib.Path(__file__).parent / "themes/breeze-dark/breeze-dark.tcl"
    theme_file_light = pathlib.Path(__file__).parent / "themes/breeze/breeze.tcl"

    parent.tk.call("source", theme_file_dark)
    parent.tk.call("source", theme_file_light)

def theme_handler():
    ttk.Style().theme_use(theme_ctl.get())    
    ttk.Style().configure(".", font=("times", 14))

    bg = ttk.Style().lookup(f"TLabel.border", "background")
    fg = ttk.Style().lookup(f"TLabel.border", "foreground")

    tk_customization(arg_bg=bg, arg_fg=fg)
    parent.configure(background=bg)
    parent.title(f"theme-example {theme_ctl.get()}")

def create_menu():        
    return demo_menu.create_menu(parent, exit_program, theme_ctl, theme_handler)

def create_nb():
    return demo_notebook.create_demo_nb(parent)

def create_misc():
    demo_misc.left_side(notebook)
    demo_misc.right_side(notebook)

def create_tabs():
    demo_tabs.create_text(notebook.items["Text w/scroll"])
    demo_tabs.create_paned(notebook.items["Paned Window"])
    demo_tabs.create_treeview(notebook.items["Treeview"])
    demo_tabs.create_listbox(notebook.items["Listbox"])
    demo_tabs.create_menubtn(notebook.items["MenuButton"])

def tk_customization(arg_bg, arg_fg):
    """
    the * will set the option globally
    better is it to specify the specfic widgets with:
        "Label.Font", "times 14"
    """
    # parent.option_readfile(fileName, priority=None)

    parent.option_clear()

    parent.option_add("*Font", "times 14")
    parent.option_add("*background", arg_bg)
    parent.option_add("*foreground", arg_fg)

if __name__ == "__main__":
    parent = tk.Tk()
    parent.title("theme-example")
    
    theme_ctl = tk.StringVar(value="breeze-dark")
    set_themes(parent)
    theme_handler()

    menubar = create_menu()
    notebook =create_nb()
    create_misc()
    create_tabs()

    parent.mainloop()

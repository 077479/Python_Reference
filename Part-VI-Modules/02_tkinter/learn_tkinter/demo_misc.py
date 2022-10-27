import tkinter as tk
from tkinter import ttk

def grid_it(ui_element, arg_row, arg_col):
        ui_element.grid(row=arg_row, column=arg_col, padx=5, pady=5, sticky="nswe")

def left_side(notebook):
    parent = notebook.items["misc"]
    frame_left = ttk.LabelFrame(parent, relief="groove", text="Misc Active")
    frame_left.pack(fill="both", expand=True, side="left", padx=5, pady=5, ipadx=10, ipady=10)

    lbl_active = ttk.Label(frame_left, text="label with text", font=("times", 14))
    grid_it(lbl_active, 0, 0)

    btn_active = ttk.Button(frame_left, text="Button")
    grid_it(btn_active, 0, 1)

    menu_btn_active_1 = ttk.Menubutton(frame_left, text="Menubutton")
    grid_it(menu_btn_active_1, 1, 0)
    menu_btn_active_2 = ttk.Menubutton(frame_left, text="Menubutton")
    grid_it(menu_btn_active_2, 1, 1)

    ch_btn_ctl = tk.IntVar(value=0) 
    ch_btn = ttk.Checkbutton(frame_left, text="on", variable=ch_btn_ctl, onvalue=1, offvalue=0)
    grid_it(ch_btn, 2, 0)
    ch_btn = ttk.Checkbutton(frame_left, text="off", variable=ch_btn_ctl, onvalue=0, offvalue=1)
    grid_it(ch_btn, 2, 1)

    sep = ttk.Separator(frame_left)
    sep.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nswe")

    rbtn_ctl = tk.IntVar(value=0)
    rbtn_1 = ttk.Radiobutton(frame_left,text="on", variable=rbtn_ctl, value=1)
    grid_it(rbtn_1, 4, 0)
    rbtn_2 = ttk.Radiobutton(frame_left,text="off", variable=rbtn_ctl, value=0)
    grid_it(rbtn_2, 4, 1)


    scale_lbl_active = ttk.Label(frame_left, text="bound to scale")
    def scale_ctl_fct(var):
        if len(var) > 3: int_var = int(var[2])*10 + int(var[3])
        else: int_var = int(var[0])*100
        scale_lbl_active["text"] = int_var
    scale_active = ttk.Scale(frame_left, orient=tk.HORIZONTAL, command=scale_ctl_fct)
    grid_it(scale_active, 5, 0)
    grid_it(scale_lbl_active, 5, 1)

    entry_lbl = ttk.Label(frame_left, text="bound to entry")
    def entry_ctl_fct(event):
        entry_lbl["text"] = event.widget.get()
    entry_active = ttk.Entry(frame_left, font=("times", 14))
    entry_active.insert(0, "entry field")
    entry_active.bind("<KeyPress-Return>", entry_ctl_fct)
    
    grid_it(entry_active, 6, 0)
    grid_it(entry_lbl, 6, 1)

    spin_active = ttk.Spinbox(frame_left, from_=0, to=100)
    spin_active.insert(0, 0)
    grid_it(spin_active, 7, 0)

def right_side(notebook):
    parent = notebook.items["misc"]

    frame_right = ttk.LabelFrame(parent, relief="groove", text="Misc Disabled")
    frame_right.pack(fill="both", expand=True, side="left", padx=5, pady=5, ipadx=10, ipady=10)
    frame_right.state(["disabled"])

    lbl_passive = ttk.Label(frame_right, text="label with text", font=("times", 14))
    grid_it(lbl_passive, 0, 0)

    btn_passive = ttk.Button(frame_right, text="Button")
    grid_it(btn_passive, 0, 1)

    menu_btn_passive_1 = ttk.Menubutton(frame_right, text="Menubutton")
    grid_it(menu_btn_passive_1, 1, 0)
    menu_btn_passive_2 = ttk.Menubutton(frame_right, text="Menubutton")
    grid_it(menu_btn_passive_2, 1, 1)

    ch_btn_ctl = tk.IntVar(value=0) 
    ch_btn = ttk.Checkbutton(frame_right, text="on", variable=ch_btn_ctl, onvalue=1, offvalue=0)
    grid_it(ch_btn, 2, 0)
    ch_btn = ttk.Checkbutton(frame_right, text="off", variable=ch_btn_ctl, onvalue=0, offvalue=1)
    grid_it(ch_btn, 2, 1)

    sep = ttk.Separator(frame_right)
    sep.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nswe")

    rbtn_ctl = tk.IntVar(value=0)
    rbtn_1 = ttk.Radiobutton(frame_right,text="on", variable=rbtn_ctl, value=1)
    grid_it(rbtn_1, 4, 0)
    rbtn_2 = ttk.Radiobutton(frame_right,text="off", variable=rbtn_ctl, value=0)
    grid_it(rbtn_2, 4, 1)

    scale_lbl_passive = ttk.Label(frame_right, text="bound to scale")
    def scale_ctl_fct(var):
        if len(var) > 3: int_var = int(var[2])*10 + int(var[3])
        else: int_var = int(var[0])*100
        scale_lbl_passive["text"] = int_var
    scale_passive = ttk.Scale(frame_right, orient=tk.HORIZONTAL, command=scale_ctl_fct)
    grid_it(scale_passive, 5, 0)
    grid_it(scale_lbl_passive, 5, 1)

    
    entry_lbl = ttk.Label(frame_right, text="bound to entry")
    def entry_ctl_fct(event):
        entry_lbl["text"] = event.widget.get()
    entry_passive = ttk.Entry(frame_right, font=("times", 14))
    entry_passive.insert(0, "entry field")
    entry_passive.bind("<KeyPress-Return>", entry_ctl_fct)
    
    grid_it(entry_passive, 6, 0)
    grid_it(entry_lbl, 6, 1)

    spin_passive = ttk.Spinbox(frame_right, from_=0, to=100)
    spin_passive.insert(0, 0)
    grid_it(spin_passive, 7, 0)

    for i in frame_right.children.items():
        i[1].state(["disabled"])
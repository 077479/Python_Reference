# Basics
- link to a doc: [link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)
- the tkinter functionality is spread across different modules
- tkinter uses "*windows*" as containers to pack "*widgets*" with functionality in it

## Tk
- tk returns a top level widget that normally represents the main window
- `tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)`
    - **screenName**: sets the DISPLAY env var (x11 only)
    - **baseName**: profile file
    - **className**: name of the widget class 
    - **useTk**: initializes the tk subsystem
    - **sync**: if True executes x-server commands simultanious
    - **use**: specifies the id of the window to an application
- **Attributes**
    - tk: tk application object provides access to the tcl interpreter
    - master: returns the widget object that contains the widget (for tk its None)
    - children: descendants of the widget as dict

## Tcl
- factory function that creates a window object without initializing the Tk subsystem
- `tkinter.Tcl(screenName=None, baseName=None, className="Tk", useTk=False)`

## tkinter.ttk
- thmed widget set, modern alternatives for classic widgets
- link to list of widgets: [link](https://docs.python.org/3/library/tkinter.ttk.html)



# Concept
## Widget
- a ui is made up of individual widgets(the ui elements)
- widgets are represented as python object

## Widget Hierarchy
- widgets are packed into container widgets
- this forms a native hierarchy e.g. root_window => frame => button
- the first element given to the init of a widget is the parent
- the attribute "*master*" refers to the parent object

## Configuration
- the appearance of widgets can be changed through "*configuration options*" or for ttk widgets "*styles*"
- configuration options can be passed at creation
    - `btn = tkinter.Button(text="Button", fg="red", bg="blue")`
- the options are stored in a dict so after creation it can be manipulated
    - `btn["fg"] = "blue"`
the config method is an alternative for the dict
    - `btn.config(fg="green")`

## Placement
- widgets arent automatically added to a window
- a "*gemetry manager*" has to be used to place them
- e.g grid

## Packer
- the packer is the way tkinter calculates the positioning of an widget within the parent
- the size of the master widget is determined by the size of the child widget
- a widget will only appear afte rthe packer was called from it
- `btn.pack()`
- **Options**
    - anchor: where the child is placed in its parcel
    - expand:
    - ipadx / ipady: internal padding on each side
    - padx / pady: external padding on each side
    - fill: fills the parent with the widget, accepts: "x", "y", "both", "none"
    - side: alignment within the cell, accepts: "left", "right", "top", "bottom"

## Events
- a tkinter app relys on an event loop (ticks and looks for input or other events)
- the loop has to be started with `widget.mainloop()`

## Varaible Coupling
- some widgets can be directly conneted to the application
- the connection works both ways (changes on one will change the other)
- arbitrary vars cant be passed to a widget
- a special tkinter variable has to be used like StringVar
    - the special variabless have set() and get()
```python
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
```

## Window Manager
- tkinter provides an interface to the window manager to change things like title or placement
- in tkinter the window manager is implemented as WM class
- the window manager is passed as master to the top level widget (main window)



# Configuration Options
- **anchor**: [n, ne, e, se, s, sw, w, nw, center] alignment within the cell
- **bitmap**: 
- **boolean**: integers 0,1 or "yes","no" can be passed
- **callbacks**: `btn["command"] = function_call` a callback to a function without arguments (through lambda arguments would go)
- **color**: as rgb => 4Bit: #RGB, 8Bit: #RRGGBB
- **cursor**: cursor image
- **distance**: screen distance
- **font**: font (tkinter.font.NORMAL / BOLD / ITALIC / ROMAN)
- **geometry**: str in form "widthxheight" the width and height of the widget e.g. `btn["geometry"] = "200x100"`
- **justify**: "left", "right", "center", "fill"
- **relief**: the border style, accepts: "raised", "sunken", "flat", "groove", "ridge"



# Bindings Events
- the bind method binds a widget to an event and binds the event to a callback function
- e.g. `def bind(self, sequence, func, add="")`
    - sequence: string that denotes the event
    - func: the function call without the bracket (means no arguments)
    - add: an empty string specifies that all other bindings for the event are replaced with this a plus adds the binding to the list of bounds for the event
- the first element given to the function is the event itself
```python
def turn_red(self, event):
    event.widget["activeforeground"] = "red"
```
## event attributes
- focus
- height
- keycode
- state
- time
- width
- x
- y
- char
- send_event
- keysum
- keysum_num
- type
- widget
- x_root
- y_root



# Images
- tkinter.Image provides the functionality to display image in widgets that allow that (label)
- tkinter.Image accepts: XBM, PGM, PPM, GIF, PNG
- tkinter does not provide a reference to the image => means if the last reference to the image is gone an empty box will be displayed



# Widgets
## common attributes
- `master`: the parent widget
- `_root`: the top level widget (main window)

## basics
- link to tkinter widgets: [link](https://coderslegacy.com/python/list-of-tkinter-widgets/)
- link to the new widgets doc: [link](https://tkdocs.com/tutorial/morewidgets.html)

### Tkinter
- Frame
- Button
- Label
- Entry
- Radio Button
- Check Button
- Combobox
- Menu Button
- Toplevel
- Scrollbar
- Menu
- List Box
- Text Widget
- Canvas
- Scale
- LabelFram
- SpinBox
- Color Chooser
- Photoimage
- ImageTk
- OptionMenu

### TTK
- ComboBox
- ProgressBar
- Notebook
- Treeview
- Sizegrip
- Separator
- Button
- Checkbutton
- Entry
- Frame
- Label
- LabelFrame
- Menubutton
- PanedWindow
- Radiobutton
- Scale
- Scrollbar
- Spinbox



# TTK Styles
## Basics
- instead of configuration options ttk widgets are using "*styles*"
- styles are defined by the (global) style object
- the specific styles then are classes that define the appearance of a widget
- the built-in styles vary from os to os
    - windows styles: 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'

## list of styles-classes for Widgets
>
    Widget          Style Class
    ------          -----------
    Button	        TButton
    Checkbutton	    TCheckbutton
    Combobox	    TCombobox
    Entry	        TEntry
    Frame	        TFrame
    Label	        TLabel
    LabelFrame	    TLabelFrame
    Menubutton	    TMenubutton
    Notebook	    TNotebook
    PanedWindow	    TPanedwindow 
    Progressbar	    Horizontal.TProgressbar / Vertical.TProgressbar
    Radiobutton	    TRadiobutton
    Scale	        Horizontal.TScale / Vertical.TScale
    Scrollbar	    Horizontal.TScrollbar / Vertical.TScrollbar
    Separator	    TSeparator
    Sizegrip	    TSizegrip
    Treeview	    Treeview

## Custom Styles
- the naming convention for custom styles is `[CustomName].[BaseStyleClass]` e.g. `Custom.TButton`
- example:
```python
import tkinter
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Fram(self.master)

        style = ttk.Style()
        style.configure("Custom.TButton",
                        foreground="black",
                        background"white",
                        padding=[10,10,10,10],
                        font="Verdana 12 underline")
        
        button = ttk.Button(frame, text="click me", style="Custom.TButton")
        button.pack()

        frame.pack(padx=5, pady=5)

if __name__ == "__main__":
    main = tkinter.Tk()
    main.geometry(200,200)
    window = Window(main)
    main.mainloop()
```

## Style Configuration
### theme_use()
- to get the by a widget used style use the `theme_use()` method of the widget
- e.g. `print(button.theme_use())`

### lookup()
- the value of an attribute of a style class can be accessed with the `lookup()` of a style class
- e.g. `print(custom_button_style.lookup("Custom.TButton", "foreground"))`

### configure()
- styles can be configured by the `configure()` method of a style
- e.g. `custom_button_style.configure("foreground")`

## theme_settings()
- `style.theme_settings([style], [dict of tyleclass // which is also a dict])`
- widget states: active: cursor hovering, focus: selected (clicked), !disabled: anything but disabled
- e.g.
```python
style = ttk.style()
style.theme_settings("default", {
                    "Custom.TButton": {
                        "configure": {"padding":10},
                        "map": {
                            "background": [("active", "yellow"),
                                            ("!disabled", "red")],
                            "foreground": [("focus", "blue"),
                                            ("active", "green")]
                        }}})
```

## theme_create()
- to create a new them the method `style.theme_create()` is used
- 

## theme_use()
- to change the active theme use the `style.theme_use([style])`





reference to tkinter manual, new widget classes should inherit from tk.Frame
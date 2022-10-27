# Basics
- link to the ttk doc: [link](https://docs.python.org/3/library/tkinter.ttk.html)
- the ttk module offers much of the original tkiniter widgets with a new fresh look
- the customization for ttk widgets works with styles
- every widget has a number of different states
- a style map can specify certain options

# Definitions
- **theme**: complete look and feel appearance of all widgets
- **style**: description of the appearance of one class of widgets

# Import
- ttk has to imported
- it is common to import tkinter as "*tk*" and "*ttk*"
- `import tkinter as tk`, and `from tkinter import ttk`

# Common TTK Methods
- all ttk widgets share a set of methods
- `cget(option)`: returns the value of an option
- `configure()`: sets widget options
    - name: The option name.
    - dbName: 	The database name of the option.
    - dbClass: The database class of the option.
    - default: The default value of the option.
    - current: The current value of the option. 
- `identify(x,y)`: returns the element on the location
- `instate(stateSpec, callback=None, *args, **k)`: determines if the widget is in the given state, possible to make callbacks
- `state(stateSpec=None)`: sets the widget into given state, if None clears teh current state

# States
- active: The mouse cursor is over the widget and pressing a mouse button will cause some action to occur
- disabled: Widget is disabled under program control
- focus: Widget has keyboard focus
- pressed: Widget is being pressed
- selected: “On”, “true”, or “current” for things like Checkbuttons and radiobuttons
- background: Windows and Mac have a notion of an “active” or foreground window. The background state is set for widgets in a background window, and cleared for those in the foreground window
- readonly: Widget should not allow user modification
- alternate: A widget-specific alternate display format
- invalid: The widget’s value is invalid

# Style
- each ttk.widget has a corresponding style-class
- the style class defines the appearance of the widget-class
- the manipulation of ttk-styles require a `ttk.Style()` object
- the style object can manipulate the style database

# Widget-Style-Classes
- ttk.Widget        Style name
- ttk.Button        TButton
- ttk.Checkbutton   TCheckbutton
- ttk.Combobox      TCombobox
- ttk.Entry         TEntry
- ttk.Frame         TFrame
- ttk.Label         TLabel
- ttk.LabelFrame    TLabelFrame
- ttk.Menubutton    TMenubutton
- ttk.Notebook      TNotebook
- ttk.PanedWindow   TPanedwindow (not TPanedWindow!)
- ttk.Progressbar   Horizontal.TProgressbar or Vertical.TProgressbar, depending on the orient option.
- ttk.Radiobutton   TRadiobutton
- ttk.Scale         Horizontal.TScale or Vertical.TScale, depending on the orient option.
- ttk.Scrollbar     Horizontal.TScrollbar or Vertical.TScrollbar, depending on the orient option.
- ttk.Separator     TSeparator
- ttk.Sizegrip      TSizegrip
- ttk.Treeview      Treeview

# Style Configuration
- styles can be configured with the `ttk.Style().cofigure(["Style-Class"], [option="Value"]) method
- if a style-class is altered all corresponding widgets will be changed
- styles can be hierarchically customized
    - i.e. a style-class can be copied and changed and passed as subclass of the corresponding style to a corresponding widget
    - e.g. `ttk.Style().configure("Custom.TButton", foreground="#00ff55")` and for the button `btn = ttk.Button(style="Custom.Button")`
    - the btn will have the customization but all other buttons will use the default style
- the style hierarchy works the following:
    1. ttk searches for an option in the most specific style => "*CustomButton*"
    2. if the option isnt found (because it wasnt set there) it searches in the next style one up the ladder => "*TButton*"
    3. if there not found it searches the application default style
- the style `ttk.Style().configure(".")` refers to the global application style

# TTK Element Layer
- each style is composed of components (at least one) called "*Element Layer*"
- for example the style of a ttk.Button has 4 elements
    1. Border: around the outside
    2. Focus-Element: to that is the button changed when it gets focus
    3. Padding-Element: to set teh padding for the text of the button
    4. Button-Label: the text or image
- to retreive a style layout use the `ttk.Style().layout([style-class])` method
- to retreive the aviable options of an element use the `ttk.Style().element_options([style-class.element])` method
- to get the current value of an elements option: `ttk.Style().lookup([style-class.element], [option])`
- e.g.
```python
import tkinter as tk
from tkinter import ttk
print(ttk.Style().layout("TButton"))
# [('Button.border', {'sticky': 'nswe', 'border': '1', 'children': [( 'Button.focus', {'sticky': 'nswe', 'children': [('Button.padding', {'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nswe'})]})]})]})]

print(ttk.Style().element_option("TButton.border"))
# ("background", "borderwith", "relief")

print(ttk.Style().lookup("TButton.border", "background"))
# "#d9d9d9"
```

# State Mapping
- within the styles different appearances for different states can be specified
- the map attribute "*maps*" an option to the state
- e.g.
```python
import tkinter as tk
from tkinter import ttk

ttk.Style().configure("Custom.TButton",
    background = "#000000",
    foreground = "#ffffff",
    font = ("Times", 18, "bold"))

ttk.Style().map("Custom.TButton",
    foreground= [
        ("disabled", "#888888"),
        ("pressed", "#ee5555"),
        ("active", "#00ffff")],
    background= [
        ("disabled", "#000000"),
        ("pressed", "#ffff00"),
        ("active", "#ffffff")],
    relief= [
        ("pressed", "groove"),
        ("!pressed", "ridge")]) # when not in state pressed
```
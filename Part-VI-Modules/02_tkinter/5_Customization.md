# Basics
- to get a better customization access to the tkinter widgets it is common to use a "*option database*"
- the option-db is a file hat specifies preferences
- after the file is loaded the options are added to the option-pool and can be set to the default
- the options-db should specify general patterns describing which widget to configure

# Methods
- `widget.option_add(pattern, value, priority=None)`:
    - pattern: `"*Widget Class*option"`
    - value: the value of the option
    - priority: higher level priorities take precedence over lower-level ones
        - 20: global properties
        - 40: default for specific applications
        - 60: options from user files
        - 80: set after application start
    - e.g.
    ```python
    self.bigFont = tkFont.Font(family="times", size=24, weight="bold")
    self.option_add("*Button)*font", self.bigFont)
    ```
- `widget.option_clear()`: removes all customization
- `widget.get(name, classname)`: returns the value of an option of the widget-class
- `widget.option_readfile(filename, priority)`:
    - sets a user preference file, after loading adds the option to the pool

# Pattern
- the pattern operate on the name of the widgets
- tkinter provides two naming schemes for widgets
## class name
- the name of the widget group is determined by the class name e.g. `tk.Button` so the name of the button class is `"Button"`

## instance name
- the default instance name of a widget is an integer representing a unique identity
- this name can be altered to create "*naming groups*"
- the options of theese "*naming groups*" can be customized
- for standart tk.Widget the `name` attribute can be altered
- e.g. `btn = tk.Button(main_wwindow, name="SpecialNameButton", text="SpecialButton")`
- when inheriting (suggested by the tkinter creators when creating a custom widget) the `class_` attribute is the way to customize the instance name
- e.g.
```python
# with inheriting from frame
class CustomWidget(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master, class_="CustomWidget")
        self.__createWidgets()

# without inheriting from frame
class CustomWidget:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, class_="CustomWidget")

        ...

        self.frame.grid() / self.fram.pack() ...
```

# Option File
## Lines
- each line represents the value of one or more options in one or more applications
    1. `app option-pattern: value`: sets only the options when application name matches "*app*"
    2. `option-pattern: value`: sets option for all applications
    - eg. `xparrot*background: "#bf8"` sets all backgrounds to the color if the name of the application is "*xparrot*"
    - **option-patter**:
        - e.g. `*Listbox.font: times 24`
        - the "*" means apllying to all listboxes
        - the "." accesses the option
        - `*font: times 24` would mean to all widgets
        - `.` means strict binding => only the specified element
        - `*` means loose binding => to all of the category
- the option hierarchy is from specific to general (instance name options are more specific)
- i.e. when several aviable the more specific option will be used
- i.e. a specific button option will be used even when a general button option is aviable
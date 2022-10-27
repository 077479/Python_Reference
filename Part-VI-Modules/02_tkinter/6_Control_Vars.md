# Basics
- to connect the logic with the ui-elements there are different approaches
- some widgets have a command attribute that allows a link between a callabla object and an event bound to the widget
- e.g. `tk.Button(text="Button1", command=function_call)`
- but this works only if the mouse-coursor is wihtin the button and clicks with the left mouse button
- a general approach are "*command handlers*" they allow more flexability
- often is is required to use "*control varialbles*" => objects that provide an interface to the ui-elements for the buisness logic

# Control Variables
- tkinter control variables are special objects that are acting like standart datatypes like int or str
- but they can be shared among widgets
- i.e. if a stored value ("var") is stored in a "*tkinter control variable*" ("cont_var") with `cont_var.set(var)`
- any widget linked to this control variable can access it
- list of control var:
    - `tk.BooleanVar`
    - `tk.StringVar`
    - `tk.IntVar`

## Control Var Methods
- `control_var.get()`: returns the value
- `control_var.set(value)`: sets the value
> if a control var changes all linked widgets will update in the next idle of the mainloop

# Focus
## Tkinter Widgets
- tkinter calls to have the keyboard input directed to a widget this widget has the focus
- focus traversal is the list of widgets that the "*tab*" key will switch to
- the list is ordered by creation date of a widget (the first created element is first traversed to)
    - `takefocus=[1 or 0]` option can in/exclude widgets from the focus
- widgets have an "*focus highlight*" option that shows which widget has the focus
    - its just an outline that can be specified
    - `highlightthickness`: specifies the weigth of the highlight
    - `highlightcolor` specifies the color of the highlight

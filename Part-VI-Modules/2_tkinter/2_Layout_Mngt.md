# Basics
- to manage to display ui-elements in a window it has to be placed
- in tkinter the manamger of the placing of ui-elements in a window is called "*Geometry-Manager*"
- tkinter provides different "*gemetry manager*"
- all widgets come with the different "*geometry-manager*" registering methods
- at creation a widget needs the "parent" ui-element as argument
- then the registering method calls the parent "*geometry-manager*"
> any ui-element that is not registered by the layout-manager wont be displayed!

# grid
## Basics
- the grid "*geometry manager*" seperates a window into different cells specified by columns and rows 
- **width**: the width of each cell is determined by the cell with the widest ui-element
- **height**: the heigt of each cell is determined by the cell with the heighest ui-element
- if a widget doesnt fill a cell, tkinter either align the ui as by the dev specified, or stretches the widget
- different cells can be combined into larger

## Attributes
>
    Attribute   Description 
    column      the column of the cell the widget will be placed in, counting from 0 
    columspan   defines teh amount of columns the widget will be spanned over 
    row         the row of the cell in which the widget will be placed in, counting from 0 
    rowspan     defines the amount of row the widget will be spanned over 
    in_         registers a widget a child of given element 
    ipadx       cell internal x padding 
    ipady       cell internal y padding 
    padx        cell external x padding 
    pady        cell external y padding 
    stickey     specifies how to behave if the space of a cell is not filled 


- stickey accepts compass directions in order to align widgets
    - e.g. `btn.grid(stickey="NE")` will align the btn widget to the top-right corner
    - tk.N: Top
    - tk.NE: Top-Right
    - tk.E: Right
    - tk.SE: Bottom-Right
    - tk.S: Bottom
    - tk.SW: Bottom-Left
    - tk.W: Left
    - tk.NW: Top-Left
    - tk.CENTER: centers the widget in the cell
    - the directions can concatenated: .grid(stickey=tk.N+tk.S) stretches the widget vertically but leave it horizontally centered
    - the directions can concatenated: .grid(stickey=tk.E+tk.W) stretches the widget horizontally but leave it vertically centered
- if "*stiky*" is not provided the default behavior is "*center*"

## Methods
### Child Methods
- `widget.grid()`: registeres the widget to the "*geometry-manager*" of the parent
- `widget.grid_forget()`: makes the widget dissappear, it still exists but it wont be displayed (can be reversed with `grid()`)
- `widget.grid_info()`: returns a dictionary with options
- `widget.grid_location(x,y)`: returns a tuple (col, row) representing the cell for the given screen position (relative to parent)
- `widget.grid_propagate(n)`: forces the widget into a given size "*n*"
- `widget.grid_remove()`: like `forget` but the grid attributes are remembered when added again with `grid()`
- `widget.grid_size()`: returns a tuple (cols, rows) representing the size (related to cells) of the widget
- `widget.grid_slaves(row=Nonw, column=None)`: returns all child widgets, if no args given all

### Parent Methods
- `parent_widget.columnconfigure(N, option=value...)`: specify an option for column N
- `parent_widget.rowconfigure(N, option=value...)`: specify an option for row N
- Options:
    - minsize: minimum size in pixel
    - pad: padding over and above the largest cell
    - weight: makes a colum/row stretchable, value gives relative weight
        - e.g. `parent_widget.columnconfigure(0, weight=3); parent_widget.columnconfigure(0, weight=1)`
        - the first column will get 3/4 of thee aviable space and the second column will get 1/4 of the aviable size

## Resizing
- to controle the behavior by resizing events
- with the methods weight method the behavior for the cells for resize events can be customized
- e.g. `child_widget.grid(sticky=tk.N+tk.S+tk.E+tk.W)`
- to customize the behavior of the widgets within the cells the stickey optios are needed to streatch teh widgets accordingly to the resize event
- e.g. `parent_widget.widget.grid(sticky=tk.N+tk.S+tk.E+tk.W)`
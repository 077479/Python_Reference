# Reference
- link to a reference: [link](- https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)

# List Tkinter Widgets
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

# List Ttk Widgets
- link to a ttk_widget reference: [link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-widget-set.html)
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

# Universal Widget Methods
- reference for universal: [link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html)
- the here listet represents only a selection of universal widget methods
- `widget.bind(sequence, func, add)`: binds an event to a widget
- `widget.unbind(sequence, funcid=None)`: removes bindings for the event
- `widget.unbind_all(sequence)`: removes all bindings for an event application wide
- `widget.cget(["option"])`: returns the value of the option
- `widget.configure(option=value)`: sets configure options for the widget
- `widget.destroy()`: removes the widget and all children permanently
- `widget.focus_displayof()`: returns the window with the input focus on the same display, if not on the same display None
- `widget.focus_force()`: forces the input focus to the widget
- `widget.focus_get()`: returns the widget that has the input focus in the application, if not None
- `widget.focus_set()`: next time the application gets input focus the given widget will get the focus
- `widget.keys()`: returns all options for the widget as string
- `widget.lift(aboveThis=None)`: brings the parent widget to the front
- `widget.lower(belowThis=None)`: brings the parent widget to the background
- `widget.mainloop()`: starts the mainloop of tcl
- `widget.quit()`: stops the mainloop
> without the mainloop the application is just a static dummy
- `widget.selection_get()`: returns in the widget selected text // raises tk.TclError
- `widget.selection_clear()`: remoevs selection of text within widget
- `widget.update()`: forces the updating of the display, !BE AWARE CAN BREAK THE LOOP!
- `widget.wait_variable(v)`: suspends a widget til the variable *v* is set so it does not block the entire application
- `widget.winfo_children()`: returns a list of all children reverse sorted by their stacking order
- `widget.winfo_id()`:return the unique id (as int) of the widget
- `widget.winfo_parent()`: returns the parent of the widget (if toplevel empty str)
- `widget.winfo_pointerxy()`: returns a tuple with the mouse coords relative to the top-level-window, if not on display (-1, -1)
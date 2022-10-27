# Basics
- Tkinter is a GUI widget set for python
- tkinter reference reference: [link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)
- tkinter uses "*windows*" as containers to pack "*widgets*" with functionality into these windows
- there can be different windows independent from each other

# Definitions
- **window**: refers to a rectangular area somewhere on the screen
- **top-level-window**: window that exists independently
- **widget**: the generic term for a tkiniter ui-element
- **frame**: basic container unit to organize widgets within a window
- **master, parent**: refers to the element that contains the widget (for top-level-windows None)
- **slave, master**: refers to the containing widgets of an element
- **cell**: area of intersection of a row and a column
- **geometry-manager**: manager object that spcifies the placing of widgets onto windows
- **event**: occurence of action that the application has to be informed of
- **event handler**: function that gets called when an event occurs
> within this document the terms "widget" and "ui-element" are used interchangeably
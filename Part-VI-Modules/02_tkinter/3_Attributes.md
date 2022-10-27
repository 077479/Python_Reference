# Basics
- each widget has a set of options to alter their behavior or appearance called "*configuration options*"
- most of the widgets share common "*configuration options*" like size
- there are different ways to set the "*configuration options*"
- to get the value of a "*configuration option*" widgets provde the `widget.cget()` method

# Configuration at Creation
- "*configuration options*" can be passed at creation
- `btn = tkinter.Button(text="Button", foreground="#000000", backgroundg="#ffffff")`

# Configuration with Dictionary
- the "*configuration options*" are stored in a dict within the widget
- with the option as str(key) and the value as value under the key
- `btn["foreground"] = "#f39211"`

# Configuration with Method
- every widget provides a configuration method to alter "*configuration options*"
    - `btn.config(foreground="#01ff00")`

# Dimensions
- dimensions like the size can be altered in various ways
- but if a value is given as `int` it is considered as pixel
- to alter that behavior a string that specifies the unit is provided
- e.g. `"1c"` refers to 1 centimeter
- c: centimeter, i: inches, m: millimeter, p: printer_points

# Coordinates
- the origin of tkinter widgets is (if not otherwise specified) at (0,0) (upper left)

# Colors
- tkinter represent colos as strings in hexadecimal
-  4Bit Color: `"#rgb"`, e.g. green: `"#0f0`
-  8Bit Color: `"#rrggbb"`, e.g. blue: `"#0000ff"`
- depending on the local installation some standart colors may be aviable like `"white"` or `"blue"`

# Fonts
- tkinter provides differnet ways to specify a font
- `widget.font("font_family", size, option)`:
    - font_family: name of the font
    - size: size of the font, as positive int => printer points, negative int => pixel
    - option: bold, italic, underline, overstrike
    - e.g.: `widget.font("Times", -16, "bold italic")` Times font with 16 pixel with **Bold** ans *Italic* as option
> there are font objects too but not covered here (tkFont.Font)

# Anchors
- the anchorsystem specifies the alignment of a widget
- tkinter uses compass directions, whereas North will be Top
    - tk.N: Top
    - tk.NE: Top-Right
    - tk.E: Right
    - tk.SE: Bottom-Right
    - tk.S: Bottom
    - tk.SW: Bottom-Left
    - tk.W: Left
    - tk.NW: Top-Left
    - tk.CENTER: Centered

# Relief
- relief refers to a simulated 3d effect
- the width of the border can be determined by the `"borderwidth"` option
- **Options**
    - "RAISED"
    - "SUNKEN"
    - "GROOVE"
    - "RIDGE"

# Bitmap
- tkinter supports any bitmaps in xbm format

# Cursors
- different cursors can be specified with the `"cursor"` option

# Images
- a lot of the widgets can display an image
- tkinter supports the images from the Pillow module
- but tkinter brings own image format modules
- **ImageTk**:
    - tkinter.ImageTk(file=FILE)
    - variety of formats: XBM, PGM, PPM, GIF, PNG
- **BitmapImage**:
    - tkinter.BitmapImage(file=FILE)
    - two color: XBM
- **PhotoImage**:
    - tk.PhotoImage(file=FILE)
- tkinter does not store a referenfce to the image
- if the last reference to the image is lost a blnk widget will be displayed

# Geometry String
- the geometry string specifies the position and size of a window
- window.geometry([width]x[height]+/-[x]+/-[y])
- **width**: width of the window
- **height**: height of the window
- **x**: x padding from the display edge
- **y**: y padding from the display edge

# Window Hierarchy
- widgets are packed into container widgets
- this forms a native hierarchy e.g. root_window => frame => button
- the first element given to the init of a widget is the parent
- the attribute "*master*" refers to the parent object
- this hierarchy is represented by the str representation of the widgets
- the str() function will return an "." if the widget is a top-level window
- and a "." with a number as id for a child
- e.g. `str(widget_parent)` returns "."
- e.g. `str(widget_child_child)` returns .[idnumber_child].[idnumber_child_child]
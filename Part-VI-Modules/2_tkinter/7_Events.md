# Basics
- an event is an action that happens during execution time of the application

# Binding
- tkinter calls the coupling of an event to a function "*binding*"
- binding happens on three levels
    1. **instance binding**: event is bound to a specific widget => widget.bind([event-sequence], [function_call])
    2. **class binding**: bind all widgets of a specific class like Button to an event => .bind_class("Widget-Class, [event-sequence], [function_call])
    3. **application binding**: like a global event => .bind_all([event-sequence], [function_call])

# Event Sequence
- in tkinter an event sequents refers a string containing one or more "*event-patterns*"
- one "*event-pattern*" describes one action that can happen
- if more than one "*event-pattern*" is given its considered an "*and*" logic (will only start the handler when all given events happen)
- general form of *"event-pattern"* `<[modifier]-type-[detail]>`
    - "*event-pattern*": has to be enclosed in `<...>`
    - "*type*": describes the general kind of event => keyboard-down
    - *"modifier"*: adding additionial requirements to the event => ctl-key pressed
    - "*detail*": specifying the event => s-key
- e.g.:
    - `<Button-1>` => mouse button 1
    - `<KeyPress-H>` => h
    - `<Control-KeyPress-s> => ctl+s`

# Event Modifiers
>
    Type        Description
    -----------------------
    Alt         alt key down
    Any         generalizes an event => <Any-KeyPress> any key on the keyboard
    Control     ctl key down
    Double      same event happens twice in a small time period => like doubleclick
    Lock        shift lock active
    Shift       shift key down
    Triple      same event happens three times in a small time period => like three times clicking

# Common Event Types
- link to a list of event-types: [link](https://www.tcl.tk/man/tcl8.5/TkCmd/bind.html#M7)
>
    Type Name           Description
    -------------------------------
    36   Activate       change from inactive to active
    37   Deactivate     change from active to inactive
    22   Configure      changing size
    17   Destroy        widget is beeing destroyed
    9    FocusIn        widget becomes the focus
    10   FocusOut       widget looses the focus

    4    Button         mouse button //detail: 1 => button 1 ... 4/5 mousewheel up/dow in linux
    5    ButtonRelease  mouse button up
    8    Leave          mouse moves out of the widget boundaries
    7    Enter          mouse enters the widget boundaries
    6    Motion         mouse motion wihtin the widget boundaries
    38   MouseWheel     mouse wheel on windows/macOs NOT ON LINUX

    2    KeyPress       keyboard key
    3    KeyRelease     keyboard key released

    12   Expose         become visible after beeing covered by another object    
    19   Map            widget is beeing mapped => placed with a geometry-manager
    18   Unmap          unmapping of a widget => removed by a geometry-manager
    15   Visibility     when some part of the application become visible on the screen

# Keyboard Keys
- list to keyboard keys: [link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html)

# Handlers
- the term "*event-handler*" refers to the function that an event is bound to over a widget
- the callback to the function will give the "*event*" as argument
- **Attributes of an Event**:
    - char: if keyboard event the pressed key
    - keycode: code of the key
    - keysym: string name of key
    - keysym_num: numeric representation of the key

    - num: the number of the mouse button
    - delta: if mousewheel represents the amount of mouswheel spins thingies (pos if up, neg if down)
        > different vals for different os => win: 120 is one up, macOS: 1 is up

    - serial: integer that is incremented everytime a client will be processed

    - height: if resizing event the new height of the widget
    - width: for resizing event the new width
    - state: integer describing the state of modifier keys
        - 0x0001: Shift.
        - 0x0002: Caps Lock.
        - 0x0004: Control.
        - 0x0008: Left-hand Alt.
        - 0x0010: Num Lock.
        - 0x0080: Right-hand Alt.
        - 0x0100: Mouse button 1.
        - 0x0200: Mouse button 2.
        - 0x0400: Mouse button 3. 
    - time: integer that is incremented every milisecond => to get time management
    - type: numeric representation of the event type
    - widget: the widget that caused the event
    - x: x-coord of the mouse during the event
    - y: y-coord of the mouse during the event
    - x_root: x-coord of the mouse relative to the screen x=0 during the event
    - y_root: y-coord of the mouse relative to the screen y=0 during the event
- e.g.
```python
def __drawOrangeBlob(self, event):
    '''Draws an orange blob in self.canv where the mouse is.'''
    r = 5   # Blob radius
    self.canv.create_oval(event.x-r, event.y-r,
        event.x+r, event.y+r, fill='orange')
```

# Virtual Events
- custom created events are called "*Virtual Events*" in tkinter
- the `event.add()` method allows to put a group of tkinter-built-in events into one event
- if any of the events in this "*event-container*" is triggered the event is triggered
- e.g. `widget.event_add("<<panic>>", "<Button-3>", "<keyPress-Pause>")`; widget.bind("<<panic>>", "<keypress-h>")
- the "*virtual-event*" has to be put in `<<>>`
- list of event related methods:
    - .event_add()
    - .event_delete()
    - .event_info()
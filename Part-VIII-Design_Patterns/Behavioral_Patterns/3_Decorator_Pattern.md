# 3 Decorator Pattern
## 3.1 Basics
- a decorator wraps an object(called core) with another object (to provide additional functionality)
- the interface of the core object(i.e. decorated object) will interact as if it were undecorated
- lets you attach new behaviors to objects by placing these inside a special wrapper
- "extend your basic behavior, but without altering yourself"
- decorators can decorate itself

## 3.2 Usecases
    - enhancing the response of a component as it sends data to a second component
    - supporting multiple optional behaviors (good alternative to multiple inheritance)
    - example:
        - notification program, where clients get a notification email
        - now the system should be extended to other communication channels
        - so the system gets a "notification" object that subclasses implement the actual methods like one object for facebook notification, one for sms notifications, one for slack notifications . . .
        - now there should be the possibility to send notifications on different channels for the same event to the same client

## 3.3 General Design
    - a wrapper contains the same methods as the target and delegates requests it receives
    - the wrapper does something to the information either "before" delegating the information, or "after" the information is processed by the core object
    - from the client perspective the wrapper and the core are identical because of the same interfaces
    - the resulting objects will be structured like a stack (the last of the stack will be the object that the client work with)

## 3.4 Python Implementation
### 3.4.1 Implementation
- "decorated_function_name = wrapper(function)"
- when the function isnt mentioned to be called without the wrapper the "@decorator" syntax can be used
- e.g.
````python
    function_name = wrapper(function_name)	# would replace the function call with the wrapped version
                                            # is the same as
    @wrapper
    def function_name():
        pass
````

### 3.4.2 Example
- example of a socket wrapper for the response function, the script will depending of "virtual"(that are not implemented) variables decorate the client socket
````python
    import gzip, socket
    from io import BytesIO

    class LogSocket:
        '''
        decorator that logs the send information to the console
        '''
        def __init__(self, socket):
            self.socket = socket

        def send(self, data):
            print(f"sending {data} to {self.socket.getpeername()}")
            self.socket.send(data)

        def close(self):
            self.socket.close()

    class GzipSocket:
        '''
        decorator that compresses the send information befor sending it
        '''
        def __init__(self, socket):
            self.socket = socket

        def send(self, data):
            buf = BytesIO()
            zipfile = gzip.GzipFile(fileob=buf, mode="w")
            zipfile.write(data)
            zipfile.close()
            self.socket.send(buf.getvalue())

        def close(self):
            self.socket.close()

    '''
    actual simple example code
    '''
    def respond(client):
        '''
        it would be totally acceptable to make the call to the decorator in the parameters of the function:
        def respond(LogSocket(client))
        '''
        response = input("Enter a val: ")
        client.send(bytes(response, "utf8"))
        client.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind("localhost", 2401)
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            if log_send:
                client = LogSocket(client)
            if client.getpeername()[0] in compress_hosts:
                client = GzipSocket(client)
            respond(client)								
        finally:
            server.close()
````
- here the socket class could easily be inherited from and the send method could be overwritten and after printing the input the "super().send(data)" method could be called
- Decorators are handy if the core object has to be modified dynamically, according to outside conditions (here for example if the server runs in debug mode)

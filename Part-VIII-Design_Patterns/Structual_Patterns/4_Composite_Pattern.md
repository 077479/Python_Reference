# 4 Composite Pattern
## 4.1 Basics
- creates tree like object structure
- these structures can be accessed as if they were an object
- the nodes of the tree like structure are called "composite objects"
- composite objects are like object containers

## 4.2 Usecase
- classic tree-structure problems

## 4.3 General Design
- traditional the composite objects categorized into "leaf nodes" cant contain further objects and "composite nodes"
- both objects have the same interface

## 4.4 Python Implementation
### 4.4.1 Implementation
- duck typing can be used to implicitly provide an interface

### 4.4.2 Example
````python
    class Component:
        def __init__(self, name):
            self.name = name
        
        def move(self, new_path):
            new_folder = get_path(new_path)
            del self.parent.children[self.name]
            new_folder.children[self.name] = self
            self.parent = new_folder

        def delete(self):
            del self.parent.children[self.name]

    class Folder(Component):
        def __init__(self, name):
            super().__inti__(name)
            self.children = dict()

        def add_child(self, child):
            child.parent = self
            self.children[child.name] = child

        def copy(self, new_path):
            pass

    class File(Component):
        def __init__(self, name, content):
            super().__inti__(name)
            self.content = content

        def copy(self, new_path):
            pass

    root = Folder("")

    # module level function to get a path
    def get_path(path):
        names = path.split("/")[1:]
        node = root
        for name in names:
            node = node.children[name]
        return node
````
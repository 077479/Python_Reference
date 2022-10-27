# 6 State Pattern
## 6.1 Basics
- Similar to the Strategy Pattern, it changes its internal workings dependent on its current state
- can appear to be another object
- a context(also called manager) that provides an interface to switch states (pointer to the current state)
- the "states" have to know when the context has to change the state and have, depending on this, to guarantee the transition between the states
- allows switching between different states dynamically

## 6.2 Usecase
- when you have an object that behaves differently depending on its current state, the number of states is enormous and the state-specific code channges frequently
- when a class is polluted with massive conditionals, that alter the behavior according to the current values
- if there is a lot of duplicate code across similar states

## 6.3 General Design
- context class that maintains the current state and relays the actions to the state classes
- multiple state classes are typically hidden from the outside
- the context acts like a black box

## 6.4 Python Implementation
### 6.4.1 Implementation
- state patterns can be implemented with coroutines (is almost the single use for it outside of asyncio)

### 6.4.2 Example
````python
    class Node:
        def __init__(self, tag_name: str="root", parent= None):
            self.parent = parent
            self.tag_name = tag_name
            self.children = []
            self.text = ""

        def __str__(self) -> str:
            if self.text:
                return f"{self.tag_name + ': '}{self.text}"
            return self.tag_name

    class Parser:
        def __init__(self, parse_string: str) -> None:
            self.parse_string = parse_string
            self.root = None
            self.current_node = None
            self.state = FirstTag()

        def process(self, remaining_string: str) -> None:
            remaining = self.state.process(remaining_string, self)
            if remaining:
                self.process(remaining)

        def start(self) -> None:
            self.process(self.parse_string)

    class FirstTag:
        def process(self, remaining_string: str, parser: Parser) -> str:
            i_start_tag = remaining_string.find("<")
            i_end_tag = remaining_string.find(">")

            tag_name = remaining_string[i_start_tag +1 : i_end_tag]

            root = Node(tag_name)

            parser.root = parser.current_node = root
            parser.state = ChildNode()

            return remaining_string[i_end_tag+1:]

    class ChildNode:
        def process(self, remaining_string: str, parser: Parser) -> str:
            stripped = remaining_string.strip()
            if stripped.startswith("</"):
                parser.state = CloseTag()
            elif stripped.startswith("<"):
                parser.state = OpenTag()
            else:
                parser.state = TextNode()
            return stripped

    class TextNode:
        def process(self, remaining_string: str, parser: Parser) -> str:
            i_start_tag = remaining_string.find("<")
            text = remaining_string[:i_start_tag]
            parser.current_node.text = text
            parser.state = ChildNode()
            return remaining_string[i_start_tag:]

    class OpenTag:
        def process(self, remaining_string: str, parser: Parser) -> str:
            i_start_tag = remaining_string.find("<")
            i_end_tag = remaining_string.find(">")
            tag_name = remaining_string[i_start_tag+1 : i_end_tag]
            node = Node(tag_name=tag_name, parent=parser.current_node)
            parser.current_node.children.append(node)
            parser.current_node = node
            parser.state = ChildNode()
            return remaining_string[i_end_tag +1:]

    class CloseTag:
        def process(self, remaining_string: str, parser: Parser) -> str:
            i_start_tag = remaining_string.find("<")
            i_end_tag = remaining_string.find(">")

            assert remaining_string[i_start_tag + 1] == "/"

            tag_name = remaining_string[i_start_tag + 2: i_end_tag]

            assert tag_name == parser.current_node.tag_name

            parser.current_node = parser.current_node.parent
            parser.state = ChildNode()
            return remaining_string[i_end_tag + 1:].strip()

    if __name__ == "__main__":
        import sys
        with open(sys.argv[1]) as file:
            contents = file.read()
            p = Parser(contents)
            p.start()

            nodes = [p.root]
            while nodes:
                node = nodes.pop(0)
                print(node)
                nodes = node.children + nodes
````
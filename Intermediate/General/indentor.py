# implementing some kinda context manager with the indentation example
# like a DSL language like python.
class Indentor:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1
    
    def print(self, text):
        print('    ' * self.level + text)


with Indentor() as indent:
    indent.print("amir")
    with indent:
        indent.print("is moving")
        with indent:
            indent.print("forward")
            with indent:
                indent.print("always")
    
    indent.print("period.")

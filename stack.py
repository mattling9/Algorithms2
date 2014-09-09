class Stack():
    """a representation of a stack"""
    def __init__(self, MaxSize):
        self.MaxSize = MaxSize
        self.StackPointer = 0
        self.list = []

    def size(self):
        StackSize = len(self.items)
        return StackSize

    def pop(self):
        size = self.StackSize()
        if Size > 0:
            self.items.pop()
            self.StackPointer = size
        else:
            print("There are no items in the stack")

    def push(self, item ):
        

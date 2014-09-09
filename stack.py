class Stack():
    """a representation of a stack"""
    def __init__(self, MaxSize):
        self.MaxSize = MaxSize
        self.StackPointer = 0
        self.List = []

    def size(self):
        StackSize = len(self.List)
        return StackSize

    def pop(self):
        StackSize = self.StackSize()
        if StackSize > 0:
            self.items.pop()
            self.StackPointer = StackSize
        else:
            print("There are no items in the stack")


    def push(self, item ):
        size()
        StackSize = self.StackSize()
        if self.StackSize < MaxSize:
            self.List.append(item)
            self.StackPoitner = StackSize
        else:
            print("The stack is full")

    def peek(self):
        size()
        StackSize = self.StackSize
        if StackSize == 0:
            print(" the stack is empty")
        else:
            print("The top item is {0}".format(self.List[StackSize-1]))

def main():
    CustomStack = Stack(5)
    Done = False
    while Done == False:
        print("Please select an option")
        print()
        print("1. Peek")
        print("2. Push")
        print("3. Pop")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            CustomStack.peek()
        elif choice == 2:
            CustomStack.push()
        elif choice == 3:
            CustomStack.pop()
        elif choice == 4:
            Done = True
        while choice < 2 or choice > 4:
            print("Please enter a valid number")
            choice=int(input())

if __name__ == "__main__":
    main()


    

        
        

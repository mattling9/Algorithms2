
class Stack():
    """A Class to represent a Stack"""
    def __init__(self, MaxStackSize):
        self._StackPointer = 0
        self._MaxStackSize = 5

def main():
    print("1. Push data onto the stack")
    print("2. Pull data from the stack")
    print()
    choice= int(input("Please choose a choice form the list above"))
    if choice == 1:
        
        

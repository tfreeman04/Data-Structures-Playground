class StackEmptyError(Exception):
    """ raised when attempting to pop or peek from an empty Stack"""

    pass


class Stack:
    """ 
    Stack data structure (LIFO)

    Supports push, pop, peek operations

    """

def __init__(self):

    self._items = [] 


    def is_empty(self) -> bool:
        """ Reutrn True if Stack is empty """
        return len(self._items) == 0

    def push(self,item):

        """ add item to the top of the Stack"""
        self._items.append(item)

    def pop(self):

        """
        Remove and return item from the top of the stack
        Raises StackEmptyError if the stack is empty.

        """
        if self.isEmpty():
            raise StackEmptyError("Cannot pop from an empty stack ")
        
        return self._items.pop()
    
    def peek(self):
        """ 
        Returns the top item without removing it from the Stack
        Raises StackEmptyError if the Stack is empty.
        """
        if self.isEmpty():
            raise StackEmptyError("Cannot peek from an empty stack ")
        
        return self._items[-1]
    
    def size(self):
        """ Returns the number of items in the Stack"""

        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"

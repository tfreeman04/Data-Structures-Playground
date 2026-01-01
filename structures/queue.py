class queue_empty(Exception):
    """ raised when attempting to dequeue or peek from an empty Queue"""
    pass
class Full(Exception):
    """ raised when attempting to enqueue to a full Queue"""
    pass
class queue:
    def __init__(self):
        self._itemsitems = []
        self.maxSize = 20

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        if len(self._items) >= self.maxSize:
            raise Full("enqueue to full queue")
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        return self._items.pop(0)
    def size(self):
        return len(self._items)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]
    
    def __repr__(self) -> str:
        return f"Queue({self._items})"
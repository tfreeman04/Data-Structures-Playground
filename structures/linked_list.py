class linked_list_empty(Exception):
    """ raised when attempting to operate on an empty linked list"""
    pass


class linked_list_node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = linked_list_node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = linked_list_node(value, self.head)
        self.head = new_node

    def delete_with_value(self, value):
        """ if value found, delete first occurrence of value in linked list """
        """ if list is empty """
        if not self.head:
            raise linked_list_empty("Cannot delete from an empty linked list")  
        """ if head needs to be removed """
        if self.head.value == value:
            self.head = self.head.next
            return
        """ traverse the list to find the value """
        current = self.head
        while current.next:
            if current.next.value == value:
                """ remove the node and set the next pointer to skip the node to be deleted """
                current.next = current.next.next
                return
            current = current.next

    def find(self, value):
        if not self.head:
            raise linked_list_empty("Cannot find in an empty linked list")
        
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return "->".join(map(str, values))
    
    def full(self):
        """ linked list is never full unless memory is exhausted """
        return False
    

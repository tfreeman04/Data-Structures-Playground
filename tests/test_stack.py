import pytest 

from structures.stack import Stack, StackEmptyError


def test_stack_initialisation():

    stack = Stack()
    assert stack.is_empty() is True
    assert stack.size() == 0

def test_push():

    stack = Stack() 
    stack.push(10)
    stack.push(20)

    assert stack.is_empty() is False
    assert stack.size() == 2
    assert repr(stack) == "Stack([10, 20])"
    assert stack.peek() == 20

def test_pop():

    stack = Stack()
    stack.push(10)
    stack.push(20)

    popped = stack.pop()
    assert popped == 20
    assert stack.size() == 1
    assert stack.peek() == 10

    popped = stack.pop()
    assert popped == 10
    assert stack.is_empty() is True

def test_peek():

    stack = Stack()
    stack.push(30)
    stack.push(40)

    top = stack.peek()
    assert top == 40
    assert stack.size() == 2  # Ensure size remains unchanged after peek    

def test_is_empty():

    stack = Stack()
    assert stack.is_empty() is True

    stack.push(50)
    assert stack.is_empty() is False

    stack.pop()
    assert stack.is_empty() is True

def test_size():

    stack = Stack()
    assert stack.size() == 0

    stack.push(60)
    stack.push(70)
    assert stack.size() == 2

    stack.pop()
    assert stack.size() == 1
def test_repr():

    stack = Stack()
    stack.push(80)
    stack.push(90)

    assert repr(stack) == "Stack([80, 90])"

def test_pop_empty():
    stack = Stack()
    with pytest.raises(StackEmptyError):
        stack.pop()

def test_peek_empty():
    stack = Stack()
    with pytest.raises(StackEmptyError):
        stack.peek()



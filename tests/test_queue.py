import pytest 
from structures.queue import queue_empty, queue, Full

def test_enqueue_dequeue():
    q = queue(maxsize=3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3 
    assert q.is_empty()
    assert q.size() == 0
def test_peek():
    q = queue()
    q.enqueue('a')
    q.enqueue('b')
    
    assert q.peek() == 'a'
    assert q.size() == 2  # size should remain unchanged after peek
def test_empty_dequeue_peek():
    q = queue()
    
    with pytest.raises(queue_empty):
        q.dequeue()
    
    with pytest.raises(queue_empty):
        q.peek()
def test_full_enqueue():
    q = queue(maxsize=2)
    q.enqueue(1)
    q.enqueue(2)
    
    with pytest.raises(Full):
        q.enqueue(3)
def test_size():
    q = queue()
    assert q.size() == 0
    
    q.enqueue(10)
    assert q.size() == 1
    
    q.enqueue(20)
    assert q.size() == 2
    
    q.dequeue()
    assert q.size() == 1
def test_is_empty():
    q = queue()
    assert q.is_empty() is True
    
    q.enqueue(5)
    assert q.is_empty() is False
    
    q.dequeue()
    assert q.is_empty() is True
def test_repr():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert repr(q) == "Queue([1, 2, 3])"


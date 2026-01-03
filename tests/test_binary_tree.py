import pytest
from structures.binary_tree import binary_tree

def test_insert_and_inorder_traversal():
    bt = binary_tree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    
    assert bt.inorder_traversal() == [2, 3, 4, 5, 7]    

def test_preorder_traversal():
    bt = binary_tree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    
    assert bt.preorder_traversal() == [5, 3, 2, 4, 7]

def test_postorder_traversal():
    bt = binary_tree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    
    assert bt.postorder_traversal() == [2, 4, 3, 7, 5]

def test_empty_tree_traversals():
    bt = binary_tree()
    
    assert bt.inorder_traversal() == []
    assert bt.preorder_traversal() == []
    assert bt.postorder_traversal() == []

def test_repr():
    bt = binary_tree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    
    assert repr(bt) == "BinaryTree(3, 5, 7)"

def test_is_empty():
    bt = binary_tree()
    assert bt.is_empty() is True
    
    bt.insert(10)
    assert bt.is_empty() is False   

def test_multiple_insertions():
    bt = binary_tree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        bt.insert(v)
    
    assert bt.inorder_traversal() == sorted(values)

    
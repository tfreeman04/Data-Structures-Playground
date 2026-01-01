import pytest
from structures.linked_list import linked_list, linked_list_empty,linked_list_node

def test_append_and_repr():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert repr(ll) == "1->2->3" 

def test_prepend():
    ll = linked_list()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert repr(ll) == "1->2->3"

def test_delete_with_value():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete_with_value(2)
    assert repr(ll) == "1->3"
    
    ll.delete_with_value(1)
    assert repr(ll) == "3"
    
    ll.delete_with_value(3)
    assert repr(ll) == ""

    with pytest.raises(linked_list_empty):
        ll.delete_with_value(4)

def test_find():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.find(2) is True
    assert ll.find(4) is False

    empty_ll = linked_list()
    with pytest.raises(linked_list_empty):
        empty_ll.find(1)
def test_full():
    ll = linked_list()
    assert ll.full() is False  # linked list should never be full
    ll.append(1)
    assert ll.full() is False       
    ll.prepend(0)
    assert ll.full() is False
    for i in range(2, 1000):
        ll.append(i)
    assert ll.full() is False

def test_delete_from_empty_list():
    ll = linked_list()
    with pytest.raises(linked_list_empty):
        ll.delete_with_value(10)  

def test_repr_empty_list():
    ll = linked_list()
    assert repr(ll) == ""

def test_repr_single_element():
    ll = linked_list()
    ll.append(42)
    assert repr(ll) == "42"

def test_repr_multiple_elements():
    ll = linked_list()
    for i in range(5):
        ll.append(i)
    assert repr(ll) == "0->1->2->3->4"  

def test_prepend_to_empty_list():
    ll = linked_list()
    ll.prepend(10)
    assert repr(ll) == "10" 

def test_append_to_empty_list():
    ll = linked_list()
    ll.append(20)
    assert repr(ll) == "20"

def test_delete_non_existent_value():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete_with_value(4)  # Should not raise an error
    assert repr(ll) == "1->2->3"  # List should remain unchanged

def test_find_in_empty_list():
    ll = linked_list()
    with pytest.raises(linked_list_empty):
        ll.find(1)
def test_find_existing_value():
    ll = linked_list()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    assert ll.find(10) is True 

def test_find_non_existing_value():
    ll = linked_list()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    assert ll.find(20) is False

def test_multiple_deletes():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    
    ll.delete_with_value(2)
    assert repr(ll) == "1->3->2->4"
    
    ll.delete_with_value(2)
    assert repr(ll) == "1->3->4"
    ll.delete_with_value(5)  # Deleting non-existent value
    assert repr(ll) == "1->3->4"
def test_delete_head_multiple_times():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    ll.delete_with_value(1)
    assert repr(ll) == "2->3"
    
    ll.delete_with_value(2)
    assert repr(ll) == "3"
    
    ll.delete_with_value(3)
    assert repr(ll) == ""

def test_delete_tail():
    ll = linked_list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    ll.delete_with_value(3)
    assert repr(ll) == "1->2"
    ll.delete_with_value(2)
    assert repr(ll) == "1"
    ll.delete_with_value(1)
    assert repr(ll) == ""   

def test_delete_all_elements_one_by_one():
    ll = linked_list()
    for i in range(5):
        ll.append(i)
    
    for i in range(5):
        ll.delete_with_value(i)
        expected = "->".join(str(x) for x in range(i+1, 5))
        assert repr(ll) == expected                     

def test_delete_middle_element():
    ll = linked_list()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    
    ll.delete_with_value(20)
    assert repr(ll) == "10->30->40"
    
    ll.delete_with_value(30)
    assert repr(ll) == "10->40"

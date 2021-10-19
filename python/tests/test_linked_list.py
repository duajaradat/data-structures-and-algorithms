from linked_list.linked_list import LinkedList

def test_LinkedList_insert():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(100) == False

def test_LinkedList_str():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(56)
    test_LinkedList.insert(70)
    assert test_LinkedList.__str__() == f"{ 70 } -> { 56 } -> NULL"


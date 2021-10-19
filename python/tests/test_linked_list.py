from linked_list.linked_list import LinkedList

def test_LinkedList_insert():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(100) == False



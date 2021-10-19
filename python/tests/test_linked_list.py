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

def test_LinkedList_append():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(70)
    test_LinkedList.append(56)
    assert test_LinkedList.__str__() == f"{ 70 } -> { 56 } -> NULL"

def test_LinkedList_insertbefore():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.insert(34)
    test_LinkedList.insert(68)
    test_LinkedList.append(9)
    test_LinkedList.insert_before(9,67)
    assert str(test_LinkedList) == f"{ 68 } -> { 34 } -> { 6 } -> { 9 } -> NULL"

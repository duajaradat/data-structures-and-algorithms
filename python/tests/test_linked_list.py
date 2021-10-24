from data_structure.linked_list.linked_list import LinkedList

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
    assert str(test_LinkedList) == f"{ 68 } -> { 34 } -> { 6 } -> { 67 } -> { 9 } -> NULL"

def test_LinkedList_insertafter():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.insert(34)
    test_LinkedList.insert(68)
    test_LinkedList.append(9)
    test_LinkedList.insert_after(10,67)
    assert str(test_LinkedList) == f"{ 68 } -> { 34 } -> { 6 } -> { 9 } -> NULL"

def test_LinkedList_insertafter_two():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.insert_after(6,67)
    assert str(test_LinkedList) == f"{ 6 } -> { 67 } -> { 9 } -> NULL"

def test_LinkedList_length():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.linked_list_length() == 2

def test_LinkedList_kth_negative():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.kthFromEnd(-1) == "k is a negative number , please enter positive number"

def test_LinkedList_kth_bigger_than_length():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.kthFromEnd(5) == "k is greater than the linked list"

def test_LinkedList_kth_equal_to_length():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.kthFromEnd(2) == "k is greater than the linked list"

def test_LinkedList_kth_less_than_length():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.kthFromEnd(0) == 9

def test_LinkedList_kth_happy_path():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(2)
    test_LinkedList.insert(6)
    test_LinkedList.append(9)
    test_LinkedList.linked_list_length()
    assert test_LinkedList.kthFromEnd(1) == 2


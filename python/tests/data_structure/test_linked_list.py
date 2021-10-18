from data_structure.linked_list import LinkedList
def test_LinkedList_isert():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value==0



def test_LinkedList_include_one():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(1) == True





def test_LinkedList_insert_case_two():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    assert test_LinkedList.head.value==0


def test_LinkedList_include_two():
    test_LinkedList = LinkedList()
    test_LinkedList.insert(0)
    test_LinkedList.insert(1)
    assert test_LinkedList.includes(100) == False


def test_LinkedList_insertbefore():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(6)
    test_LinkedList.insert(34)
    test_LinkedList.insert(68)
    test_LinkedList.append(9)
    test_LinkedList.insert_after(34,1)
    test_LinkedList.insert_before(9,67)
    assert str(test_LinkedList) == f"{ 68 } -> { 34 } -> { 1 } -> { 6 } -> { 67 } -> { 9 } -> NULL"

def test_LinkedList_insertafter():
    test_LinkedList=LinkedList()
    test_LinkedList.insert(2)
    test_LinkedList.insert(4)
    test_LinkedList.insert(8)
    test_LinkedList.append(9)
    test_LinkedList.insert_after(4,1)
    assert str(test_LinkedList) == f"{ 8 } -> { 4 } -> { 1 } -> { 2 } -> { 9 } -> NULL"

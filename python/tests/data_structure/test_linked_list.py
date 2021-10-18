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



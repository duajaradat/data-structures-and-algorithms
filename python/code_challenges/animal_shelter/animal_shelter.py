class Animal:
    def __init__(self,value=None):
        """
        A class to create nodes
        """
        self.value = value
        self.next = None


class Animal_Shelter:
    """
    a class which holds only dogs and cats objects.
    """
    def __init__(self):
        self.front=None
        self.rear=None


    def  enqueue(self,animal):
        """
        enqueue method :
        Arguments: animal
        animal can be either a dog or a cat object.
        """
        new_node=Animal(animal)

        if not self.rear:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def is_empty(self):
        if not self.rear:
            return True
        else:
            return False

    def dequeue(self,pref):
        """
        dequeue method :
        Arguments: pref
        pref can be either "dog" or "cat" nodes
        Return: either a dog or a cat, based on preference.
        If pref is not "dog" or "cat" then return null.
        """
        if self.is_empty():
            raise Exception("Animal Shelter is Empty")

        if  self.front.value==pref:
            removed_node=self.front.value
            self.front=self.front.next
            removed_node.next=None
            return removed_node

    def __str__(self):
        name=self.front
        string=''
        while name:
            string+=f'{name.value} ->'
            name=name.next
        return string










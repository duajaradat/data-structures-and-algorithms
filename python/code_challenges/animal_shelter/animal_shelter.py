class Animal:
    def __init__(self,value=None):
        """
        A class to create nodes
        """
        self.value = value
        self.next = None


class Dog:
    def __init__(self,dog_name):
        self.name=dog_name
        self.type ='Dog'

class Cat:
    def __init__(self,cat_name):
        self.name=cat_name
        self.pref ='Cat'

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


        if  self.front.value.__class__.__name__==pref:   #  1
            removed_node=self.front.value  #  1
            self.front=self.front.next   #  1
            removed_node.next=None     #  1
            return removed_node.name





if __name__ == '__main__':
    bondoq=Cat('bondoq')
    animal1=Animal_Shelter(bondoq)
    animal1.enqueue(bondoq)








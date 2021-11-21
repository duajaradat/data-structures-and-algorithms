from data_structure.linked_list.linked_list import LinkedList , Node

class HashTable:
    """
    class simulatethe functionality of a hash table
    """
    def __init__(self, size=1024):
        """
        Initalization of a hash table
        Args : size of the array to
               bucket is what is contained in each index of the array
        """
        self.size = size
        self.buckets = [None] * self.size

    def __hash(self,key):
        """
        hash function to get the hash value of the key
        Args : key to be hashed
        Returns : hash index of the key
        """
        hash_value=0
        for char in key:
            hash_value+=ord(char)
        return hash_value % self.size

    def add(self, key, value):
        """
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        Args : key to be added
               value to be added to the key
        Returns : None
        """
        index = self.__hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        self.buckets[index].insert([key,value])


    def get(self, key):
        """
        This method should hash the key, and return the value from the table, handling collisions as needed.
        Args : key to be searched
        Returns : value of the key
        """
        index = self.__hash(key)
        if not self.buckets[index]:
            return None
        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

    def contains(self, key):
        """
        This method should hash the key, and return true if the key is in the table, false otherwise.
        Args : key to be searched
        Returns : boolean
        """
        index = self.__hash(key)
        if not self.buckets[index]:
            return False
        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        """
        This method should hash the key, and remove the key and value from the table, handling collisions as needed.
        Args : key to be removed
        Returns : None
        """
        index = self.__hash(key)
        if not self.buckets[index]:
            return None
        if self.buckets[index].head.value[0] == key:
            self.buckets[index].head = self.buckets[index].head.next
            return



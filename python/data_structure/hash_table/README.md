# Hash Table Implementation

## Author
*Du'a Jaradat*

---

## Links
- [Pull Request](https://github.com/duajaradat/data-structures-and-algorithms/pull/45)

- [Code](https://github.com/duajaradat/data-structures-and-algorithms/blob/hashtable/python/data_structure/hash_table/hashtable.py)


---

### Problem Domain

Challenge Type: New Implementation

**Implementation**

Implement a Hashtable Class with the following methods:

- add

     - Arguments: key, value
     - Returns: nothing
     - This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- get
     - Arguments: key
     - Returns: Value associated with that key in the table

- contains
     - Arguments: key
     - Returns: Boolean, indicating if the key exists in the table already.

- hash
     - Arguments: key
     - Returns: Index in the collection for that key

### Structure and Testing

Write tests to prove the following functionality:

- [] Adding a key/value to your hashtable results in the   value being in the data structure
- []Retrieving based on a key returns the value stored
- []Successfully returns null for a key that does not exist in the hashtable
- []Successfully handle a collision within the hashtable
- []Successfully retrieve a value from a bucket within the hashtable that has a collision
- []Successfully hash a key to an in-range value


---

### Big O Analysis


|| Time | Space |
|:-----------| :----------- | :----------- |
|Hash Table | O() | O() |

---


### Whiteboard Visual
***[Hash Table]***
![Hash Table]()


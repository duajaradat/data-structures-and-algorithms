# Challenge Setup & Execution

## Author
*Du'a Jaradat*

---

## Links
[Pull Request](https://github.com/duajaradat/data-structures-and-algorithms/pull/35)
[Code](https://github.com/duajaradat/data-structures-and-algorithms/blob/stack-queue-pseudo/python/data_structure/stacks_queues/stack-queue-pseudo.py)

### Problem Domain

***Implement a Queue using two Stacks***

***Feature Tasks***

- Create a new class called pseudo queue.
     - Do not use an existing Queue.
     - Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
     - Internally, utilize 2 Stack instances to create and manage the queue

- Methods:
     - enqueue
         - Arguments: value
          - Inserts value into the PseudoQueue, using a first-in, first-out approach.
     - dequeue
         - Arguments: none
         - Extracts a value from the PseudoQueue, using a first-in, first-out approach.h

**NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.**

---

### Inputs and Expected Outputs

 **[Enqueue]**

| Input | Arg    |Expected Output |
| :----------- |:-----------| :----------- |
| [10]->[15]->[20] | 5 |[5]->[10]->[15]->[20] |
|  |5 |[5] |


 **[Dequeue]**

| Input | Arg    |Expected Output |
| :----------- |:-----------| :----------- |
| [5]->[10]->[15]->[20] | 20 |[5]->[10]->[15])|
|[5]->[10]->[15]  |15 |[5]->[10] |


---

### Big O


| Time | Space |
| :----------- | :----------- |
| O(1) | O(1) |


---





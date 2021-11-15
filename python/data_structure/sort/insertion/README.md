
# Challenge Setup & Execution

## Author
*Du'a Jaradat*

---

## Links
- [Pull Request](https://github.com/duajaradat/data-structures-and-algorithms/pull/42)

- [Code](https://github.com/duajaradat/data-structures-and-algorithms/blob/insertion-sort/python/data_structure/sort/insertion/insertion_sort.py)

### Problem Domain

**Implementation**

- Provide a visual step through for each of the sample arrays based on the provided pseudo code

- Convert the pseudo-code into working code in your language

- Present a complete set of working tests

### Structure and Testing

- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)



---

### Big O Analysis


|| Time | Space |
|:-----------| :----------- | :----------- |
|Insertion sort | O(n^2) | O(1) |

---

## Steps to  do Insertion Sort
for the example in the WhiteBoard :
```python
arr = [8,4,23,42,16,15]
```
### PASS 1
Initially, an array of 6 integers, in order to implement the insertion sort, we shall take two variables, i and j,  j is the index of the first element whereas i is the index of second element.
```python
i = 1
j = i - 1 = 0
```
Making a temporary variable key to store the value of the ith element temporarily.
```python
arr[i] = 4
```
While j equal or bigger than 0 ,and temp is less than arr[j] , then place the value of the jth element at the index ‘j+1’.

```python
arr[j + 1] = arr [j] = 8
```
Now decrement ‘j’ by one, i.e j-1, if we do this, the jth index will become less than zero, so it will break the while loop .

```python
arr[j+1]= temp = 4
arr = [4,8,23,42,16,15]
```
### PASS 2

Now , i , j will be increased one , and temp will be arr[i] , then the condition for the while loop will not be true because temp is bigger than arr[j]. So in this pass nothing will be changed.
```python
i = 2
j = i - 1 = 1
temp = arr[i] = 23

temp > arr[j]
23 > 8
```

### PASS 3

Now , i , j will be increased one , and temp will be arr[i] , then the condition for the while loop will not be true again for the same reson in PASS 2. So keep every thing as is.
```python
i = 3
j = i - 1 = 2
temp = arr[i] = 42

temp > arr[j]
42 > 23
```

### PASS 4

Now , i , j will be increased one , and temp will be arr[i] , then the condition for the while loop will be true , so will enter the while loop , and assign the value of index j to arr[j + 1] , make a shift in the array. then decrease j by one to compare it with again with temp.
```python
i = 4
j = i - 1 = 3
temp = arr[i] = 16

# /// first iteration
temp < arr[j]
16 < 42

arr[4] = 42
j = j-1 = 3-1=2

# /// second iteration
temp = 16
temp < arr[j]
16 < 23

arr[3] = 23
j = j - 1 = 2 - 1 = 1

[4,8,16,23,42,15]

```

### PASS 5
Now , i , j will be increased one , and temp will be arr[i] , then the condition for the while loop will be true , so will enter the while loop , and assign the value of index j to arr[j + 1] , make a shift in the array. then decrease j by one to compare it with again with temp. and stick with the while loop until the condition will be false

```python
i = 5
j = i - 1 = 4
temp = arr[i] = 15

# /// first iteration
temp < arr[j]
15 < 42

arr[5] = 42
j = j-1 = 4-1=3

# /// second iteration
temp = 15
temp < arr[j]
15 < 23

arr[4] = 23
j = j - 1 = 3 - 1 = 2

# /// third iteration
temp = 15
temp < arr[j]
15 < 16

arr[3] = 16
j = j - 1 = 2 - 1 = 1

# /// fourth iteration
temp = 15
temp < arr[j]
15 < 8  --- > # will not enter the loop


[4,8,15,16,23,42]

```
---

### Whiteboard Visual
***[Insertion Sort]***
![Insertion-Sort](insertion_sort1.png)
![Insertion-Sort](insertion_sort2.png)


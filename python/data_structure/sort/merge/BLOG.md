## Steps to  do Merge Sort
for the example in the WhiteBoard :
```python
arr = [8,4,23,42,16,15]
```
**Given unsorted list of elements.**

Divide the unsorted array into two halves

```python
mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

[8,4,23],[42,16,15]
```
Call the fuction merge again for the halves.
Keep dividing it until the subpart of the list consists of only one element.
```python
     merge_sort(left)
     merge_sort(right)

[8][4] [23]  |  [42][16] [15]
```
Later, we will combine the two elements in the given sorted manner.
```
[8][4] [23]  |  [42][16] [15]
# merge after sorting
[4,8] [23]   |  [16,42]  [15]

Again, we will combine the two lists of two elements and convert them into a list of four elements after sorting. We will keep repeating the process until we find the final sorted sequence of the array
```python

# merge after sorting
[4,8,23]   |  [15,16,42]
```

The final sorted sequence of data
```python
# final merge
  [4,8,15,16,23,42]
```

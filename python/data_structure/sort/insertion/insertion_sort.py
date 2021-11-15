def insertion_sort(arr):
    """
    This is a function takes a list of unsorted integers
    Arguments --> arr of int
    Returns --> None
    """
    i = 1
    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        while j >=0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp
    return arr


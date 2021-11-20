def quick_sort(arr, left=0, right=None):
    """
    Sort a list of integers in ascending order
    Args:
        arr (int): list
        left (int): number
        right (int): number
    Returns :
     a sorted list
    """
    if right == None:
        right = len(arr) - 1

    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, (position - 1))
        quick_sort(arr, (position + 1), right)
    return arr

def partition(arr, left, right):
    """
    Sets a pivot which is a value in the partitioning space to find a position

    Args:
        arr (int)
        left (int)
        right (int)

    Returns: pivot index
    """
    pivot = arr[right]
    low = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)
    return low + 1


def swap(arr, i, low):
    """Swaping the location of two indexes i , low

    Args:
        arr (int)
        i (int)
        low (int)
    Returns: None
    """
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

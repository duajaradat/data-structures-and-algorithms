def merge_sort(array):

    n = len(array)

    if n > 1:
        mid_index = n // 2
        left = array[0:mid_index]
        right = array[mid_index:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)

    return array

def merge(left, right, array):
    l_index = 0
    r_index = 0
    output_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            array[output_index] = left[l_index]
            l_index += 1
        else:
            array[output_index] = right[r_index]
            r_index += 1

        output_index += 1

    if l_index == len(left):
        while r_index < len(right):
            array[output_index] = right[r_index]
            r_index += 1
            output_index += 1
    else:
        while l_index < len(left):
            array[output_index] = left[l_index]
            l_index += 1
            output_index += 1

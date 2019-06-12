def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr if x < arr[0]]) + [arr[0]] + qsort([x for x in arr if x > arr[0]])


def qsort_alt(arr):
    if len(arr) <= 1:
        return arr
    else:
        lesser_than_pivot = []
        greater_than_pivot = []
        pivot = arr[len(arr)-1]
        for element in arr[:len(arr)-1]:
            if element < pivot:
                lesser_than_pivot.append(element)
            else:
                greater_than_pivot.append(element)
        return qsort_alt(lesser_than_pivot)+[pivot]+qsort_alt(greater_than_pivot)


def qsort_space(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)-1]
    wall_idx, idx = 0, 0

    while idx < len(arr)-1:
        if arr[idx] < pivot:
            if idx != wall_idx:
                arr[wall_idx], arr[idx] = arr[idx], arr[wall_idx]
            wall_idx += 1
            idx += 1
        else:
            idx += 1
    arr[wall_idx], arr[len(arr)-1] = arr[len(arr)-1], arr[wall_idx]

    return qsort_space(arr[:wall_idx]) + [arr[wall_idx]] + qsort_space(arr[wall_idx+1:])


def qsort_eff(arr, start, end):
    pivot = arr[end]
    wall_idx, idx = start, start

    while idx < end:
        if arr[idx] < pivot:
            if idx != wall_idx:
                arr[wall_idx], arr[idx] = arr[idx], arr[wall_idx]
            wall_idx += 1
            idx += 1
        else:
            idx += 1
    arr[wall_idx], arr[end] = arr[end], arr[wall_idx]

    if start <= wall_idx-1:
        qsort_eff(arr, start, wall_idx-1)
    if wall_idx+1 <= end:
        qsort_eff(arr, wall_idx+1, end)


if __name__ == '__main__':
    # arr = [23, 26, 123, 341, 1245, 1211, 667, 134, 764, 1, 27]
    arr = [2983, 1341248, 8, 1, 134, 123, 673, 3, 562, 78, 334, 897, 123, 576, 333, 87, 243443]
    print(arr, end="; before quick sorting\n")
    qsort_eff(arr, 0, len(arr)-1)
    print(arr, end="; after quick sorting")

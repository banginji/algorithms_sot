def build_min_heap(arr):
    for idx in range(len(arr) // 2, -1, -1):
        min_heapify(arr, idx)


def min_heapify(arr, idx):
    left_idx = left(idx)
    right_idx = right(idx)
    if left_idx < len(arr) and arr[left_idx] < arr[idx]:
        smallest_idx = left_idx
    else:
        smallest_idx = idx
    if right_idx < len(arr) and arr[right_idx] < arr[smallest_idx]:
        smallest_idx = right_idx
    if smallest_idx is not idx:
        arr[idx], arr[smallest_idx] = arr[smallest_idx], arr[idx]
        min_heapify(arr, smallest_idx)

def left(idx):
    return 2 * idx + 1


def right(idx):
    return 2 * idx + 2

def heap_sort(arr):
    build_min_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        # print(arr, end=", before\n")
        arr[0], arr[i] = arr[i], arr[0]
        # arr = arr[:i]
        # print(arr, end=", after\n")
        temp = arr[:i]
        min_heapify(temp, 0)
        arr = temp+arr[i:]
    return arr


if __name__ == '__main__':
    print("Min Heap Impl")
    # arr = [34, 65, 23, 87]
    arr = [534, 63, 24, 762, 7, 123, 678, 34, 787, 34]
    # arr = heap_sort(arr)
    build_min_heap(arr)
    print(arr)

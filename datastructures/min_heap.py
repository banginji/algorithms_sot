def build_min_heap(heap):
    for idx in range(len(heap) // 2, -1, -1):
        min_heapify(heap, idx)


def min_heapify(heap, idx, last_idx_sub_heap=None):
    left_idx = left(idx)
    right_idx = right(idx)
    len_heap = len(heap) if not last_idx_sub_heap else last_idx_sub_heap
    if left_idx < len_heap and heap[left_idx] < heap[idx]:
        smallest_idx = left_idx
    else:
        smallest_idx = idx
    if right_idx < len_heap and heap[right_idx] < heap[smallest_idx]:
        smallest_idx = right_idx
    if smallest_idx is not idx:
        heap[idx], heap[smallest_idx] = heap[smallest_idx], heap[idx]
        min_heapify(heap, smallest_idx, None if not last_idx_sub_heap else last_idx_sub_heap)


def left(idx):
    return 2 * idx + 1


def right(idx):
    return 2 * idx + 2


def heap_sort(heap):
    build_min_heap(heap)
    for idx in range(len(heap)-1, 0, -1):
        heap[0], heap[idx] = heap[idx], heap[0]
        #temp = heap[:idx]
        min_heapify(heap, 0, idx)
        #heap = temp+heap[idx:]
    return heap


if __name__ == '__main__':
    heap = [534, 63, 24, 762, 7, 123, 678, 34, 787, 34]
    #build_min_heap(heap)
    heap = heap_sort(heap)
    print(heap)

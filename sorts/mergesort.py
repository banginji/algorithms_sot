import math


def msort(arr):
    if len(arr) <= 1:
        return arr
    else:
        midpoint = math.ceil(len(arr)/2)
        return merge(msort(arr[:midpoint]), msort(arr[midpoint:]))


def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    else:
        return a[:1]+merge(a[1:], b) if a[0]<b[0] else b[:1]+merge(a, b[1:])


if __name__ == '__main__':
    print(msort([23, 54, 12, 56, 325, 134, 235, 769, 2342, 785, 2422, 76, 23, 7, 2, 745]))
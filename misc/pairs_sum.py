def pairs(arr, sum):
    # checked_array = [0 for i in range(len(arr))]
    pairs_tuples = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j] == sum:
                pairs_tuples.append({i, j})
    return pairs_tuples


if __name__ == '__main__':
    print(pairs([34, 23, 1234], 57))
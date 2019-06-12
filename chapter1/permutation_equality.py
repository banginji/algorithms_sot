from sorts import quicksort as qs


def is_perm_equal(input1, input2):
    return qs.qsort_alt(input1) == qs.qsort_alt(input2)


if __name__ == '__main__':
    print(is_perm_equal("apple", "papel"), end="")

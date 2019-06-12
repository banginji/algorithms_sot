def str_contains_str(str1, str2):
    len_str1 = len_string(str1)
    len_str2 = len_string(str2)

    if len_str1 < len_str2:
        longer_str = str2
        shorter_str = str1
    else:
        longer_str = str1
        shorter_str = str2

    shorter_idx, longer_idx = 0, 0

    for longer_idx in range(len_string(longer_str)):
        if shorter_str[shorter_idx] is longer_str[longer_idx]:
            for shorter_idx in range(len_string(shorter_str)):
                if shorter_str[shorter_idx] is not longer_str[longer_idx]:
                    return False
                longer_idx += 1
            return True
    return False


def len_string(str):
    _len = 0
    while str[_len: _len+1]:
        _len += 1
    return _len


if __name__ == '__main__':
    print(str_contains_str("pabeabc", "abc"))

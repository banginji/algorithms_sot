from sorts import mergesort as ms


# Proper implementation
def is_perm_pal(str):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    odd = 0
    for char in str:
        char_val = get_char_val(char)
        if char_val != -1:
            table[char_val] += 1
            if table[char_val] % 2:
                odd += 1
            else:
                odd -= 1

    return odd <= 1


def get_char_val(char):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    char_val = ord(char)

    if a <= char_val <= z:
        return char_val - a
    elif A <= char_val <= Z:
        return char_val - A
    else:
        return -1


# Custom implementation - no need to check
def is_perm_palindrome(str):
    chance = False
    sorted_string = ms.msort(str.lower())
    sorted_string = ''.join(x if x != ' ' else '' for x in sorted_string)
    print(sorted_string)

    idx = 0
    # print(len(sorted_string), end=" len\n")
    while idx < len(sorted_string):
        # print(idx, end="\n")
        if idx == len(sorted_string) - 1 and chance:
            return False
        elif idx == len(sorted_string) - 1 and not chance:
            return True
        if sorted_string[idx] != sorted_string[idx+1]:
            if not chance:
                chance = True
                idx += 1
                continue
            if chance:
                return False
        idx += 2
    return True


def iterate_string(seq, step):
    idx = 0
    for elem in seq:
        yield idx, elem
        idx += step


if __name__ == '__main__':
    # print(is_perm_palindrome("Tact Coab"))
    # print(is_perm_palindrome("Able was I ere xI saw Elba"))
    # print(is_perm_palindrome("jhsabckj hjsbckj"))
    print(is_perm_palindrome("malayalam"))
    # print(is_perm_pal("si s"))

def url_encoded(str):
    return ''.join(x if x != ' ' else '%20' for x in str)


if __name__ == '__main__':
    print(url_encoded("a b c"))

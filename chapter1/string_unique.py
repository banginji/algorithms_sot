# put string into set and check length
def is_unique(string):
    return len(set(string)) == len(string)


if __name__ == '__main__':
    print(is_unique("kjangasfad"), end="\n")

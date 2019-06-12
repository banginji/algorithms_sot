from collections import Counter


def func(sentence, words):
    words_in_sentence = sentence.split()
    idx1, idx2 = 0, 0
    while idx1 < len(words):
        while idx2 < len(words_in_sentence):
            if words[idx1] == words_in_sentence[idx2]:
                words_in_sentence.remove(words_in_sentence[idx2])
                # idx2 -= 1
            else:
                idx2 += 1
        idx1 += 1
        idx2 = 0

    metadata = {word:words_in_sentence.count(word) for word in words_in_sentence}
    # word, word_count = [metadata.keys()], metadata.values()
    # print(f"{[w for w in metadata.keys()]}, {word_count}")
    # print(metadata.keys()[:2])
    metadata = {word:words_in_sentence.count(word) for word in words_in_sentence}
    return [w for w in metadata.keys()][:2]


def reorder(number, log_lines):
    word_lines = []
    number_lines = []
    for line in log_lines:
        words_in_sentence = line.split()
        if words_in_sentence[1].isalpha():
            word_lines.append(line)
        else:
            number_lines.append(line)
    print(f"{word_lines}, {number_lines}")
    buffer = []
    for w in word_lines:
        buffer.append(w.split()[1])
    print(buffer)
    buffer = sorted(buffer)
    print(buffer)
    result_list = []
    for _s in buffer:
        for w in word_lines:
            if _s == w.split()[1]:
                result_list.append(w)
    for n in number_lines:
        result_list.append(n)
    # return result_list
    print(result_list)


def buffer(literatureText, wordsToExclude):
    words_in_sentence = literatureText.split()
    idx1, idx2 = 0, 0
    while idx1 < len(wordsToExclude):
        while idx2 < len(words_in_sentence):
            if wordsToExclude[idx1] == words_in_sentence[idx2]:
                words_in_sentence.remove(words_in_sentence[idx2])
            else:
                idx2 += 1
        idx1 += 1
        idx2 = 0

    metadata = {word: words_in_sentence.count(word) for word in words_in_sentence}
    return [w for w in metadata.keys()][:2]


def correct_one(sentence, words):
    words_after_removal = [w for w in sentence.split() if w not in words]
    return list({w:words_after_removal.count(w) for w in words_after_removal}.keys())[:2]


def correct_one_using_counter(sentence, words):
    words_after_removal = [w for w in sentence.split() if w not in words]
    word_count = Counter(words_after_removal)
    for word, count in word_count.most_common():
        print(f"{word}, {count}")
    return word_count.most_common(2)


def correct_two(sentences):
    word_lines = []
    number_lines = []
    for line in sentences:
        words_in_sentence = line.split()
        if words_in_sentence[1].isalpha():
            word_lines.append(line)
        else:
            number_lines.append(line)

    result_list = sorted(word_lines, key=lambda sentence: sentence.split()[1])
    result_list.extend(number_lines)
    return result_list


def check_one(sentence, words):
    words_after_removal = [w for w in sentence.split() if w not in words]
    print(list({w: words_after_removal.count(w) for w in words_after_removal}.keys())[:2])


if __name__ == '__main__':
   # print(buffer("hi there hi hi three three", ["there"]))
   #  reorder(5, ["3d zab efe d", "2f2 kjn efgw wef", "3r 3 46 6", "34f 3 35 462"])
   # print(correct_one("hi there hi hi three three", ["there"]))
   # print(correct_two(["3d zab efe d", "2f2 kjn efgw wef", "3r 3 46 6", "34f 3 35 462"]))
   # print(correct_one_using_counter("hi there hi hi three three", ["there"]))
   check_one("hi there hi hi three three", ["there"])
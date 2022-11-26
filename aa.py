import re


def rec_aa(word, new_word, idx, replacement=True):
    length = len(word)
    len_new = len(new_word)

    if word[:idx] < new_word[:idx]:
        # print(f'old word slice: {word[:idx]}, new word slice: {new_word[:idx]}')
        return new_word
    elif word[:idx] == new_word[:idx]:
        # print(f'middle here - old word: {word}, new word: {new_word}')
        while word[idx - 1] == new_word[idx - 1] and idx < min(length, len_new):
            idx += 1
        if word[idx - 1] < new_word[idx - 1] or (word[idx - 1] == new_word[idx - 1] and length <= len_new):
            return new_word
        elif replacement:
            # print(f'(fun in rec_aa) old: {word[:idx]}, new: {new_word[:idx]}')
            idx = min(len_new, idx + 1)
            aa_positions = [(j, j + 2) for j in range(idx - 2, -1, -1) if new_word[j:j + 2] == "aa"]
            for start, end in aa_positions:
                new_word = new_word[:start] + "zz" + new_word[end:]
                result = rec_aa(word, new_word, idx, replacement=False)
                if result is not None:
                    # print(f'(in rec_aa) old: {w}, new: {resulting}')
                    return result
                else:
                    new_word = new_word[:start] + "aa" + new_word[end:]

            for start, end in aa_positions:
                new_word = new_word[:start] + "zz" + new_word[end:]
                result = rec_aa(word, new_word, idx)
                if result is not None:
                    # print(f'(in rec_aa) old: {w}, new: {resulting}')
                    return result
                else:
                    new_word = new_word[:start] + "aa" + new_word[end:]
    elif replacement:
        idx = min(len_new, idx + 1)
        aa_positions = [(j, j + 2) for j in range(idx - 2, -1, -1) if new_word[j:j + 2] == "aa"]
        for start, end in aa_positions:
            new_word = new_word[:start] + "zz" + new_word[end:]
            result = rec_aa(word, new_word, idx, replacement=False)
            if result is not None:
                # print(f'(in rec_aa) old: {w}, new: {resulting}')
                return result
            else:
                new_word = new_word[:start] + "aa" + new_word[end:]

        for start, end in aa_positions:
            new_word = new_word[:start] + "zz" + new_word[end:]
            result = rec_aa(word, new_word, idx)
            if result is not None:
                # print(f'(in rec_aa) old: {w}, new: {resulting}')
                return result
            else:
                new_word = new_word[:start] + "aa" + new_word[end:]

    return None


"""
def rec_aa(word, new_word):
    len_new = len(new_word)

    if word <= new_word:
        return new_word
    else:
        aa_positions = [(j, j + 2) for j in range(len_new - 2, -1, -1) if new_word[j:j + 2] == "aa"]
        for start, end in aa_positions:
            new_word = new_word[:start] + "zz" + new_word[end:]
            result = rec_aa(word, new_word)
            if result is not None:
                return result
            else:
                new_word = new_word[:start] + "aa" + new_word[end:]

    return None"""


n = int(input())

can_be_sorted = True
w = 'a'
index = 1
orderable = True

for i in range(n):
    if orderable:
        new = input()
        resulting = rec_aa(w, new, index)
        if resulting is not None:
            # print(f'old: {w}, new: {resulting}')
            w = resulting
        else:
            orderable = False
    else:
        continue

print("yes" if orderable else "no")

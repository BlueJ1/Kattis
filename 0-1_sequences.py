def swaps(zeros, ones):
    n_swaps = 0
    n_z = len(zeros)
    for i in range(n_z):
        n_swaps += zeros[i] - i
    for i in range(len(ones)):
        n_swaps += (n_z + i) - ones[i]

    return n_swaps


def rec_f(qmarks: list, zeros: list, ones: list):
    if len(qmarks) == 0:
        n_swaps = swaps(sorted(zeros), sorted(ones))
        return n_swaps

    zeros.append(qmarks[0])
    n_swaps = rec_f(qmarks[1:], zeros, ones)
    zeros.pop()
    ones.append(qmarks[0])
    n_swaps += rec_f(qmarks[1:], zeros, ones)
    ones.pop()
    return n_swaps


sequence = []
zeros, ones, qmarks = [], [], []
i = 0
for c in input():
    if c == '0':
        zeros.append(i)
    elif c == '1':
        ones.append(i)
    else:
        qmarks.append(i)

    i += 1

print(rec_f(qmarks, zeros, ones) // 2)

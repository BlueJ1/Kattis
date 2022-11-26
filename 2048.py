# SOLVED

board = [[int(x) for x in input().split()] for _ in range(4)]
move = int(input().strip())

# 0: left
# 1: up
# 2: right
# 3: down
if move == 0:
    for i in range(4):
        all_zero = True
        for j in range(4):
            if board[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            continue

        j = 0
        n_zeros = 0
        while j < 3 - n_zeros:
            if board[i][j] == 0:
                for k in range(j, 3):
                    board[i][k] = board[i][k + 1]
                board[i][3] = 0
                n_zeros += 1
                continue
            elif board[i][j + 1] == 0:
                for k in range(j + 1, 3):
                    board[i][k] = board[i][k + 1]
                board[i][3] = 0
                n_zeros += 1
                continue
            elif board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                for k in range(j + 1, 3):
                    board[i][k] = board[i][k + 1]
                board[i][3] = 0
                n_zeros += 1
            j += 1
elif move == 1:
    for j in range(4):
        all_zero = True
        for i in range(4):
            if board[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            continue

        i = 0
        n_zeros = 0
        while i < 3 - n_zeros:
            if board[i][j] == 0:
                for k in range(i, 3):
                    board[k][j] = board[k + 1][j]
                board[3][j] = 0
                n_zeros += 1
                continue
            if board[i + 1][j] == 0:
                for k in range(i + 1, 3):
                    board[k][j] = board[k + 1][j]
                board[3][j] = 0
                n_zeros += 1
                continue
            if board[i][j] == board[i + 1][j]:
                board[i][j] *= 2
                for k in range(i + 1, 3):
                    board[k][j] = board[k + 1][j]
                board[3][j] = 0
                n_zeros += 1
            i += 1
elif move == 2:
    for i in range(4):
        all_zero = True
        for j in range(4):
            if board[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            continue

        j = 3
        n_zeros = 0
        while j > n_zeros:
            if board[i][j] == 0:
                for k in range(j, 0, -1):
                    board[i][k] = board[i][k - 1]
                board[i][0] = 0
                n_zeros += 1
                continue
            if board[i][j - 1] == 0:
                for k in range(j - 1, 0, -1):
                    board[i][k] = board[i][k - 1]
                board[i][0] = 0
                n_zeros += 1
                continue
            if board[i][j] == board[i][j - 1]:
                board[i][j] *= 2
                for k in range(j - 1, 0, -1):
                    board[i][k] = board[i][k - 1]
                board[i][0] = 0
                n_zeros += 1
            j -= 1
elif move == 3:
    for j in range(4):
        all_zero = True
        for i in range(4):
            if board[i][j] != 0:
                all_zero = False
                break
        if all_zero:
            continue

        i = 3
        n_zeros = 0
        while i > n_zeros:
            if board[i][j] == 0:
                for k in range(i, 0, -1):
                    board[k][j] = board[k - 1][j]
                board[0][j] = 0
                n_zeros += 1
                continue
            if board[i - 1][j] == 0:
                for k in range(i - 1, 0, -1):
                    board[k][j] = board[k - 1][j]
                board[0][j] = 0
                n_zeros += 1
                continue
            if board[i][j] == board[i - 1][j]:
                board[i][j] *= 2
                for k in range(i - 1, 0, -1):
                    board[k][j] = board[k - 1][j]
                board[0][j] = 0
                n_zeros += 1
            i -= 1

# print(board)

for i in range(4):
    for j in range(3):
        print(board[i][j], end=' ')
    print(board[i][3])

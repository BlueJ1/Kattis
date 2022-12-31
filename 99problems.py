(lambda N: (print(N - N % 100 - 1) if N > 100 else print(99)) if N % 100 < 49 else print(N - N % 100 + 99))(int(input()))

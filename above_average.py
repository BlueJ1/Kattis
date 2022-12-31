[(lambda grades: print(f'{(sum([1 if grade > sum(grades) / len(grades) else 0 for grade in grades]) / len(grades)) * 100:.3f}%'))([int(c) for c in input().split()[1:]]) for _ in range(int(input()))]

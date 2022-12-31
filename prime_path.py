from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if not number % i:
            return False
    return True


n = int(input())

for _ in range(n):
    n_steps = 0
    t = input().split
    start, goal = int(t()[0]), int(t()[1])
    discovered = [start]
    frontier = [start]
    while goal not in frontier:
        new_frontier = []
        for prime in frontier:
            for i in range(1, 10):
                new_n = i * 1000 + prime % 1000
                if new_n != prime and is_prime(new_n) and new_n not in discovered:
                    discovered.append(new_n)
                    new_frontier.append(new_n)
            for i in range(10):
                new_n = i * 100 + prime % 100 + 1000 * (prime // 1000)
                if new_n != prime and is_prime(new_n) and new_n not in discovered:
                    discovered.append(new_n)
                    new_frontier.append(new_n)
            for i in range(10):
                new_n = i * 10 + prime % 10 + 100 * (prime // 100)
                if new_n != prime and is_prime(new_n) and new_n not in discovered:
                    discovered.append(new_n)
                    new_frontier.append(new_n)
            for i in range(10):
                new_n = i + prime - prime % 10
                if new_n != prime and is_prime(new_n) and new_n not in discovered:
                    discovered.append(new_n)
                    new_frontier.append(new_n)
        frontier = new_frontier
        n_steps += 1
        if len(frontier) == 0:
            break
    if len(frontier) == 0:
        print("Impossible")
    else:
        print(n_steps)

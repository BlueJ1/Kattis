(lambda integers: [print(sorted(integers)[ord(c) - ord("A")], end=" ") for c in input()])([int(c) for c in input().split()])

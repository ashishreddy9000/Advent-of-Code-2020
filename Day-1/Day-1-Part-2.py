from itertools import combinations
from math import prod

file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-1/Day-1-Input.txt", 'r')
content = list(map(int, (file.read().strip().split("\n"))))
ans = combinations(content,3)
for x in ans:
    if sum(x) == 2020:
        print(x)
        print(prod(x))

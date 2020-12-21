from itertools import combinations

file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-9/Day-9-Input.txt", 'r')
content = list(map(int, (file.read().strip().split('\n'))))
global break_number

for x in range(0, len(content) - 25):
    temp = content[x:x+25]
    combination_list = combinations(temp, 2)
    possible_sums = []
    for i,j in combination_list:
        possible_sums.append(i+j)
    if content[x+25] not in possible_sums:
        break_number = content[x+25]
        break
print(break_number)
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
condition = 0
x = 0
while condition == 0:
    ans = 0
    i = x
    buffer = []
    while ans <= break_number:
        buffer.append(content[i])
        ans = sum(buffer)
        i+=1
        if ans == break_number:
            print(buffer)
            print(min(buffer) + max(buffer))
            condition = 1
            break
    x+=1
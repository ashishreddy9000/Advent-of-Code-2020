from math import prod

ans = []
def slope(a,b):
    y = a
    trees = 0
    length = len(nested_content[0])
    for x in range(b, len(nested_content), b):
        if nested_content[x][y] == '#':
            trees+=1
        k = y + a
        if k - length >= 0:
            y = k -length
        else:
            y = k
    ans.append(trees)

file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-3/Day-3-Input.txt", 'r')
content = list(map(str, (file.read().strip().split("\n"))))
nested_content = []
for x in content:
    nested_content.append(list(x))

slope(1,1)
slope(3,1)
slope(5,1)
slope(7,1)
slope(1,2)

print(ans)
print(prod(ans))
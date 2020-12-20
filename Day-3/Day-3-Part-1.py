file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-3/Day-3-Input.txt", 'r')
content = list(map(str, (file.read().strip().split("\n"))))
nested_content = []
for x in content:
    nested_content.append(list(x))
y = 3
trees = 0
length = len(nested_content[0])
for x in range(1, len(nested_content)):
    if nested_content[x][y] == '#':
        trees+=1
    k = y + 3
    if k - length == 1:
        y = 1
    elif k - length == 2:
        y = 2
    elif k - length == 3:
        y = 3
    elif k - length == 0:
        y = 0
    else:
        y = k
print(trees)
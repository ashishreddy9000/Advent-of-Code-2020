file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-10/Day-10-Input.txt", 'r')
content = list(map(int, (file.read().strip().split('\n'))))
content.sort()
content.append(content[-1]+3)
content.insert(0,0)
no_of_ones = 0
no_of_threes = 0
for x in range(0, len(content)-1):
    diff = content[x+1] - content[x]
    if diff == 1:
        no_of_ones+=1
    elif diff == 3:
        no_of_threes+=1
print(no_of_ones*no_of_threes)
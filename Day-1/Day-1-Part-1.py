file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-1/Day-1-Input.txt", 'r')
content = list(map(int, (file.read().strip().split("\n"))))
i = 0
j = 199
content.sort()
while i<j:
    temp = content[i] + content[j]
    if temp < 2020:
        i+=1
    elif temp == 2020:
        print(str(content[i]) + ' ' + str(content[j]))
        print(content[i]*content[j])
        break
    elif temp > 2020:
        j-=1

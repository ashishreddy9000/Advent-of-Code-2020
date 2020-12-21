file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-8/Day-8-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n'))))
commands = []
accumulator = 0
for x in content:
    commands.append(x.split())
x = 0
x_list = []
while x < len(commands):
    x_list.append(x)
    if commands[x][0] == 'nop':
        x+=1
    elif commands[x][0] == 'acc':
        k = int(commands[x][1])
        accumulator = accumulator + k
        x+=1
    elif commands[x][0] == 'jmp':
        k = int(commands[x][1])
        x = x + k
    if x in x_list:
        print(accumulator)
        break
file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-8/Day-8-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n'))))
commands = []
accumulator = 0
for x in content:
    commands.append(x.split())
x = 0
x_list = []
log = []
while x < len(commands):
    k = int(commands[x][1])
    x_list.append(x)
    if commands[x][0] == 'nop':
        log.append(x)
        x+=1
    elif commands[x][0] == 'acc':
        accumulator = accumulator + k
        x+=1
    elif commands[x][0] == 'jmp':
        log.append(x)
        x = x + k
    if x in x_list:
        break
log.sort()
for a in log:
    accumulator = 0
    identifier = 1
    x = 0
    x_list = []
    if commands[a][0] == 'nop':
        commands[a][0] = 'jmp'
    elif commands[a][0] == 'jmp':
        commands[a][0] = 'nop'
    while x < len(commands):
        k = int(commands[x][1])
        x_list.append(x)
        if commands[x][0] == 'nop':
            x+=1
        elif commands[x][0] == 'acc':
            accumulator = accumulator + k
            x+=1
        elif commands[x][0] == 'jmp':
            x = x + k
        if x in x_list:
            identifier = 0
            break
    if identifier == 1:
        print(accumulator)
    if commands[a][0] == 'jmp':
        commands[a][0] = 'nop'
    elif commands[a][0] == 'nop':
        commands[a][0] = 'jmp'
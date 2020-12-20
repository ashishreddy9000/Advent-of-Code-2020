file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-5/Day-5-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n'))))
seat_ids = []
for x in content:
    l_range = 0
    u_range = 127
    c_l_range = 0
    c_u_range = 7
    while l_range != u_range:
        for y in x:
            if y == 'F':
                u_range = (l_range + u_range - 1) // 2
            elif y == 'B':
                l_range = (l_range + u_range + 1) // 2
            elif y == 'L':
                c_u_range = (c_l_range + c_u_range - 1) // 2
            elif y == 'R':
                c_l_range = (c_l_range + c_u_range + 1) // 2
    seat_ids.append(l_range * 8 + c_l_range)
print(max(seat_ids))
file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-4/Day-4-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n\n'))))
validated = 0
for x in content:
    passport_distorted = x.split('\n')
    passport = []
    present_fields = []
    for y in passport_distorted:
        k = y.split()
        for z in k:
            passport.append(z)
    for y in passport:
        k = y.split(':')
        present_fields.append(k[0])
    if len(present_fields) == 8:
        validated+=1
    elif len(present_fields) == 7:
        if 'cid' not in present_fields:
            validated+=1
print(validated)
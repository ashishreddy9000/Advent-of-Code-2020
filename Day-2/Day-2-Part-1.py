file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-2/Day-2-Input.txt", 'r')
content = list(map(str, (file.read().strip().split("\n"))))
correct = 0
for x in content:
    lower_limit = int(x.split('-',1)[0])
    upper_limit = int(((x.split('-')[1]).split(' ',1))[0])
    key_letter = ((((x.split('-')[1]).split(' ',1))[1]).split(':',1))[0]
    password = (list(((((x.split('-')[1]).split(' ',1))[1]).split(':',1))[1]))
    password.pop(0)
    temp_counter = 0
    for y in password:
        if y == key_letter:
            temp_counter+=1
    if temp_counter >= lower_limit and temp_counter <= upper_limit:
        correct+=1
print(correct)
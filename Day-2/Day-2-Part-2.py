file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-2/Day-2-Input.txt", 'r')
content = list(map(str, (file.read().strip().split("\n"))))
correct = 0
for x in content:
    lower_limit = int(x.split('-',1)[0])-1
    upper_limit = int(((x.split('-')[1]).split(' ',1))[0])-1
    key_letter = ((((x.split('-')[1]).split(' ',1))[1]).split(':',1))[0]
    password = (list(((((x.split('-')[1]).split(' ',1))[1]).split(':',1))[1]))
    password.pop(0)
    if (password[lower_limit] == key_letter and password[upper_limit] == key_letter):
        pass
    elif (password[lower_limit] == key_letter or password[upper_limit] == key_letter):
        correct+=1
    else:
        pass
print(correct)
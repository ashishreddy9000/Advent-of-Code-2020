from collections import Counter

file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-6/Day-6-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n\n'))))
sum_of_yes = 0
for x in content:
    split_x = x.split('\n')
    all_answers = ''
    for y in split_x:
        all_answers+=y
    no_of_yes = len(dict(Counter(list(all_answers))))
    sum_of_yes+=no_of_yes
print(sum_of_yes)
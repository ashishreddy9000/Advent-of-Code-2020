from collections import Counter

file = open("/home/ashishreddy9000/Documents/Advent-of-Code-2020/Day-6/Day-6-Input.txt", 'r')
content = list(map(str, (file.read().strip().split('\n\n'))))
sum_of_yes = 0
for x in content:
    split_x = x.split('\n')
    length = len(split_x)
    if length == 1:
        sum_of_yes+=len(list(split_x[0]))
    else:
        all_answers = ''
        for y in split_x:
            all_answers+=y
        counter_dict = dict(Counter(list(all_answers)))
        for i,j in counter_dict.items():
            if j == length:
                sum_of_yes+=1
print(sum_of_yes)
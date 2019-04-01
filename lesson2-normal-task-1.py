list_number = [2, -5, 8, 9, -25, 25, 4]
list_new = []
for _ in range(len(list_number)):
    if type(pow(list_number[_], 0.5)) is float and pow(list_number[_], 0.5) % 1 == 0:
        list_new.append(int(pow(list_number[_], 0.5)))
print(list_new)
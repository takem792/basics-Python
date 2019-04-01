list_random = [-16, 10, 23, 24, 11, 4, 16]
list_new = []
for _ in range(len(list_random)):
    if list_random[_] % 2 == 0:
        list_new.append(list_random[_] / 4)
    else:
        list_new.append(list_random[_] *2)
print(list_new)
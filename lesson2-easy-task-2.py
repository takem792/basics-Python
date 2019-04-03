list_rand_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_rand_2 = [2, 4, 8]
for _ in range(len(list_rand_2)):
    while True:
        if list_rand_2[_] in list_rand_1:
            list_rand_1.remove(list_rand_2[_])
        else:
            break
print(list_rand_1)
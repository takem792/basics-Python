import random
length_list = int(input('Введите кол-во элементов списка ->'))
list_random = []
for _ in range(length_list):
    list_random.append(random.randint(-100, 100))
print(list_random)
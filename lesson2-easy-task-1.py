list_fruit = ["яблоко", "банан", "киви", "арбуз"]
len_world = 0
for _ in range(len(list_fruit)):
    if len_world < len(list_fruit[_]):
        len_world = len(list_fruit[_])

for _ in range(len(list_fruit)):
    print(_+1, list_fruit[_].rjust(len_world+1))
    _ += 1
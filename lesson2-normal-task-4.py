lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst.sort()
lst2 = [lst[0]]
for _ in range(1, len(lst)):
    if lst[_] != lst[_ - 1]:
        lst2.append(lst[_])
print(lst2)
lst3 = []
for _ in range(len(lst)):
    if lst.count(lst[_]) == 1:
        lst3.append(lst[_])
print(lst3)
# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_len(*args):
    '''
    Как и в предыдущем можно решить несколькими способами, исхожу из задачи (просили фунцуию)
    '''
    return max(*args, key=len)


list_1 = 'eeee'
list_2 = 're'
list_3 = 'fwefwefwe'
list_4 = 'fwef'
print('Самая длинная строка - ', max_len(list_1, list_2, list_3, list_4))

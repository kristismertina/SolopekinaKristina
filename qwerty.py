num = [1, 11, 111]
lst = []
if len(num) > 0:
    for i in num:
        if len(num) % 2 == 0:
            break
        else:
            lst.append(i)
            print(lst)
else:
    print('Список пуст')


woman_name_dict = {'man_1': "Вася", 'man_2': "Петя", 'woman_1': "Ольга", 'woman_2': "Елена", 'woman_3': "Екатерина"}
for key in woman_name_dict:
    if key[0:4] == 'woman':
        print(woman_name_dict)


element = [1, 7, -9, 5, -8, 0]
element.remove(0)


element_new = [i**2 for i in element if i < 0]
element.insert()
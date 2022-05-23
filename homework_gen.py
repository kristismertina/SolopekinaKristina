# 1 задача

name = ["Вася", "Петя", "Ольга", "Елена", "Екатерина"]
print(name[2:])

women_name = [i for i in name if i[-1] == "а"]
print(women_name)

# 2 задача
a = ['11', '1111', '111', '345', '5677']
a_new = [i for i in a if len(i) == 1 or len(i) % 3 == 0]
print(a_new)

exem = [i for i in range(1, 1000, 100)]
print(exem)

exem_1 = [i * 100 for i in range(1, 10)]
print(exem_1)

# доп задача №3
el = [1, 2, 34, -12, 45, -46]
elem_negative = [i for i in el if i < 0]
elem_positive = [i for i in el if i > 0]
print('Положительные:', elem_positive, 'Отрицательные:', elem_negative)






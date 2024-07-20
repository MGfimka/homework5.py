# Задайте переменные разных типов данных:
immutable_var = 1, 2, 3, 4
print(immutable_var)
immutable_var_2 = ('car1', 'car2', 'car3', 'car4')
print(immutable_var_2)
immutable_var_3 = tuple([1, 2, 'car3', 'car4'])
print(immutable_var_3)

# Изменение значений переменных:
immutable_var = 1, 2, 3, 'Falce', 'string'
print(immutable_var)
immutable_var[0] = 150
print(immutable_var) #кортеж не поддерживает обращение по элементам

#Создание изменяемых структур данных:
mutable_list = ([1, 2, 3], 6, 5, 4)
print(mutable_list)
mutable_list[0][0] = 7
print(mutable_list)
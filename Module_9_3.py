# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для первой задачи
first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))

# Генераторная сборка для второй задачи
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))
print(list(second_result))

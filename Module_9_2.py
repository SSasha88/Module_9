print('"Списковые, словарные сборки"')
print()
# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая часть: Список длин строк >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Вторая часть: Пары строк одинаковой длины
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Третья часть: Словарь строк с четной длиной
all_strings = first_strings + second_strings
third_result = {s: len(s) for s in all_strings if len(s) % 2 == 0}

# Вывод результатов
print("first_result:", first_result)
print("second_result:", second_result)
print("third_result:", third_result)

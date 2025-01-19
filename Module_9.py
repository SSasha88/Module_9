print('Задача "Вызов разом"')

def apply_all_func(int_list, *functions):
    #Создаю пустой словарь для хранения результатов
    results = {}
    # Перебираю все функции из *functions
    for func in functions:
        # Вызываю текущую функцию с аргументом int_list
        result = func(int_list)
        # Сохраняю результат в словарь под ключом имени функции
        results[func.__name__] = result
    return results
# Пример вызова функции с двумя функциями
print(apply_all_func([6, 20, 15, 9], max, min))
# Пример вызова функции с тремя функциями
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

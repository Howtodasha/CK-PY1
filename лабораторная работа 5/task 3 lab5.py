from random import randint
def get_unique_list_numbers() -> list[int]:
    

    size = 15
    list_unique = []
    while len(list_unique) != size:
        key = randint(-10,10)
        if key not in list_unique:
            list_unique.append(key)
    return list_unique


    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

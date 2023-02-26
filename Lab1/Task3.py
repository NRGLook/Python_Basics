def even_list(list_of_nums):
    return [num for num in list_of_nums if num % 2 == 0]


print(even_list([num for num in range(1, 100)]))

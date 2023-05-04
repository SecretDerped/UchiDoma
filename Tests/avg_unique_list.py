def get_avg_unique_lists(lst1, lst2):
    '''
    Принимает два списка чисел и возвращает среднее арифметическое
    только тех чисел, которые встречаются в каждом из списков только один раз.

    >>> get_avg_unique_lists([1, 1, 1, 2, 3, 3, 4, 5, 5], [1, 1, 2, 3, 5, 6, 7, 7])
    3.7
    >>> get_avg_unique_lists([1, 2], [1, 2])
    1.5
    '''
    numbers1 = dict()
    numbers2 = dict()
    for num in lst1:
        if num not in numbers1:
            numbers1[num] = 1
        else:
            numbers1[num] += 1
    for num in lst2:
        if num not in numbers2:
            numbers2[num] = 1
        else:
            numbers2[num] += 1
    unique1 = [key for key in numbers1 if numbers1[key] == 1]
    unique2 = [key for key in numbers2 if numbers2[key] == 1]
    unique = unique1 + unique2
    if not unique:
        return 0
    return round(sum(unique) / len(unique), 1)


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(get_avg_unique_lists(lst1, lst2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

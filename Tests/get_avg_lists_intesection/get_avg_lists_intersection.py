def get_avg_lists_intersection(lst1, lst2):
    intersection = set(lst1).intersection(lst2)
    numbers = []
    for el in lst1 + lst2:
        if el in intersection:
            numbers.append(el)
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 1)

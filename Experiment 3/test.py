list = [(1, 2), (3, 1), (4, 1), (2, 3), (5, 1)]
list.sort(key=lambda x: x[1])
print(list)
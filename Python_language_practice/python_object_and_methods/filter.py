items = [("product 1", 10), ("product 2", 19), ("product 3", 9)]
print(items)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

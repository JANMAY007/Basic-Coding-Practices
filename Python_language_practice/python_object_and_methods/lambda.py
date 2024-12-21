items = [("product 1", 10), ("product 2", 19), ("product 3", 9)]
print(items)
'''
def sort_items(item):
    return item[1]
'''
# for not declaring above function lambda is used
items.sort(key=lambda item: item[1])
print(items)

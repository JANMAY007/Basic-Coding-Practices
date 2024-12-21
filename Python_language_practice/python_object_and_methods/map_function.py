items = [("product 1", 10), ("product 2", 19), ("product 3", 9)]
prices = map(lambda item1: item[1], items)
print(prices)
for item in prices:
    print(item)
price = list(map(lambda item2: item[1], items))
print(price)

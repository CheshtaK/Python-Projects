stock = {'apple': [10, 20, 5],
         'banana': [20, 15, 10],
         'pear': [5, 30, 20]}

print("Unsorted")
for item in stock:
    print(item, ": ", stock[item])


print("\nSorted List -- Ascending")
for item in stock:
    stock[item].sort()
    print(item, ": ", stock[item])

print("\nSorted List -- Descending")
for item in stock:
    stock[item].sort(reverse=True)
    print(item, ": ", stock[item])

print("\nSort by key")
for item in sorted(stock, key=stock.get, reverse=False):
    print(item, ": ", stock[item])

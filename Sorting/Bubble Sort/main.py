# Bubble Sort (Ascending)
# Compares consecutive items 
# then swap if the next item is greated than the previous item

items = [32,67,11,7,23,7,42]
isOrdered = False

print("Unordered items: " + str(items))

while not isOrdered:
  isOrdered = True
  for x in range(len(items) - 1):
    if items[x] > items[x + 1]:
      temp = items[x]
      items[x] = items[x + 1]
      items[x + 1] = temp
      isOrdered = False

print("Ordered items: " + str(items))
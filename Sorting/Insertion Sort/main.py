# Insertion Sort
# Compares n and n+1 element
# Then swap if n > n+1
# After that, the process it will iterate from the top again

items = [7,6,5,4,3,2,1]
isOrdered = False

while not isOrdered:
  isOrdered = True
  for x in range(len(items) - 1):
    if items[x] > items[x + 1]:
      temp = items[x]
      items[x] = items[x + 1]
      items[x + 1] = temp
      isOrdered = False
      break

print(items)
# Selection Sort
# Finds the index with the biggest element
# Then it swaps the element to the last index
# After that, the last index will be ignored
# Then it will loop again.

items = [4,34,87,1,65,2,8,0,23,-4,67,-67]
print(items)

def selectionSort(array):
  
  for i in range(len(array)-1, -1, -1):
    bigIndex = 0

    for j in range(i + 1):
      if array[bigIndex] < array[j]:
        bigIndex = j

    temp = array[i]
    array[i] = array[bigIndex]
    array[bigIndex] = temp

  return array

print(selectionSort(items))
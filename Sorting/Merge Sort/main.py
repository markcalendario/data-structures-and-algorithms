# Merge Sort
# Sorts an array using a recursive function
# It divides an array into half recursively until the array reaches one element
# Then it will return a sorted version of a divided array until it reaches the first caller of the function

def mergeSort(array):
  arrayLength = len(array)
  left = array[:arrayLength//2] 
  right = array[arrayLength//2:]
  temporaryArray = []
  
  if len(left) > 1:
    for item in mergeSort(left):
      temporaryArray.append(item)
  else:
    temporaryArray.append(left[0])

  if len(right) > 1:
    for item in mergeSort(right):
      temporaryArray.append(item)
  else:
    temporaryArray.append(right[0])

  ok = False
  while not ok:
    ok = True
    for i in range(len(temporaryArray) - 1):
      if temporaryArray[i] > temporaryArray[i + 1]:
        temp = temporaryArray[i]
        temporaryArray[i] = temporaryArray[i + 1]
        temporaryArray[i + 1] = temp
        ok = False

  return temporaryArray

ar = [6,23,12,43,2,99,32,0,3,8,-763, 763, -763,87]
print("Before sorting", ar)
print("After sorting", mergeSort(ar))
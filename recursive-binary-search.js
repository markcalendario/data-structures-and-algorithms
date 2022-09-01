const { orderedList } = require("./sampleData")

let turns = 0

function binarySearch(list, target, first, last) {
  turns++

  const mid = Math.round((first + last) / 2)

  if (list[mid] === target)
    return console.log(`Target ${target} found at ${turns} turn(s).`)

  if (first > last)
    return console.log(`Target ${target} is not in the list. [${turns} turn(s)]`)

  if (list[mid] < target)
    first = mid + 1
  else
    last = mid - 1

  binarySearch(list, target, first, last)
}

binarySearch(orderedList, 2937, 0, orderedList.length - 1);
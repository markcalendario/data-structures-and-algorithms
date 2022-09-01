const { orderedList } = require("./sampleData")

function binarySearch(list, target) {
  let turns = 0
  let first = 0
  let last = list.length - 1

  while (first <= last) {
    turns++
    const mid = Math.round((first + last) / 2)

    if (list[mid] === target) {
      return console.log(`Target ${target} found at ${turns} turn(s).`)
    }

    if (list[mid] < target) {
      first = mid + 1
    } else {
      last = mid - 1
    }
  }

  return console.log(`Target ${target} is not in the list. [${turns} turns]`)
}

binarySearch(orderedList, 2937);
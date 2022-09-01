const { orderedList } = require("./sampleData");

function linearSearch(list, target) {
  let x;

  for (x = 0; x < list.length; x++) {
    if (list[x] === target)
      return console.log(`Item ${target} found at position ${x + 1} in ${x + 1} turn(s).`)
  }

  return console.log(`Target ${target} not found. [${x} turns]`)
}

linearSearch(orderedList, 2937);
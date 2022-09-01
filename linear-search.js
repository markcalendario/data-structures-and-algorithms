function linearSearch(list, target) {
  for (let x = 0; x < list.length; x++) {
    if (list[x] === target)
      return console.log(`Item ${target} found at position ${x + 1} in ${x + 1} turn(s).`)
  }

  return console.log(`Target ${target} not found. [${turns} turns]`)

}

const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

linearSearch(list, 10);
#!/usr/bin/node
let array = process.argv.slice(2);
array = array.map(Number);
if (process.argv.length <= 3) {
    console.log(0)
} else {
  array = [... new Set(array)];
  array = array.sort((a, b) => {return b - a});
  console.log(array[1]);
}

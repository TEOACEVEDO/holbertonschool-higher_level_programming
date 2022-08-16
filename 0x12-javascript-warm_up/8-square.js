#!/usr/bin/node
const INT = parseInt(process.argv[2]);

let i, j, b = process.argv[2];
if (INT) {
  for (i = 1; i <= b; i++) {
    let str = "";
    for (j = 1; j <= b; j++) {
      str += "X";
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
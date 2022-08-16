#!/usr/bin/node
const INT = parseInt(process.argv[2]);

let i, j;
if (INT) {
  for (i = 1; i <= process.argv[2]; i++) {
    let str = '';
    for (j = 1; j <= process.argv[2]; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}

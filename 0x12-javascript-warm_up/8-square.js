#!/usr/bin/node
/*
 * Prints a square
*/
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < size; y++) {
    let row = '';
    for (let z = 0; z < size; z++) row += 'X';
    console.log(row);
  }
}

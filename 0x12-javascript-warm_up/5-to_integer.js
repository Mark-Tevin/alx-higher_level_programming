#!/usr/bin/node

/*
 * prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
*/
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not anumber');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}

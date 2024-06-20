#!/usr/bin/node

// This first line specifies path to interpreter

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not anumber');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}

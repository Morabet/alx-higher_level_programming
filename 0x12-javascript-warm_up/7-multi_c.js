#!/usr/bin/node

const argv = process.argv;

const num = parseInt(argv[2]);
let i = 0;

if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Missing number of occurrences'); }

while (i < num) {
  console.log('C is fun');
  i++;
}

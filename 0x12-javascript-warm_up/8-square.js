#!/usr/bin/node

const argv = process.argv;

const num = parseInt(argv[2]);
let i = 0; let j = 0;

if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Missing size'); }

for (i = 0; i < num; i++) {
  for (j = 0; j < num; j++) { process.stdout.write('X'); }
  console.log();
}

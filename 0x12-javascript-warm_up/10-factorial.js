#!/usr/bin/node

const argv = process.argv;

const num = parseInt(argv[2]);

function fac (i) {
  if (isNaN(i) || i === 1) { return (1); } else { return i * fac(i - 1); }
}

console.log(fac(num));

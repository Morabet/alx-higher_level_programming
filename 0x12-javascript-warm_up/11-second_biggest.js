#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 2) {
  console.log(0);
} else {
  const arr = argv.slice(2).map(n => parseInt(n));
  arr.sort((a, b) => b - a);

  console.log(arr[1]);
}

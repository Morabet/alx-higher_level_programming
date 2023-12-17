#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const arr = argv.slice(2).map(n => parseInt(n));
  const sec = arr.sort((a, b) => b - a)[1];

  console.log(sec);
}

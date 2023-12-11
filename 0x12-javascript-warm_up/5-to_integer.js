#!/usr/bin/node

const argv = process.argv;

const num = Math.floor(Number(argv[2]));


if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Not a number'); } else { console.log(`My number: ${num}`); }

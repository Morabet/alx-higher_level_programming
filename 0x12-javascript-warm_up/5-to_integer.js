#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);

// console.log(number);

if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Not a number'); } else { console.log(`My number: ${num}`); }

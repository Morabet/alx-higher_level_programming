#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(process.argv[2]) || typeof process.argv[2] === 'undefined') { console.log('Not a number'); } else { console.log(`My number: ${num}`); }

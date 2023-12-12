#!/usr/bin/node

const dict = require('./101-data').dict;

const sorted = {};

Object.getOwnPropertyNames(dict).forEach(c => {
  if (sorted[dict[c]] === undefined) { sorted[dict[c]] = [c]; } else { sorted[dict[c]].push(c); }
});

console.log(sorted);

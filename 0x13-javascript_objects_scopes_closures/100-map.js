#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((val, idx) => val * idx);
console.log(list);
console.log(newList);

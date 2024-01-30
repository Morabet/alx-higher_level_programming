#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

if (argv.length >= 3) {
  fs.readFile(argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

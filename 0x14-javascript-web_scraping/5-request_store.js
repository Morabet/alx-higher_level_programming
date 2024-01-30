#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;
const fs = require('fs');

if (argv.length >= 4) {
  request.get(argv[2], 'utf8', err => {
    console.log(err);
  }).pipe(fs.createWriteStream(argv[3]));
}

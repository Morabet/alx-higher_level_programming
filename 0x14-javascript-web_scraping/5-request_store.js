#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;
const fs = require('fs');

if (argv.length >= 4) {
  request(argv[2]).pipe(fs.createWriteStream(argv[3]));
}

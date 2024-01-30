#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

if (argv.length >= 3) {
  request(argv[2], (err, response) => {
    if (err) { console.log(err); } else { console.log(`code :${response.statusCode}`); }
  });
}

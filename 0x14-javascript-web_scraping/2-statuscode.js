#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

if (argv.length >= 3) {
  request.get(argv[2], (error, response) => {
    if (error) { console.log(error.message); } else { console.log(`code :${response.statusCode}`); }
  });
}

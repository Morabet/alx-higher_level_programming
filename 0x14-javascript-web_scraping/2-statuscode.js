#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}

if (argv.length >= 3) {
  getStatusCode(argv[2]);
}

#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

if (argv.length >= 3) {
  const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error.message);
    } else {
      try {
        const start = JSON.parse(body);
        console.log(start.title);
      } catch (parseError) {
        console.error(parseError.message);
      }
    }
  });
}

#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const index = 0;
  const characters = JSON.parse(body).characters;
  printCharcter(characters, index);
});

const printCharcter = function (url, i) {
  request(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printCharcter(url, i++);
    }
  });
};

#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

const filmurl = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(filmurl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

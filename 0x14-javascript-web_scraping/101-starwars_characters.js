#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

const film_url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(film_url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (characters.length === index) return;
  request(characters[index], (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
}

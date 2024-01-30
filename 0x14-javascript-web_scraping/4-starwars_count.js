#!/usr/bin/node

const argv = require('process').argv;

async function getWedge (url) {
  const request = new Request(url);
  const response = await fetch(request);

  const films = await response.json();

  const wedgeid = 'https://swapi-api.alx-tools.com/api/people/18/';
  const wedgefilms = films.results.filter(film => film.characters.includes(wedgeid));

  console.log(wedgefilms.length);
}

if (argv.length >= 3) {
  getWedge(argv[2]);
}

#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const results = data.results || [];

    console.log(results.reduce((count, movie) => {
      return movie.characters && movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

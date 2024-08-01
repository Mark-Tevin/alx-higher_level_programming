#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}

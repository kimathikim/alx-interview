#!/usr/bin/node

const req = require('request');

function fetchData (url, id) {
  return new Promise((resolve, reject) => {
    req(url + id, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

function fetchCharacter (character) {
  return new Promise((resolve, reject) => {
    req(character, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body.name);
      }
    });
  });
}

fetchData('https://swapi-api.alx-tools.com/api/films/', process.argv[2])
  .then((data) => {
    const characters = data.characters;
    return Promise.all(characters.map(fetchCharacter));
  })
  .then((characterNames) => {
    for (const name of characterNames) {
      console.log(name);
    }
  })
  .catch((error) => {
    console.error(error);
  });

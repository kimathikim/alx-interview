#!/usr/bin/node

const req = require('request');

async function fetchData (url, id) {
  try {
    const body = await new Promise((resolve, reject) => {
      req(url + id, { json: true }, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    return body;
  } catch (error) {
    console.error(error);
  }
}

async function fetchCharacter (character) {
  try {
    const body = await new Promise((resolve, reject) => {
      req(character, { json: true }, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body.name);
        }
      });
    });
    console.log(body);
  } catch (error) {
    console.error(error);
  }
}

fetchData('https://swapi-api.alx-tools.com/api/films/', process.argv[2])
  .then((data) => {
    const characters = data.characters;
    characters.forEach((character) => {
      fetchCharacter(character);
    });
  })
  .catch((error) => {
    console.error(error);
  });

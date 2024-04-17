#!/usr/bin/env node

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

fetchData('https://swapi-api.alx-tools.com/api/film/', process.argv[2])
  .then((data) => {
    const characters = data.characters;
    characters.forEach((character) => {
      req(character, { json: true }, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(body.name);
        }
      });
    });
  })
  .catch((error) => {
    console.error(error);
  });

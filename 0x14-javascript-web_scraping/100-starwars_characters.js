#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (er, resp, body) {
  if (er) console.log(er);
  else {
    for (let i = 0; i < JSON.parse(body).characters.length; i++) {
      request.get(JSON.parse(body).characters[i], function (er2, resp2, body2) {
        console.log(JSON.parse(body2).name);
      });
    }
  }
});

#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (er, response, body) {
  if (er) console.log(er);
  else console.log(JSON.parse(body).title);
});

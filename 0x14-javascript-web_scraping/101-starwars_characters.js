#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function recur (array, j) {
  if (j >= array.length) return;
  request.get(array[j], function (er2, resp2, body2) {
    console.log(JSON.parse(body2).name);
    recur(array, j + 1);
  });
}
request.get(url, function (er, resp, body) {
  if (er) console.log(er);
  else {
    recur(JSON.parse(body).characters, 0);
  }
});

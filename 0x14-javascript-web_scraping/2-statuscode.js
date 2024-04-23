#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (er, response, body) {
  if (er) throw er;
  else console.log('code:', response.statusCode);
});

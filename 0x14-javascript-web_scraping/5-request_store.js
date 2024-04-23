#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (er, resp, body) {
  if (er) console.log(er);
  else if (resp.statusCode === 200) fs.writeFile(process.argv[3], body, 'utf8', (er) => { if (er) throw er; });
});

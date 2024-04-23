#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (er, response, body) {
  if (er) console.log(er);
  else if (response.statusCode === 200) {
    let r = 0;
    const res = JSON.parse(body).res;
    const wedge = '/api/people/18/';
    for (let i = 0; i < res.length; i++) {
      if (res[i].characters.find(el => el.includes(wedge))) {
        r++;
      }
    }
    console.log(r);
  }
});

#!/usr/bin/node
const dict = require('./101-data.js').dict;
let Dict2 = {};
for (let key in dict) {
  if (Dict2[dict[key]] === undefined) {
    Dict2[dict[key]] = [key];
  } else {
    Dict2[dict[key]].push(key);
  }
}
console.log(Dict2);

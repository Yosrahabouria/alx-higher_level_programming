#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (let key in dict) {
  if (newDict[dict[key]] === undefined) {
    Dict2[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);

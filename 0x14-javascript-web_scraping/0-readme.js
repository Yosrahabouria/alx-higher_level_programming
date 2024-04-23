#!/usr/bin/node
const fs = require('fs');

fs.readFile(file_Path, 'utf8', (er, data) => {
  if (er) {
    console.error(er);
  } else {
    console.log(data);
  }
};

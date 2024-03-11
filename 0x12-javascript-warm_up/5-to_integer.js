#!/usr/bin/node

const Myarg = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(Myarg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Myarg);
}

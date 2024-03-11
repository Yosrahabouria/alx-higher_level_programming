#!/usr/bin/node

let Myarg = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(Myarg)) {
  console.log('Missing number of occurrences');
} else {
  while (Myarg > 0) {
    console.log('C is fun');
    Myarg--;
  }
}

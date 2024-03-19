#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const L = process.argv.length;
  const myArgs = [];
  for (let i = 2; i < L; i++) {
    myArgs[i - 2] = parseInt(process.argv[i]);
  }
  myArgs.sort(function (a, b) { return b - a; });
  console.log(myArgs[1]);
}

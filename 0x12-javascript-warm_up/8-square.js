#!/usr/bin/node

let Myarg = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(Myarg)) {
  console.log('Missing size');
}
let Myarg2 = 'X';
for (let i = 0; i < Myarg - 1; i++) {
	Myarg2 += 'X';
}
while (Myarg > 0) {
  console.log(Myarg2);
  Myarg2--;
}

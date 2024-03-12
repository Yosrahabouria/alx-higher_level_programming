#!/usr/bin/node

function factorial (x) {
  if (x <= 0){
    return 0;
  } else if (x === 1) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}

const myArg = parseInt(process.argv[2]);
if (isNaN(myArg)) {
  console.log('1');
} else {
  console.log(factorial(myArg));
}

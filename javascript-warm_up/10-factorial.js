#!/usr/bin/node

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const n = args[0];

console.log(factorial(n));

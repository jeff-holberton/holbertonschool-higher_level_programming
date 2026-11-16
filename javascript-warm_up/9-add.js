#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const a = Number(args[0]);
const b = Number(args[1]);

console.log(add(a, b));

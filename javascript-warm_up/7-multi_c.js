#!/usr/bin/node

const args = process.argv.slice(2);

const string = 'C is fun';
const x = Number(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < x; i++) {
  console.log(string);
}

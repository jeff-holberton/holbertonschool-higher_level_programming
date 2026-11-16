#!/usr/bin/node

const args = process.argv.slice(2);

const char = 'X';
const size = Number(args[0]);

if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    process.stdout.write(char);
  }
  process.stdout.write('\n');
}

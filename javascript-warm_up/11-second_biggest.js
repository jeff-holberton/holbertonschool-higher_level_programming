#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  let biggest = args[0];
  let secondBiggest = biggest;

  for (let i = 1; i < args.length; i++) {
    if (args[i] > biggest) {
      secondBiggest = biggest;
      biggest = args[i];
    }
  }

  console.log(secondBiggest);
}

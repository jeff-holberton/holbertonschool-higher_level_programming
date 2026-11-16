#!/usr/bin/node

const args = process.argv.slice(2);

const isEmpty = (args) => args[Symbol.iterator]().next().done;
if (isEmpty(args)) {
  console.log('No argument');
} else {
  console.log(args[0]);
}

#!/usr/bin/node

const nums = process.argv.slice(2).map(Number);

if (nums.length <= 1) {
  console.log(0);
} else {
  let biggest = nums[0];
  let secondBiggest = -Infinity;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > biggest) {
      secondBiggest = biggest;
      biggest = nums[i];
    } else if (nums[i] > secondBiggest && nums[i] < biggest) {
      secondBiggest = nums[i];
    }
  }

  console.log(secondBiggest);
}

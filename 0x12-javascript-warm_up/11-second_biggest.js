#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[3] === undefined)) {
  console.log(0);
} else {
  process.argv.shift();
  process.argv.shift();
  const arr = process.argv.map(Number).sort((a, b) => a - b).reverse();
  console.log(arr[1]);
}

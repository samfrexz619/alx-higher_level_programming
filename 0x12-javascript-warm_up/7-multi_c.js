#!/usr/bin/node
const msg = ['C is fun'];
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(msg[0]);
  }
}

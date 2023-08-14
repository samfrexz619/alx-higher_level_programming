#!/usr/bin/node
const str = 'X';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(str[0].repeat(parseInt(process.argv[2])));
  }
}

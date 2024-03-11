#!/usr/bin/node
const bashArgs = process.argv;
if (Number(bashArgs[2])) {
  console.log('My number: ' + parseInt(bashArgs[2]));
} else {
  console.log('Not a number');
}

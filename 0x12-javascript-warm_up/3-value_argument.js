#!/usr/bin/node
const bashArgs = process.argv;
if (bashArgs[2]) {
  console.log(bashArgs[2]);
} else {
  console.log('No argument');
}

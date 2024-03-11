#!/usr/bin/node
function add (a, b) {
  const args = process.argv;
  a = parseInt(args[2]);
  b = parseInt(args[3]);
  const sum = a + b;
  return sum;
}
console.log(add());

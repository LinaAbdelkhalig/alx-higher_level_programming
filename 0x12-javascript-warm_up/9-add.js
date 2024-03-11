#!/usr/bin/node
function add(a, b)
{
	let args = process.argv;
	a = parseInt(args[2]);
	b = parseInt(args[3]);
	let sum = a + b;
	return sum;
}
console.log(add());
